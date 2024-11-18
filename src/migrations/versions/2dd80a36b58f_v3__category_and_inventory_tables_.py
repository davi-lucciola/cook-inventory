"""V3__category_and_inventory_tables_created

Revision ID: 2dd80a36b58f
Revises: b12f0ea206af
Create Date: 2024-11-18 16:51:02.467081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dd80a36b58f'
down_revision = 'b12f0ea206af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('alert_quantity', sa.Float(), nullable=False),
    sa.Column('measure', sa.Enum('G', 'L', 'ML', 'KG', 'UNIT', name='measure'), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventories')
    # ### end Alembic commands ###
