"""links table

Revision ID: f745352090c3
Revises: 
Create Date: 2023-01-31 16:00:21.250289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f745352090c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('short_url', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_url')
    )
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_link_url'), ['url'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('link', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_link_url'))

    op.drop_table('link')
    # ### end Alembic commands ###