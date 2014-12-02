import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):
	def setUp(self):
		Pessoa.pessoas = {}
		Pessoa.contador_id = 0

	def tearDown(self):
		pass

	def test_criar_pessoa(self):
		p = Pessoa('joao', 'rua dos bobos','enrolado')
		p.nome |should| equal_to('joao')
		p.endereco |should| equal_to('rua dos bobos')
		p.estado_civil |should| equal_to('enrolado')
		p.id |should| equal_to(1)
		Pessoa.pessoas[1] |should| equal_to(p)
		#alternativa aa expectativa anterior
		Pessoa.pessoas |should| include_values(p)

	def test_alterar_endereco(self):
		p = Pessoa('joao', 'rua dos bobos','enrolado')
		p.alterar_endereco('rua das coves')
		p.endereco |should| equal_to('rua das coves')

	def test_alterar_estado_civil(self):
		p = Pessoa('joao', 'rua dos bobos','enrolado')
		p.alterar_estado_civil('casado')
		p.estado_civil |should| equal_to('casado')


