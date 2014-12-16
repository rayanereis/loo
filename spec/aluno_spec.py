import unittest
from should_dsl import should
from aluno import Aluno

class AlunoSpec(unittest.TestCase):

	def setUp(self):
		Aluno.alunos = {}
		Aluno.contador_matriculas = 0
		self.a = Aluno('joao', 'rua dos bobos','enrolado')

	#Construtor
	def test_atribuir_matricula(self):
		self.a.matricula |should| equal_to(1)

	def test_armazenar_instancia(self):
		Aluno.alunos |should| include_values(self.a)
	#/Construtor
	
	def test_associar_responsavel(self):
		from pessoa import Pessoa

		responsavel = Pessoa('Maria', 'rua das coves', 'casada')
		self.a.associar_responsavel(responsavel)
		self.a.responsavel |should| be(responsavel)

	def test_matricular(self):
		from curso import Curso

		curso = Curso('Informatica')
		self.a.matricular(curso)
		self.a.curso |should| be(curso)
		#curso.alunos |should| include_values(self.a)

