"""Create users table

Revision ID: dc08f3bc4a91
Revises: fd53bda9de7e
Create Date: 2021-11-22 09:37:36.573909

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Sequence, Identity

# revision identifiers, used by Alembic.
revision = 'dc08f3bc4a91'
down_revision = 'fd53bda9de7e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column("id", sa.Integer, Sequence("id"), primary_key=True),
        sa.Column("names", sa.String(255), nullable=False),
        sa.Column("lastnames", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("phone", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table("users")
