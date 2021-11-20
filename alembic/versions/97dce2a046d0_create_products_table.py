"""create products table

Revision ID: 97dce2a046d0
Revises: 
Create Date: 2021-11-19 12:41:13.861642

"""
from alembic import op
from sqlalchemy.schema import Sequence
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '97dce2a046d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column("id", sa.Integer, Sequence("id"), primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("stock", sa.Integer(), nullable=False)
    )


def downgrade():
    op.drop_table("products")
