"""create phone number table

Revision ID: 40f21f190425
Revises: 
Create Date: 2024-09-03 19:48:34.342924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40f21f190425'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(20), nullable=True))


def downgrade() -> None:
    pass
