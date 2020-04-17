# coding:utf-8
# caindo/jogo.py

import pygame, os, random, time
from pygame.locals import *

# Define a posição da janela
os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"

# Inicia o pygame
pygame.init()

# Define a tela
tela_tam = {"larg": 800, "alt": 600}

tela = pygame.display.set_mode((tela_tam["larg"], tela_tam["alt"]))

pygame.display.set_caption("Caindo")

# Máximo FPS
fps = 80

# Encurta a variável do mouse
mouse = pygame.mouse

# Encurta a variável do clock
clock = pygame.time.Clock()

# Barrinha do jogador
bar = pygame.Surface((80,20))
bar = bar.convert()
bar.fill((0,0,255))

# Prepara o fundo do jogo
fundo = pygame.Surface((tela_tam["larg"], tela_tam["alt"]))
fundo = fundo.convert()
fundo.fill((255,255,255))

# Esconde o ponteiro do mouse
mouse.set_visible(False)

# Prepara a partícula que cai
particula = pygame.Surface((20,20))
particula.convert()
particula.fill((0,0,0))

# Partícula na tela?
part_tela = False

relogio = 10

# Velocidade inicial de queda
veloc = 0.3

# Pontos
pontos = 0
errou = 0

# Fonte
fonte = pygame.font.SysFont("Arial",40)

# Começa o jogo
while True:
	# Verifica os eventos
	for evt in pygame.event.get():
		# Sair
		if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
			exit()

	# Pega a posição do mouse
	mouse_pos = mouse.get_pos()

	bar_x = mouse_pos[0]
	if bar_x > tela_tam["larg"] - 80:
		bar_x = tela_tam["larg"] - 80

	bar_y = tela_tam["alt"] - 50

	# Pega o tempo do processador
	tempo = clock.tick(fps)

	# Gera uma partícula
	if not part_tela:
		part_tela = True
		# Cor da partícula
		r = random.randint(0,220)
		g = random.randint(0,220)
		b = random.randint(0,220)
		particula.fill((r,g,b))
		# Posição da partícula
		part_pos = {"x": random.randint(1,tela_tam["larg"]-20), "y":20}
	else:
		part_pos["y"] += tempo * veloc

	# Desenha o fundo
	tela.blit(fundo, (0,0))

	# Desenha a barra do jogador
	tela.blit(bar, (bar_x, bar_y))

	# Desenha a partícula
	tela.blit(particula, (part_pos["x"],part_pos["y"]))

	# Pontuação
	pts_fonte = fonte.render(str(pontos), True, (30,30,30))
	tela.blit(pts_fonte, (20,20))

	errou_fonte = fonte.render(str(errou), True, (255,0,0))
	tela.blit(errou_fonte, (20,70))

	# Prepara os Rects da barra e da part.
	bar_rect = pygame.Rect((bar_x,bar_y), (80,20))
	part_rect = pygame.Rect((part_pos["x"],part_pos["y"]), (20,20))

	# Detectar colisão
	if bar_rect.colliderect(part_rect):
		part_tela = False
		veloc += 0.05
		pontos += 1

	if part_pos["y"] > tela_tam["alt"]:
		part_tela = False
		errou += 1

	# Tempo restante
	relogio_cont = relogio - time.clock() * 10
	
	#pts_fonte = fonte.render("00:"+str(int(relogio_cont)), True, (30,30,30))
	#tela.blit(pts_fonte, (tela_tam["larg"]/2-50,20))	

	pygame.display.flip()

	if errou >= 10:
		break

while True:
	for evt in pygame.event.get():
		# Sair
		if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
			exit()

	pts_fonte = fonte.render("Fim de jogo!", True, (30,30,30))
	tela.blit(pts_fonte, (tela_tam["larg"]/2-50,150))

	pygame.display.flip()