from game import Game


def test_instancia_game():
	game = Game()
	assert game.suspeitos != []
	assert game.locais != []
	assert game.armas != []


def test_inicializa_game():
	game = Game()
	game.inicializar()
	assert game.cenario != []
	assert len(game.cenario) == 3