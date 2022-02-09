"""Adding addresses table

Revision ID: 8e55781bb037
Revises: c4844850e5fc
Create Date: 2021-11-20 19:12:00.821199

"""
from alembic import op
from sqlalchemy.schema import Sequence, Identity
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8e55781bb037'
down_revision = 'c4844850e5fc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('addresses',
                    sa.Column("id", sa.Integer, Sequence("id"), primary_key=True),
                    sa.Column("address", sa.String(255), nullable=False),
                    sa.Column("district", sa.Integer(), nullable=False),
                    sa.Column("postal_code", sa.String(255), nullable=True),
                    )


def downgrade():
    op.drop_table("addresses")
