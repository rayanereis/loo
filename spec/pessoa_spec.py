import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):
	def test_criar_pessoa(self):
		Pessoa.pessoas = {}
		Pessoa.contador_id = 0
		p = Pessoa('joao', 'rua dos bobos')
		p.nome |should| equal_to('joao')
		p.endereco |should| equal_to('rua dos bobos')
		p.id |should| equal_to(1)
		Pessoa.pessoas[1] |should| equal_to(p)

	def test_alterar_endereco(self):
		p = Pessoa('joao', 'rua dos bobos')
		p.alterar_endereco('rua das coves')
		p.endereco |should| equal_to('rua das coves')
