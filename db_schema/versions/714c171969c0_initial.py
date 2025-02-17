"""initial

Revision ID: 714c171969c0
Revises: 
Create Date: 2025-02-18 17:28:11.232451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '714c171969c0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('security',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=False),
    sa.Column('board', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('candle',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('security_id', sa.UUID(), nullable=False),
    sa.Column('timeframe', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('open', sa.Float(), nullable=False),
    sa.Column('high', sa.Float(), nullable=False),
    sa.Column('low', sa.Float(), nullable=False),
    sa.Column('close', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['security_id'], ['security.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candle')
    op.drop_table('security')
    # ### end Alembic commands ###
