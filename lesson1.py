from pygame import *
 
#parent class for other classes
class GameSprite(sprite.Sprite):
 # constructor of the class
 def __init__(self, player_image, player_x, player_y, size_x, size_y):
     # Callig for the constructor of the class (Sprite):
     sprite.Sprite.__init__(self)
     # each sprite needs to have image 
     self.image = transform.scale(image.load(player_image), (size_x, size_y))
 
     # each sprite must store the property rect - the rectangle in which it is inscribed
     self.rect = self.image.get_rect()
     self.rect.x = player_x
     self.rect.y = player_y
 # method that draws the hero on the window
 def reset(self):
     window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Player(GameSprite):
 #a method that implements sprite control by keyboard arrow buttons
 def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
     # Callig for the constructor of the class (Sprite):
     GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
 
     self.x_speed = player_x_speed
     self.y_speed = player_y_speed
 def update(self):
      ''' moves the character using the current horizontal and vertical speed'''
      # first move horizontally
      self.rect.x += self.x_speed
      self.rect.y += self.y_speed
 
#Creating window
win_width = 700
win_height = 500
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#set the color according to the RGB color scheme
 
#create wall pictures
w1 = GameSprite('platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('platform2_v.png', 370, 100, 50, 400)
 
#Creating sprites
packman = Player('hero.png', 5, win_height - 80, 80, 80, 0, 0)
 
#game loop
run = True
while run:
 #loop runs every 0.05 seconds
 time.delay(50)
 window.fill(back)#color the window
 
 for e in event.get():
      if e.type == QUIT:
          run = False
      elif e.type == KEYDOWN:
          if e.key == K_LEFT:
              packman.x_speed = -5
          elif e.key == K_RIGHT:
              packman.x_speed = 5
          elif e.key == K_UP:
              packman.y_speed = -5
          elif e.key == K_DOWN:
              packman.y_speed = 5
      elif e.type == KEYUP:
          if e.key == K_LEFT:
              packman.x_speed = 0
          elif e.key == K_RIGHT:
              packman.x_speed = 0
          elif e.key == K_UP:
              packman.y_speed = 0
          elif e.key == K_DOWN:
              packman.y_speed = 0
 #draw objects
#  w1.reset()
#  w2.reset()
 packman.reset()
 
 #turn on the movement
 packman.update()
 
 display.update()
