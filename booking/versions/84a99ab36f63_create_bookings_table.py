"""create bookings table

Revision ID: 84a99ab36f63
Revises: 
Create Date: 2022-10-31 19:48:38.093300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a99ab36f63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(12), nullable=False),
    )
    op.create_table(
        'rooms',
        sa.Column('room_id', sa.Integer, primary_key=True),
        sa.Column('room_name', sa.String(12), nullable=False),
        sa.Column('capacity', sa.Integer, nullable=False),
    )
    op.create_table(
        'bookings',
        sa.Column('booking_id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('book_num', sa.Integer, nullable=False),
        sa.Column('start_datetime', sa.DateTime, nullable=False),
        sa.Column('end_datetime', sa.DateTime, nullable=False),
    )

def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('rooms')
    op.drop_table('bookings')
