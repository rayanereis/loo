import unittest
from should_dsl import should
from aluno import Aluno

class AlunoSpec(unittest.TestCase):

	def setUp(self):
		Aluno.alunos = {}
		Aluno.contador_matriculas = 0
		self.a = Aluno('joao', 'rua dos bobos','enrolado')

	#Construtor
	def test_atribui_matricula(self):
		self.a.matricula |should| equal_to(1)

	def test_armazena_instancia(self):
		Aluno.alunos |should| include_values(self.a)

	#/Construtor
	

