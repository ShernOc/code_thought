"""empty message

Revision ID: a1b16ec56cc5
Revises: 6d926965f8a6
Create Date: 2024-12-18 12:30:37.513753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b16ec56cc5'
down_revision: Union[str, None] = '6d926965f8a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
