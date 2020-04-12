"""empty message

Revision ID: 2d60d496ad4c
Revises: 89f1bb8ffda9
Create Date: 2019-12-27 14:11:13.655720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d60d496ad4c'
down_revision = '89f1bb8ffda9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follow',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('fid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('uid', 'fid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follow')
    # ### end Alembic commands ###