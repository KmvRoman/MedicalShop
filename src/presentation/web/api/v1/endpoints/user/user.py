from fastapi import APIRouter, Depends

from src.application.create_client.dto import CreateClientDtoInput
from src.application.create_employee.dto import CreateEmployeeDtoInput
from src.application.create_order.dto import CreateOrderDtoInput
from src.application.create_product.dto import CreateProductDtoInput
from src.application.update_quantity.dto import UpdateQuantityDtoInput
from src.domain.order.entities.order import OrderProduct, OrderProductIdent, OrderId
from src.domain.product.entities.product import ProductId
from src.domain.user.write.entities.client import ClientId
from src.domain.user.write.entities.employee import EmployeeId
from src.infrastructure.ioc.interfaces import InteractorFactory
from src.presentation.web.api.v1.dependencies.dependencies import IocDependencyMarker
from src.presentation.web.api.v1.endpoints.user.dto.request import (
    CreateClientRequest, CreateEmployeeRequest,
    ProductOrderRequest, CreateOrderRequest, CreateProductRequest, UpdateProductQuantity,
)
from src.presentation.web.api.v1.endpoints.user.dto.response import Success

router = APIRouter(prefix="/api/v1", tags=["User Interface"])


@router.post(path="/client")
async def create_client(
        payload: CreateClientRequest,
        ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> ClientId:
    create_client_case = await ioc.create_client()
    client_id = await create_client_case(
        data=CreateClientDtoInput(
            full_name=payload.full_name, birthdate=payload.birthdate,
        )
    )
    return client_id


@router.post(path="/employee")
async def create_employee(
        payload: CreateEmployeeRequest,
        ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> EmployeeId:
    create_employee_case = await ioc.create_employee()
    employee_id = await create_employee_case(
        data=CreateEmployeeDtoInput(
            full_name=payload.full_name, birthdate=payload.birthdate,
        )
    )
    return employee_id


@router.post(path="/product")
async def create_product(
        payload: CreateProductRequest,
        ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> ProductId:
    create_product_case = await ioc.create_product()
    product_id = await create_product_case(
        data=CreateProductDtoInput(
            name=payload.name, quantity=payload.quantity, price=payload.price,
        )
    )
    return product_id


@router.post(path="/order")
async def create_order(
        payload: CreateOrderRequest,
        ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> OrderId:
    create_order_case = await ioc.create_order()
    order_id = await create_order_case(data=CreateOrderDtoInput(
        client_id=payload.client_id, date=payload.date,
        products=[
            OrderProductIdent(employee_id=pr.employee, product_id=pr.product)
            for pr in payload.products
        ]
    ))
    return order_id


@router.post(path="/product/add/quantity")
async def update_product_quantity(
        payload: UpdateProductQuantity,
        ioc: InteractorFactory = Depends(IocDependencyMarker)
) -> Success:
    update_quantity_case = await ioc.update_quantity()
    await update_quantity_case(data=UpdateQuantityDtoInput(
        product_id=payload.product_id, quantity_will_add=payload.quantity_add,
    ))
    return Success()
