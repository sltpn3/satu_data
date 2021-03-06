"""alter table opd

Revision ID: 55f038048030
Revises: 422693177c04
Create Date: 2021-12-20 17:16:03.175685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55f038048030'
down_revision = '422693177c04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('opd', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('opd', 'is_active')
    # ### end Alembic commands ###
