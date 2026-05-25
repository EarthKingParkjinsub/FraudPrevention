"""add user detail fields

Revision ID: 20260511_0005
Revises: 20260413_0004
Create Date: 2026-05-11 16:30:00
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260511_0005"
down_revision = "20260413_0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("age_group", sa.String(length=20), nullable=True))
    op.add_column("users", sa.Column("job", sa.String(length=30), nullable=True))
    op.add_column("users", sa.Column("main_bank", sa.String(length=30), nullable=True))
    op.add_column("users", sa.Column("residence", sa.String(length=100), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "residence")
    op.drop_column("users", "main_bank")
    op.drop_column("users", "job")
    op.drop_column("users", "age_group")
