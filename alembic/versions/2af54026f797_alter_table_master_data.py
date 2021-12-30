"""alter table master_data

Revision ID: 2af54026f797
Revises: ea19ae27a841
Create Date: 2021-12-23 10:37:31.746089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2af54026f797'
down_revision = 'ea19ae27a841'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('master_data', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('master_data', 'is_active')
    # ### end Alembic commands ###
