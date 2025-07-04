"""Changed field

Revision ID: 9b4f3a94e264
Revises: 2be0fc404953
Create Date: 2025-06-02 15:49:00.933969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b4f3a94e264'
down_revision = '2be0fc404953'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('_password')

    # ### end Alembic commands ###
