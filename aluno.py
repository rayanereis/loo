from pessoa import Pessoa

class Aluno(Pessoa):

	alunos = {}
	contador_matriculas = 0

	@classmethod
	def inserir(cls, aluno):
		cls.alunos[aluno.matricula] = aluno

	@classmethod
	def identificar(cls):
		cls.contador_matriculas = cls.contador_matriculas + 1
		return cls.contador_matriculas

	def __init__(self, nome, endereco, estado_civil):
		Pessoa.__init__(self, nome, endereco, estado_civil)
		self.matricula = Aluno.identificar()
		Aluno.inserir(self)

	def associar_responsavel(self, responsavel):
		self.responsavel = responsavel

	def matricular(self, curso):
		self.curso = curso
