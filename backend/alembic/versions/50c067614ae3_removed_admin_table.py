"""removed admin table

Revision ID: 50c067614ae3
Revises: 8fe99edfd9e8
Create Date: 2024-12-20 14:45:23.953235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50c067614ae3'
down_revision: Union[str, None] = '8fe99edfd9e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_name', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
