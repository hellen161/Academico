from django.contrib import admin
from .models import *

admin.site.register([
    Cidade, Ocupacao, Pessoa, InstituicaoEnsino, AreaSaber,
    Curso, Turma, Disciplina, AvaliacaoTipo, Periodo, Matricula,
    CursoDisciplina, Avaliacao, Frequencia, Turno, Ocorrencia
])
