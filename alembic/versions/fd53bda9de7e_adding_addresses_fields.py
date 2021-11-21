"""Adding addresses fields

Revision ID: fd53bda9de7e
Revises: 8e55781bb037
Create Date: 2021-11-20 19:17:41.392572

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'fd53bda9de7e'
down_revision = '8e55781bb037'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("addresses", sa.Column("province", sa.Integer(), nullable=False))
    op.add_column("addresses", sa.Column("department", sa.Integer(), nullable=False))


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if "province" in tables:
        op.drop_column("addresses", "province")
    if "department" in tables:
        op.drop_column("addresses", "department")
