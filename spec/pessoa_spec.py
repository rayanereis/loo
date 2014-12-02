import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):

	def setUp(self):
		Pessoa.pessoas = {}
		Pessoa.contador_id = 0
		self.p = Pessoa('joao', 'rua dos bobos','enrolado')

	#Construtor
	def test_atribui_id(self):
		self.p.id |should| equal_to(1)

	def test_armazena_instancia(self):
		Pessoa.pessoas |should| include_values(self.p)

	def test_inicializa_atributos(self):
		self.p.nome |should| equal_to('joao')
		self.p.endereco |should| equal_to('rua dos bobos')
		self.p.estado_civil |should| equal_to('enrolado')
	#/Construtor

	def test_alterar_endereco(self):
		self.p.alterar_endereco('rua das coves')
		self.p.endereco |should| equal_to('rua das coves')

	def test_alterar_estado_civil(self):
		self.p.alterar_estado_civil('casado')
		self.p.estado_civil |should| equal_to('casado')


