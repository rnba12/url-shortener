"""duplicate urls

Revision ID: 09be7fefb7f6
Revises: f745352090c3
Create Date: 2023-02-01 15:49:53.770985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09be7fefb7f6'
down_revision = 'f745352090c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.drop_index('ix_link_url')
        batch_op.create_index(batch_op.f('ix_link_url'), ['url'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_link_url'))
        batch_op.create_index('ix_link_url', ['url'], unique=False)

    # ### end Alembic commands ###