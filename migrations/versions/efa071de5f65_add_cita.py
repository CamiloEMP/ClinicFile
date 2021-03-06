"""add cita

Revision ID: efa071de5f65
Revises: 0c57e25fff96
Create Date: 2021-10-18 18:00:02.634773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efa071de5f65'
down_revision = '0c57e25fff96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('citas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medico_id', sa.Integer(), nullable=True),
    sa.Column('fecha_hora', sa.DateTime(), nullable=True),
    sa.Column('duracion', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Text(), nullable=True),
    sa.Column('paciente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['medico_id'], ['medicos.id'], ),
    sa.ForeignKeyConstraint(['paciente_id'], ['pacientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('citas')
    # ### end Alembic commands ###
