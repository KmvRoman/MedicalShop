"""add tables

Revision ID: 4a5f2968fb83
Revises: 
Create Date: 2023-11-11 13:55:22.927135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a5f2968fb83'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clienttable',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, cache=1), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('birthdate', sa.DATE(), nullable=False),
    sa.Column('date_registration', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employeetable',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, cache=1), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('birthdate', sa.DATE(), nullable=False),
    sa.Column('date_registration', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producttable',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, cache=1), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('quantity', sa.INTEGER(), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ordertable',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, cache=1), nullable=False),
    sa.Column('client_id', sa.BIGINT(), nullable=False),
    sa.Column('price', sa.BIGINT(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clienttable.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderproducttable',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, cache=1), nullable=False),
    sa.Column('order_id', sa.BIGINT(), nullable=False),
    sa.Column('employee_id', sa.BIGINT(), nullable=False),
    sa.Column('product_id', sa.BIGINT(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employeetable.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['order_id'], ['ordertable.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['producttable.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderproducttable')
    op.drop_table('ordertable')
    op.drop_table('producttable')
    op.drop_table('employeetable')
    op.drop_table('clienttable')
    # ### end Alembic commands ###