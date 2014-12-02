import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):
	def test_aaa(self):
		p = Pessoa('t')

	def test_criar_pessoa(self):
		Pessoa.pessoas = {}
		Pessoa.contador_id = 0
		p = Pessoa('joao')
		p.nome |should| equal_to('joao')
		p.id |should| equal_to(1)
		Pessoa.pessoas[1] |should| equal_to(p)

