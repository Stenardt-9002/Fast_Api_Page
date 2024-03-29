"""Add User Table

Revision ID: 3271ea88f089
Revises: 61a35d94b5db
Create Date: 2023-07-18 15:17:59.387416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3271ea88f089'
down_revision = '61a35d94b5db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users" , 
                    sa.Column("id" , sa.Integer() , nullable=False),
                    sa.Column("email" , sa.String() , nullable = False),
                    sa.Column("password" , sa.String() , nullable = False),
                    sa.Column("created_at" , sa.TIMESTAMP(timezone=True) , server_default = sa.text("now()") , nullable =False) , 
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
