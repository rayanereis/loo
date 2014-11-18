import unittest
from should_dsl import should
from pessoa import Pessoa


class PessoaSpec(unittest.TestCase):
	def test_atribui_nome_a_uma_pessoa(self):
		p = Pessoa('joao')
		p.nome |should| equal_to('joao')

