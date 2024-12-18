"""Renaming admins to admin

Revision ID: 3da85ff116d6
Revises: fcc22e451984
Create Date: 2024-12-18 14:03:41.024882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da85ff116d6'
down_revision: Union[str, None] = 'fcc22e451984'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
