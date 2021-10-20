"""add paciente

Revision ID: 0c57e25fff96
Revises: 
Create Date: 2021-10-18 14:56:36.394195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c57e25fff96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pacientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=True),
    sa.Column('telefono', sa.Text(), nullable=True),
    sa.Column('tipo_documento', sa.Text(), nullable=True),
    sa.Column('no_documento', sa.BigInteger(), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('correo', sa.Text(), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pacientes')
    # ### end Alembic commands ###
