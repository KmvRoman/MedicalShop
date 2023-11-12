from sqlalchemy import select, func, distinct

from src.domain.user.read.client_stats import ClientStats
from src.domain.user.read.employee_stats import EmployeeStats
from src.domain.user.write.entities.employee import EmployeeId
from src.domain.user.write.entities.client import ClientId
from src.infrastructure.database import ClientTable, OrderProductTable, ProductTable, OrderTable, EmployeeTable
from src.infrastructure.database.repositories.base import BaseRepository
from src.infrastructure.database.serialize.statistic.mapping import (
    serialize_employees_statistic, serialize_employee_statistic, serialize_client_statistic,
)


class StatisticRepository(BaseRepository):
    async def read_client_statistics(self, client_id: ClientId, year: int, month: int) -> ClientStats | None:
        stmt = select(
            ClientTable.id, ClientTable.full_name, func.count(OrderProductTable.product_id),
            func.sum(ProductTable.price),
        ).select_from(ClientTable).join(
            OrderTable, ClientTable.id == OrderTable.client_id
        ).join(
            OrderProductTable, OrderTable.id == OrderProductTable.order_id
        ).join(
            ProductTable, OrderProductTable.product_id == ProductTable.id
        ).where(
            ClientTable.id == client_id,
            func.date_part("YEAR", OrderTable.date) == year,
            func.date_part("MONTH", OrderTable.date) == month,
        ).group_by(ClientTable.id)
        result = (await self.session.execute(stmt)).all()
        return serialize_client_statistic(payload=result)

    async def read_employee_statistic(
            self, employee_id: EmployeeId, year: int, month: int,
    ) -> EmployeeStats | None:
        stmt = select(
            EmployeeTable.id, EmployeeTable.full_name, func.count(distinct(OrderTable.client_id)),
            func.count(OrderProductTable.id), func.sum(ProductTable.price)
        ).select_from(EmployeeTable).join(
            OrderProductTable, OrderProductTable.employee_id == EmployeeTable.id
        ).join(
            OrderTable, OrderProductTable.order_id == OrderTable.id
        ).join(
            ProductTable, ProductTable.id == OrderProductTable.product_id
        ).where(
            EmployeeTable.id == employee_id,
            func.date_part("YEAR", OrderTable.date) == year,
            func.date_part("MONTH", OrderTable.date) == month,
        ).group_by(EmployeeTable.id)
        result = (await self.session.execute(stmt)).all()
        return serialize_employee_statistic(payload=result)

    async def read_employees_statistic(self, year: int, month: int) -> list[EmployeeStats]:
        stmt = select(
            EmployeeTable.id, EmployeeTable.full_name, func.count(distinct(OrderTable.client_id)),
            func.count(OrderProductTable.id), func.sum(ProductTable.price)
        ).select_from(EmployeeTable).join(
            OrderProductTable, OrderProductTable.employee_id == EmployeeTable.id
        ).join(
            OrderTable, OrderProductTable.order_id == OrderTable.id
        ).join(
            ProductTable, ProductTable.id == OrderProductTable.product_id
        ).where(
            func.date_part("YEAR", OrderTable.date) == year,
            func.date_part("MONTH", OrderTable.date) == month,
        ).group_by(EmployeeTable.id)
        result = (await self.session.execute(stmt)).all()
        return serialize_employees_statistic(payload=result)
