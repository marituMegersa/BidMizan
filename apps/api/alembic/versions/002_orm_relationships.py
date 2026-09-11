"""Add ORM relationships and foreign key indices

Revision ID: 002_orm_relationships
Revises: None
Create Date: 2026-09-11 08:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '002_orm_relationships'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('ix_tender_centers_authority_id', 'tender_centers', ['authority_id'], unique=False)
    op.create_index('ix_procurement_auditors_center_id', 'procurement_auditors', ['center_id'], unique=False)

def downgrade():
    op.drop_index('ix_procurement_auditors_center_id', table_name='procurement_auditors')
    op.drop_index('ix_tender_centers_authority_id', table_name='tender_centers')
