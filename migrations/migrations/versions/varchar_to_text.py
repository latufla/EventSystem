"""empty message

Revision ID: a2e65d235e4c
Revises: a8e25d235e4c
Create Date: 2017-11-5

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2e65d235e4c'
down_revision = 'a8e25d235e4c'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("user", "login", existing_type=sa.String(80), type_=sa.String(20))
    op.alter_column("user", "gender", existing_type=sa.String(80), type_=sa.String(6))
    op.alter_column("user", "image_big", existing_type=sa.String(120), type_=sa.Text)
    op.alter_column("user", "role", existing_type=sa.String(80), type_=sa.String(10))

    op.alter_column("event", "title", existing_type=sa.String(80), type_=sa.Text)
    op.alter_column("event", "description_short", existing_type=sa.String(80), type_=sa.Text)
    op.alter_column("event", "description", existing_type=sa.String(120), type_=sa.Text)
    op.alter_column("event", "status", existing_type=sa.String(80), type_=sa.String(20))
    op.alter_column("event", "result_file", existing_type=sa.String(120), type_=sa.Text)
    op.alter_column("event", "image_big", existing_type=sa.String(120), type_=sa.Text)


def downgrade():
    op.alter_column("user", "login", type_=sa.String(80), existing_type=sa.String(20))
    op.alter_column("user", "gender", type_=sa.String(80), existing_type=sa.String(6))
    op.alter_column("user", "image_big", type_=sa.String(120), existing_type=sa.Text)
    op.alter_column("user", "role", type_=sa.String(80), existing_type=sa.String(10))

    op.alter_column("event", "title", type_=sa.String(80), existing_type=sa.Text)
    op.alter_column("event", "description_short", type_=sa.String(80), existing_type=sa.Text)
    op.alter_column("event", "description", type_=sa.String(120), existing_type=sa.Text)
    op.alter_column("event", "status", type_=sa.String(80), existing_type=sa.String(20))
    op.alter_column("event", "result_file", type_=sa.String(120), existing_type=sa.Text)
    op.alter_column("event", "image_big", type_=sa.String(120), existing_type=sa.Text)
