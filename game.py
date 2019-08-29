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

	cenario = []

	def inicializar(self):
		self.cenario = [random.randint(0, len(self.suspeitos)-1),
						random.randint(0, len(self.locais)-1),
						random.randint(0, len(self.armas)-1)]
		print("cenário gerado: " + str(self.cenario))

	def checar_hipotese(self, hipotese):
		array_hipotese = hipotese.split(',')
		#convetendo para inteiros
		array_hipotese = [int(i) for i in array_hipotese] 
		erros = []
		
		for i in range(len(self.cenario)):
			if self.cenario[i] != array_hipotese[i]: erros.append(i+1)

		if erros == []:
			return 0 
		else:
			return random.choice(erros)

	def resolve_jogo():
		pass


if __name__ == '__main__':
	# Jogo vai aqui
	pass
