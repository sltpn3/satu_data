"""alter table input_history

Revision ID: 467c99c9a450
Revises: 4c48ebfa74bc
Create Date: 2021-12-15 15:05:48.574981

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '467c99c9a450'
down_revision = '4c48ebfa74bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('input_history', sa.Column('value_int', sa.Integer(), nullable=True))
    op.add_column('input_history', sa.Column('value_float', sa.Float(), nullable=True))
    op.add_column('input_history', sa.Column('value_text', sa.Text(), nullable=True))
    op.drop_column('input_history', 'value')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('input_history', sa.Column('value', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('input_history', 'value_text')
    op.drop_column('input_history', 'value_float')
    op.drop_column('input_history', 'value_int')
    # ### end Alembic commands ###
