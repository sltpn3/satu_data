"""alter table urusan

Revision ID: 1962d3edad1a
Revises: 55f038048030
Create Date: 2021-12-20 17:50:14.375155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1962d3edad1a'
down_revision = '55f038048030'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('urusan', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('urusan', 'is_active')
    # ### end Alembic commands ###
