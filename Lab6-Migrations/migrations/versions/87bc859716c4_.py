"""empty message

Revision ID: 87bc859716c4
Revises: 8efca74dd9d2
Create Date: 2021-04-05 18:46:35.948830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87bc859716c4'
down_revision = '8efca74dd9d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_empl', schema=None) as batch_op:
        batch_op.alter_column('empl_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('task_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_empl', schema=None) as batch_op:
        batch_op.alter_column('task_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('empl_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
