import random
import pdb

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
		print("cenário gerado: Morto por " + self.suspeitos[self.cenario[0]]\
			  + " com " + self.armas[self.cenario[2]] + " em " + self.locais[self.cenario[1]])

	def checar_hipotese(self, hipotese):
		array_hipotese = hipotese.split(',')
		array_hipotese = [int(i) for i in array_hipotese] #convetendo para inteiros
		erros = []
		
		for i in range(len(self.cenario)):
			if self.cenario[i] != array_hipotese[i]: erros.append(i+1)

		if erros == []:
			return 0 
		else:
			return random.choice(erros)

	def resolve_jogo(self, _suspeitos=[], _locais=[], _armas=[], qtdJogadas=0):
		#pdb.set_trace()
		if _suspeitos == [] and _locais == [] and _armas == []:
			_suspeitos = [ i for i in range(0, len(self.suspeitos))]			
			_locais = [ i for i in range(0, len(self.locais))]
			_armas = [ i for i in range(0, len(self.armas))]
			return self.resolve_jogo(_suspeitos=_suspeitos, _locais=_locais, _armas=_armas, qtdJogadas=qtdJogadas)

		if len(_suspeitos) > 1: idSuspeito = random.randint(0, len(_suspeitos)-1)
		else: idSuspeito = 0

		if len(_locais) > 1: idLocal = random.randint(0, len(_locais)-1)
		else: idLocal = 0

		if len(_armas) > 1: idArma = random.randint(0, len(_armas)-1)
		else: idArma = 0

		qtdJogadas += 1

		print("Testando hipotese " + str(qtdJogadas) + ": Morto com " + self.armas[_armas[idArma]]+ \
			  " em " + self.locais[_locais[idLocal]] + ' por ' + self.suspeitos[_suspeitos[idSuspeito]])

		_hipotese = str(_suspeitos[idSuspeito]) + ',' + str(_locais[idLocal]) + ',' + str(_armas[idArma])
		resultado_hipotese = self.checar_hipotese(_hipotese)

		'''
		print(dict(hipotese = _hipotese,
					cenario = self.cenario,
					resultado_hipotese = resultado_hipotese,
					suspeitos = _suspeitos,
					locais = _locais,
					armas = _armas))
		'''

		if resultado_hipotese == 0:
			print("Caso solucionado!")
			print("fim do jogo!")
			return 0

		if resultado_hipotese == 1: _suspeitos.pop(idSuspeito)
		if resultado_hipotese == 2: _locais.pop(idLocal)
		if resultado_hipotese == 3: _armas.pop(idArma)

		return self.resolve_jogo(_suspeitos=_suspeitos, _locais=_locais, _armas=_armas, qtdJogadas=qtdJogadas)



if __name__ == '__main__':
	game = Game()
	game.inicializar()
	game.resolve_jogo()
	pass
