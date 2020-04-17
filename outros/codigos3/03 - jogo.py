import os,sys,string
import pygame
from pygame.locals import *

#classe para eventos aleatorios
import random as Random

#funcao que cria o fundo de tela

def create_background(image):
   #captura a superficie da tela
   screen = pygame.display.get_surface()
   #captura as dimensoes da tela
   screen_size = screen.get_size()
   #converte a imagem
   tile=pygame.image.load(image).convert()
   #converte o plano de fundo em superficie
   back = pygame.Surface(screen.get_size()).convert()   
   #'cola' a imagem sobre a superficie de fundo
   back.blit(tile,(0,0))
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

def main(args):
   #captura o caminho completo do arquivo
   fullpath = os.path.abspath(args[0])
   #extrai o diretorio onde se encontra o arquivo
   dir = os.path.split(fullpath)[0]
   #forca a modificacao do diretorio
   os.chdir(dir)
   #verifica se definiu tela cheia
   fullscreen = '-fullscreen' in args
   screensize = (640,480)
   #define nova resolucao se for definida por parametro
   for arg in args:
      if arg[:5] == '-res=':
         screensize = [int(x) for x in string.split(arg[5:],',')]
   #inicializa a tela		 
   init(screensize,fullscreen)
   screen = pygame.display.get_surface()
   screen_size = screen.get_size()
   #cria o plano de fundo com imagem
   background = create_background(os.path.join('imagens','beach.png'))   
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

      #pre carrega o buffer			
      screen.blit(background,(0,0))
      #muda para o buffer pre carregado	  
      pygame.display.flip()
	  
#chamada da funcao principal	  

if __name__ == '__main__':
   main(sys.argv)