#coding:utf-8

import pygame, os, random
from pygame.locals import *

# Define a posição da janela
os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"

# Inicia o PyGame
pygame.init()

# Tela de 640x480
tela = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Caindo!")

# Máximo FPS do jogo
fps = 80

# Encurta a variável de mouse
mouse = pygame.mouse

# Encurta a variável de clock
clock = pygame.time.Clock()

# Barrinha do jogador
bar = pygame.Surface((80,20))
bar = bar.convert()
bar.fill((0,0,255))

# Prepara o fundo do jogo para ser utilizado
tela_tam = {"larg": 1024, "alt": 768}
fundo = pygame.Surface((tela_tam["larg"],tela_tam["alt"]))
fundo = fundo.convert()
fundo.fill((200,200,200))

# Prepara uma partícula que cai :)
particula = pygame.Surface((20,20))
particula = particula.convert()
particula.fill((0,0,0))

# Partícula na tela?
part_tela = False

# Esconde o ponteiro do mouse
mouse.set_visible(False)

# Define a velocidade inicial
veloc = 0.3

while True:
	# Verifica os eventos de teclado
	for evt in pygame.event.get():
		# Se for pra sair (X no canto ou tecla ESC)
		if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
			exit()

	tela.blit(fundo, (0,0))
	
	# Pega o tempo do processador
	tempo = clock.tick(fps)

	# Gera uma partícula
	if not part_tela:
		part_pos = {"x": random.randint(1,tela_tam["larg"]-20), "y": 20}
		part_tela = True
	else:
		part_pos["y"] += tempo * veloc

	tela.blit(particula, (part_pos["x"], part_pos["y"]))

	# Pega a posição do mouse
	mouse_pos = mouse.get_pos()

	# Desenhamos a barra na tela, utilizando apenas a posição X do mouse, já que Y é fixo
	# e dependendo do tamanho da tela, Y também muda.
	if mouse_pos[0] < 0:
		mouse_x = 0
	# Largura - 80 (que é a largura da barra)
	elif mouse_pos[0] > tela_tam["larg"] - 80:
		mouse_x = tela_tam["larg"] - 80
	else:
		mouse_x = mouse_pos[0]
	
	# Deixamos 50 de espaço da base da tela até a barra
	mouse_y = tela_tam["alt"] - 50
	
	# Desenha a barra
	tela.blit(bar, (mouse_x, mouse_y))

	# Prepara os Rects da barra e da partícula
	bar_rect = pygame.Rect((mouse_x,mouse_y), (80,20))
	part_rect = pygame.Rect((part_pos["x"], part_pos["y"]), (20,20))

	# Detectar colisão
	if bar_rect.colliderect(part_rect):
		part_tela = False
		veloc += 0.1

	# Verifica se a partícula saiu da tela
	if part_pos['y']>tela_tam['alt']:
		part_tela=False #depois da pra implementar alguma coisa a mais, como diminuir a velocidade, etc...
	pygame.display.flip()
