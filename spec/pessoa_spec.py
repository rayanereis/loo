import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):
	def test_criar_pessoa(self):
		p = Pessoa('joao')
		p.nome |should| equal_to('joao')
		p.id |should| equal_to(1)
		Pessoa.pessoas[1] |should| equal_to(p)

