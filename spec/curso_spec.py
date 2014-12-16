import unittest
from should_dsl import should
from curso import Curso

class CursoSpec(unittest.TestCase):
	def test_criar_curso(self):
		c = Curso('Arquitetura')
		c.nome |should| equal_to('Arquitetura')

