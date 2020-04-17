# coding:utf-8
#!/usr/bin/env python
#

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

tela = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

# Prepara as duas barras, a bolinha e o fundo
fundo = pygame.Surface((640,480))
fundo = fundo.convert()
fundo.fill((0,0,0))

bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))

circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
bolinha = circ_sur.convert()

# Define alguns valores iniciais, como posições e velocidade
bar1_x, bar2_x = 10, 620
bar1_y, bar2_y = 215, 215

bolinha_x, bolinha_y = 307.5, 232.5
bar1_movim = bar2_movim = 0
veloc_x = veloc_y = veloc_circ = 5500
bar1_pontos = bar2_pontos = 0
veloc = 0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",40)

while True:
    
    # Captura os eventos do teclado

    for evt in pygame.event.get():
        # Se for pra sair...
        if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
            exit()

        # Se apertar a tecla
        if evt.type == KEYDOWN:
            if evt.key == K_UP:
                bar1_movim = -veloc
            elif evt.key == K_DOWN:
                bar1_movim = veloc

        # Se soltar a tecla
        elif evt.type == KEYUP:
            if evt.key == K_UP:
                bar1_movim = 0
            elif evt.key == K_DOWN:
                bar1_movim = 0
    
    # Prepara a pontuação para ser impressa na tela
    pontos1 = font.render(str(bar1_pontos), True,(255,255,255))
    pontos2 = font.render(str(bar2_pontos), True,(255,255,255))

    # Desenha o fundo
    tela.blit(fundo,(0,0))
    
    # Desenha as bordas
    pygame.draw.rect(tela,(255,255,255),Rect((5,5),(630,470)),2)
    
    #Desenha a linha no meio
    pygame.draw.aaline(tela,(255,255,255),(330,5),(330,475))
    
    # Desenha na tela as barras, a bolinha e as pontuações
    tela.blit(bar1, (bar1_x,bar1_y))
    tela.blit(bar2, (bar2_x,bar2_y))
    tela.blit(bolinha, (bolinha_x,bolinha_y))
    tela.blit(pontos1, (250,210))
    tela.blit(pontos2, (380,210))

    # Move a barra no eixo Y de acordo com o botão pressionado
    bar1_y += bar1_movim
    
    # Movimento da bolinha
    tempo = clock.tick(50)
    tempo_segs = tempo / 1000.0
    
    bolinha_x += veloc_x * tempo_segs
    bolinha_y += veloc_y * tempo_segs
    veloc = veloc_circ * tempo_segs

    # Inteligência artificial
    if bolinha_x >= 305:
        if not bar2_y == bolinha_y + 7.5:
            if bar2_y < bolinha_y + 7.5:
                bar2_y += veloc
            if  bar2_y > bolinha_y - 42.5:
                bar2_y -= veloc
        else:
            bar2_y == bolinha_y + 7.5

    if bolinha_x <= 305:
        if not bar1_y == bolinha_y + 7.5:
            if bar1_y < bolinha_y + 7.5:
                bar1_y += veloc
            if  bar1_y > bolinha_y - 42.5:
                bar1_y -= veloc
        else:
            bar1_y == bolinha_y + 7.5

    # Impede as barras de sairem da tela
    if bar1_y >= 420:
        bar1_y = 420
    elif bar1_y <= 10:
        bar1_y = 10
    if bar2_y >= 420:
        bar2_y = 420
    elif bar2_y <= 10:
        bar2_y = 10

    # Maneira primitiva de checar colisões
    if bolinha_x <= bar1_x + 10:
        if bolinha_y >= bar1_y - 7.5 and bolinha_y <= bar1_y + 42.5:
            bolinha_x = 20
            veloc_x = -veloc_x
    if bolinha_x >= bar2_x - 15:
        if bolinha_y >= bar2_y - 7.5 and bolinha_y <= bar2_y + 42.5:
            bolinha_x = 605
            veloc_x = -veloc_x
    if bolinha_x < 5:
        bar2_pontos += 1
        bolinha_x, bolinha_y = 320, 232.5
        bar1_y,bar_2_y = 215, 215
    elif bolinha_x > 620:
        bar1_pontos += 1
        bolinha_x, bolinha_y = 307.5, 232.5
        bar1_y, bar2_y = 215, 215
    if bolinha_y <= 10:
        veloc_y = -veloc_y
        bolinha_y = 10.
    elif bolinha_y >= 457.5:
        veloc_y = -veloc_y
        bolinha_y = 457.5

    # Atualiza a tela
    pygame.display.flip()