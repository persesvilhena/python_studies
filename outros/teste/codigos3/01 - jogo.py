import os,sys,string
import pygame
from pygame.locals import *

#classe para eventos aleatorios
import random as Random

#funcao que cria o fundo de tela

def create_background():
   #captura a superficie da tela
   screen = pygame.display.get_surface()
   #converte a superficie toda da tela
   back = pygame.Surface(screen.get_size()).convert()
   #pinta toda a superficie com uma cor
   back.fill((0,0,0))
   #retorna o fundo de tela
   return back
   
#funcao que define a tela

def init(size,fullscreen):
   #inicializa o pygame
   pygame.init()
   #acrescenta o buffer duplo aos parametros
   flags = DOUBLEBUF
   #se for definido o modo tela cheia, acrescenta aos parametros
   if fullscreen:
      flags |= FULLSCREEN
   screen = pygame.display.set_mode(size,flags)
   #deixa o mouse invisivel
   pygame.mouse.set_visible(0)
   #define o titulo da tela
   pygame.display.set_caption('PYTHON')

#funcao principal   
   
def main(args):
   #define se quer que exibe em tela cheia
   fullscreen = False
   #define o tamanho da tela (640 X 480)
   screensize = (640,480)
   #inicializa a tela
   init(screensize,fullscreen)
   screen = pygame.display.get_surface()
   screen_size = screen.get_size()
   #cria o plano de fundo
   background = create_background()
   #pre carrega o buffer
   screen.blit(background,(0,0))
   #muda para o buffer pre carregado
   pygame.display.flip()
   #cria um relogio, uma thread de execucao
   clock = pygame.time.Clock()
   dt = 16
   while 1:
      #determina o intervalo do relogio
      clock.tick(1000/dt)
	  #aguarda captura eventos da tela (16 por segundo)
      for event in pygame.event.get():
	     #se for evento de fechar tela, sai
         if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

      screen.blit(background,(0,0))
      pygame.display.flip()
	  
#chamada da funcao principal	  

if __name__ == '__main__':
   main(sys.argv)