from game import Game


def test_instancia_game():
	game = Game()
	assert game.suspeitos != []
	assert game.locais != []
	assert game.armas != []


def test_inicializa_game():
	game = Game()
	assert game.cenario == []
	game.inicializar()
	assert game.cenario != []
	assert len(game.cenario) == 3


def test_checar_hipotese():
	game = Game()
	game.inicializar()
	assert game.checar_hipotese('1,1,1') in [0, 1, 2, 3]


def test_ganhar_jogo():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('0,0,0') == 0


def test_errar_suspeito():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('1,0,0') == 1


def test_errar_local():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('0,1,0') == 2


def test_errar_arma():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('0,0,1') == 3


def test_errar_arma_e_suspeito():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('1,0,1') in [1,3]


def test_errar_local_e_suspeito():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('1,1,0') in [1,2]


def test_errar_arma_e_local():
	game = Game()
	game.inicializar()
	game.cenario = [0, 0, 0]
	assert game.checar_hipotese('0,1,1') in [2,3]


def test_descobrir_crime():
	game = Game()
	game.inicializar()
	assert game.resolve_jogo() == 0