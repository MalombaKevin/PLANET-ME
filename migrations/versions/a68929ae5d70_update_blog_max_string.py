"""update  blog max string

Revision ID: a68929ae5d70
Revises: d92fd14fa88e
Create Date: 2022-05-19 07:56:21.750324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a68929ae5d70'
down_revision = 'd92fd14fa88e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('megapitch', 'country')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('megapitch', sa.Column('country', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
