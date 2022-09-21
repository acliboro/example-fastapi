"""add content column to posts table

Revision ID: 4f47ac26fca1
Revises: 3d01af97d375
Create Date: 2022-09-16 10:44:48.975759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f47ac26fca1'
down_revision = '3d01af97d375'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
