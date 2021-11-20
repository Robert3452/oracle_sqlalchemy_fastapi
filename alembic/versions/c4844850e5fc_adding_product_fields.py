"""adding product fields

Revision ID: c4844850e5fc
Revises: 97dce2a046d0
Create Date: 2021-11-20 07:22:08.940389

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c4844850e5fc'
down_revision = '97dce2a046d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("products", sa.Column('image', sa.String(255), nullable=False))
    op.add_column("products", sa.Column('longDescription', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('products', 'image')
    op.drop_column('products', 'longDescription')