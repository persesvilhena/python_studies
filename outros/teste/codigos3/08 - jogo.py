import os,sys,string
import pygame
from pygame.locals import *
import random

class Block(pygame.sprite.Sprite):
   __speed = 30.0
   
   def __init__(self, color, width, height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface([width, height])
      self.image.fill((255,255,255))
      self.image.set_colorkey((255,255,255))
      pygame.draw.ellipse(self.image,color,[0,0,width,height])
      self.rect = self.image.get_rect()
   def update(self,dt):
      self.rect = self.rect.move((0,max(self.__speed*dt,1)))

      screen = pygame.display.get_surface()
      screen_size = screen.get_size()
      if (self.rect.top > screen_size[1]):
          self.kill()

class ImageBlock(pygame.sprite.Sprite):
   max_speed = 120.0
   __speed = 30.0
   
   def __init__( self, imagefile, width, height ):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(imagefile)
      self.image = pygame.transform.smoothscale(self.image,(width,height))
      self.rect = self.image.get_rect()
      self.speed = [0.0,0.0]

   def update(self,dt):
      self.rect = self.rect.move((self.speed[0]*dt,self.speed[1]*dt))
   #def update(self,dt):
    #  self.rect = self.rect.move((0,max(self.__speed*dt,1)))

      screen = pygame.display.get_surface()
      screen_size = screen.get_size()

      #fazer a imagem subir e descer
      if(self.rect.bottom > screen_size[1]):
         self.rect.bottom = 30
         #self.speed[1] = -1 * abs(self.speed[1])
      elif (self.rect.top < 0):
         self.speed[1] = abs(self.speed[1])
      
      if (self.rect.top > screen_size[1]):
          self.kill()
      if (self.rect.left > screen_size[0]):
          self.kill()          

   def move( self, x, y ):
      #print self.rect.left
      #if(self.rect.left>=0)and(self.rect.left<=500):
      #   self.rect.move_ip( x, y )
      #else:
      #   self.rect.move_ip( -x, y )      
      #self.update(1);
      self.rect.move_ip(x,y)
      screen_size = pygame.display.get_surface().get_size()
      if(self.rect.left < 0):
         self.rect.left = 0
      elif (self.rect.right > screen_size[0]):
         self.rect.right = screen_size[0]

class TextBlock(pygame.sprite.Sprite):
   def __init__(self, text, color, font_size):
      pygame.sprite.Sprite.__init__(self)
      font = pygame.font.Font(None, font_size)
      text = font.render(text,True,color)
      self.image = text
      self.rect = self.image.get_rect()

#pygame.init()

#screen_width=700
#screen_height=400

#screen=pygame.display.set_mode([screen_width,screen_height])



def create_background(image):
   screen = pygame.display.get_surface()
   screen_size = screen.get_size()
   tile=pygame.image.load(image).convert()
   back = pygame.Surface(screen.get_size()).convert()
   tile = pygame.transform.smoothscale(tile,screen_size)
   back.blit(tile,(0,0))
   return back

#def create_imagem(image):
   #screen = pygame.display.get_surface()
   #screen = pygame.sprite.add(image)
   #screen_size = (100,100)
   #tile=pygame.image.load(image).convert()
   #back = pygame.Surface((100,100)).convert()
   #tile = pygame.transform.smoothscale(tile,screen_size)
   #back.blit(tile,(0,0))
   #return back

def init(size,fullscreen):
   pygame.init()
   flags = DOUBLEBUF
   screen = pygame.display.set_mode(size,flags)
   pygame.mouse.set_visible(0)
   pygame.display.set_caption('PYTHON')

def main(args):
   fullpath = os.path.abspath(args[0])
   dir = os.path.split(fullpath)[0]
   os.chdir(dir)
   fullscreen = '-fullscreen' in args
   screensize = (640,480)
   for arg in args:
      if arg[:5] == '-res=':
         screensize = [int(x) for x in string.split(arg[5:],',')]
   init(screensize,fullscreen)


   #surface - bitmap -> blit
   #sprite -    -> draw
   screen = pygame.display.get_surface()
   screen_size = screen.get_size()

   background = create_background(os.path.join('imagens','beach.png'))
   screen.blit(background,(0,0))
   pygame.display.flip()

   interface_objs = pygame.sprite.LayeredUpdates()

   pygame_text_bg = TextBlock('PYTHON', (0,0,0) , 18)
   pygame_text_bg.rect.centerx = screen_size[0]/2+2
   pygame_text_bg.rect.centery = screen_size[1]-10+2
   pygame_text_bg.layer = 1
   

   pygame_text = TextBlock('PYTHON', (255,255,255) , 18)
   pygame_text.rect.centerx = screen_size[0]/2
   pygame_text.rect.centery = screen_size[1]-10
   pygame_text.layer = 0

   interface_objs.add(pygame_text_bg)
   interface_objs.add(pygame_text)

   block_list = pygame.sprite.LayeredUpdates()
   block_list2 = pygame.sprite.LayeredUpdates()

   block2 = ImageBlock(os.path.join('imagens','rabbit.png'),30, 30)
   block_list2.add(block2)    

   for i in range(3):
      block = Block((0,0,0), 20, 15)
      block.rect.x = random.randrange(screen_size[0])
      block.rect.y = random.randrange(screen_size[1])
      block_list.add(block)

     

   clock = pygame.time.Clock()
   dt = 16

   key = { K_LEFT: False, K_RIGHT: False }
   deslocamento = 10.0;
   block2.speed[1] = block2.max_speed
   
   
   while 1:
      ellapsed = clock.tick(1000/dt)

      for event in pygame.event.get([QUIT]):
         pygame.quit()
         sys.exit(0)
      #elif (event.type == KEYDOWN):
      
      for event in pygame.event.get([KEYDOWN,KEYUP]):
         valor = (event.type == KEYDOWN)

         if (event.key == K_ESCAPE):
            pygame.quit()
            sys.exit(0)
         elif (event.key in key.keys()):
            key[event.key]=valor
            #   block_list2.get_sprite(0).image.x+=10
      if key[ K_LEFT ]:
         block_list2.get_sprite(0).move( -deslocamento,   0 )
      if key[ K_RIGHT ]:
         block2.move(  deslocamento,   0 )
      #update objects
      #block_list.update(ellapsed/1000.0)
      block_list2.update(ellapsed/1000.0)      
      interface_objs.update(ellapsed/1000.0)



      collided_list = pygame.sprite.spritecollide(block2, block_list, False)
      if(len(collided_list)>0):
         block2.kill()
         block2 = ImageBlock(os.path.join('imagens','rabbit.png'),30, 30)
         block2.speed[1] = block2.max_speed
         block_list2.add(block2)
      

      #Fim do Input Handler
      screen.blit(background,(0,0))

      block_list.draw(screen)
      block_list2.draw(screen)      
      interface_objs.draw(screen)

      #ao fim do desenho temos que trocar o front buffer e o back buffer
      pygame.display.flip()


if __name__ == '__main__':
   main(sys.argv)
      
   
