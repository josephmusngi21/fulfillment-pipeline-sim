"""create initial schema scaffold

Revision ID: 20260421_0001
Revises:
Create Date: 2026-04-21 00:00:00

TODO: Implement initial schema migration operations.
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "20260421_0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """TODO: Create initial database tables and constraints."""
    pass


def downgrade() -> None:
    """TODO: Drop initial database tables and constraints."""
    pass
