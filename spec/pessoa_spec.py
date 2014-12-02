import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass

	def setUp(self):
		Pessoa.pessoas = {}
		Pessoa.contador_id = 0
		self.p = Pessoa('joao', 'rua dos bobos','enrolado')

	def tearDown(self):
		pass

	def test_criar_pessoa(self):
		#Na pratica anula os efeitos do setUp(), por ser um teste de "inicio do mundo"
		Pessoa.pessoas = {}
		Pessoa.contador_id = 0
		uma_pessoa = Pessoa('joao', 'rua dos bobos','enrolado')
		#
		uma_pessoa.nome |should| equal_to('joao')
		uma_pessoa.endereco |should| equal_to('rua dos bobos')
		uma_pessoa.estado_civil |should| equal_to('enrolado')
		uma_pessoa.id |should| equal_to(1)
		Pessoa.pessoas[1] |should| equal_to(uma_pessoa)
		#alternativa aa expectativa anterior
		Pessoa.pessoas |should| include_values(uma_pessoa)

	def test_alterar_endereco(self):
		self.p.alterar_endereco('rua das coves')
		self.p.endereco |should| equal_to('rua das coves')

	def test_alterar_estado_civil(self):
		self.p.alterar_estado_civil('casado')
		self.p.estado_civil |should| equal_to('casado')


