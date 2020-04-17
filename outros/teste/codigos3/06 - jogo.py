import os,sys,string
import pygame
from pygame.locals import *
import random

#classe que gera um sprite desenhado na tela

class Block(pygame.sprite.Sprite):
   def __init__(self, color, width, height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface([width, height])
      #preenche o sprite na tela
      self.image.fill((255,255,255))
      #define cor chave para o sprite
      self.image.set_colorkey((255,255,255))
      #desenha uma elipse com a cor definida
      pygame.draw.ellipse(self.image,color,[0,0,width,height])
      self.rect = self.image.get_rect()

#classe que gera um sprite de texto na tela

class TextBlock(pygame.sprite.Sprite):
   def __init__(self, text, color, font_size):
      pygame.sprite.Sprite.__init__(self)
      #define a fonte do texto
      font = pygame.font.Font(None, font_size)
      #renderiza o texto
      text = font.render(text,True,color)
      self.image = text
      self.rect = self.image.get_rect()

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
   #reconfigura as imagens de acordo com o tamanho da tela
   tile = pygame.transform.smoothscale(tile,screen_size)
   #'cola' a imagem sobre a superficie de fundo   
   back.blit(tile,(0,0))
   return back

def create_imagem(image):
   screen = pygame.display.get_surface()
   screen_size = (100,100)
   tile=pygame.image.load(image).convert()
   back = pygame.Surface((100,100)).convert()
   tile = pygame.transform.smoothscale(tile,screen_size)
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

   #imagem = pygame.sprite.RenderPlain()
   imagem = create_imagem(os.path.join('imagens','coelho.png'))
   screen.blit(background,(0,0))
   pygame.display.flip()   


   imagem2 = create_imagem(os.path.join('imagens','arvore.png'))
   screen.blit(background,(0,0))
   pygame.display.flip()  

   interface_objs = pygame.sprite.RenderPlain()
   
   #gera efeito de sombra no texto

   pygame_text_bg = TextBlock('PYTHON', (0,0,0) , 18)
   pygame_text_bg.rect.centerx = screen_size[0]/2+2
   pygame_text_bg.rect.centery = screen_size[1]-10+2

   pygame_text = TextBlock('PYTHON', (255,255,255) , 18)
   pygame_text.rect.centerx = screen_size[0]/2
   pygame_text.rect.centery = screen_size[1]-10

   interface_objs.add(pygame_text_bg)
   interface_objs.add(pygame_text)

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
         #se uma tecla for pressionada, verifica qual tecla foi pressionada
         elif (event.type == KEYDOWN):
            #se a tecla pressionada for ESC, sai
            if (event.key == K_ESCAPE):
               pygame.quit()
               sys.exit(0)

      #Fim do Input Handler
      screen.blit(background,(0,0))
      screen.blit(imagem,(0,0))
      screen.blit(imagem2,(100,100))       

      interface_objs.draw(screen)

      #ao fim do desenho temos que trocar o front buffer e o back buffer
      pygame.display.flip()


if __name__ == '__main__':
   main(sys.argv)
      
   
