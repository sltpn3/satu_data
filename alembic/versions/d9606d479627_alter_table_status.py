"""alter table status

Revision ID: d9606d479627
Revises: edd2abd9d638
Create Date: 2021-12-07 15:28:51.775025

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd9606d479627'
down_revision = 'edd2abd9d638'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('status', sa.Column('role_in_process', sa.Integer(), nullable=True))
    op.drop_constraint('fk_status_role_id_role', 'status', type_='foreignkey')
    op.create_foreign_key(op.f('fk_status_role_in_process_role'), 'status', 'role', ['role_in_process'], ['id'])
    op.drop_column('status', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('status', sa.Column('role_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(op.f('fk_status_role_in_process_role'), 'status', type_='foreignkey')
    op.create_foreign_key('fk_status_role_id_role', 'status', 'role', ['role_id'], ['id'])
    op.drop_column('status', 'role_in_process')
    # ### end Alembic commands ###
