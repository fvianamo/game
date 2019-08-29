import random

class Game:

	suspeitos = ['Charles B. Abbage',
				 'Donald Duck Knuth',
				 'Ada L. Ovelace',
				 'Alan T. Uring',
				 'Ivar J. Acobson',
				 'Ras Mus Ler Dorf']

	locais = 	['Redmond',
				 'Palo Alto',
				 'San Francisco',
				 'Tokio',
				 'Restaurante no Fim do Universo',
				 'São Paulo',
				 'Cupertino',
				 'Helsinki',
				 'Maida Vale',
				 'Toronto']

	armas =		['Peixeira',
				 'DynaTAC 8000X',
				 'Trezoitão',
				 'Trebuchet',
				 'Maça',
				 'Gládio']

	def inicializar(self):
		self.cenario = [random.choice(self.suspeitos),
						random.choice(self.locais),
						random.choice(self.armas)]
		print("cenário gerado: " + str(self.cenario))