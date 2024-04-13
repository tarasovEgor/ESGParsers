"""empty message

Revision ID: 81d4e0456e95
Revises: 3a79a22b07ba
Create Date: 2022-11-11 13:31:55.292956

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "81d4e0456e95"
down_revision = "3a79a22b07ba"
branch_labels = None
depends_on = None

bank = sa.table(
    "bank",
    sa.Column("id", sa.Integer()),
    sa.Column("licence", sa.String()),
    sa.Column("bank_type_id", sa.Integer()),
    sa.Column("bank_name", sa.String()),
    sa.Column("description", sa.String()),
)


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("bank", sa.Column("licence", sa.String(), nullable=True))
    op.create_index(op.f("ix_bank_licence"), "bank", ["licence"], unique=False)
    op.execute(sa.update(bank).where(bank.c.bank_type_id == 1).values(licence=bank.c.id))
    # op.execute("update bank set licence = id where bank_type_id=1")
    op.execute("ALTER SEQUENCE bank_id_seq RESTART WITH 10000")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_bank_licence"), table_name="bank")
    op.drop_column("bank", "licence")
    # ### end Alembic commands ###