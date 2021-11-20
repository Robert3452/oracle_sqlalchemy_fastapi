"""adding product fields

Revision ID: c4844850e5fc
Revises: 97dce2a046d0
Create Date: 2021-11-20 07:22:08.940389

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'c4844850e5fc'
down_revision = '97dce2a046d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("products", sa.Column(
        'image', sa.String(255), nullable=False))

    op.add_column("products", sa.Column(
        'long_description', sa.Text(), nullable=True))

    op.add_column("products", sa.Column('enabled', sa.CHAR(1), default=True))


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if "image" in tables:
        op.drop_column('products', 'image')
    if "longDescription" in tables:
        op.drop_column('products', 'long_description')
    if "enabled" in tables:
        op.drop_column('products', 'enabled')

