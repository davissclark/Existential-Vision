"""big update

Revision ID: 2ca28381576
Revises: 5ac1de91ab9
Create Date: 2014-10-13 20:40:50.680167

"""

# revision identifiers, used by Alembic.
revision = '2ca28381576'
down_revision = '5ac1de91ab9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('url', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tags', 'url')
    ### end Alembic commands ###
