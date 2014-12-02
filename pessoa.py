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

	def __init__(self, nome, endereco, estado_civil):
		self.nome = nome
		self.endereco = endereco
		self.estado_civil = estado_civil
		self.id = Pessoa.identifica()
		Pessoa.insere(self)

	def alterar_endereco(self, novo_endereco):
		self.endereco = novo_endereco

	def alterar_estado_civil(self, novo_estado_civil):
		self.estado_civil = novo_estado_civil
