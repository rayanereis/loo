class Pessoa:

	pessoas = {}
	contador_id = 0

	@classmethod
	def insere(cls, pessoa):
		cls.pessoas[pessoa.id] = pessoa

	@classmethod
	def identifica(cls):
		cls.contador_id = cls.contador_id + 1
		return cls.contador_id

	def __init__(self, nome):
		self.nome = nome
		self.id = Pessoa.identifica()
		Pessoa.insere(self)
