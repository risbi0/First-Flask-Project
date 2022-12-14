"""new fields in user model

Revision ID: 66059d98f62f
Revises: 29e612662b73
Create Date: 2022-10-19 22:24:38.308429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66059d98f62f'
down_revision = '29e612662b73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
