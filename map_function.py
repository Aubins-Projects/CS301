import pygame, sys
from pygame.locals import *

def display(level):
  screen_h = 1012
  screen_w = 724

  background_img = "full_map2.png"
  block_img = "block.png"
  blocks = {}

  pygame.init()
  running=True
  screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
  pygame.display.set_caption("MAP")
  background = pygame.image.load(background_img).convert()
  for room in level.rooms:
    blocks[room.name] = pygame.image.load(block_img).convert()

  

  try:
    while running==True:
      
      for event in pygame.event.get():
        
        if event.type == QUIT:
          pygame.quit()
          running=False
          break
          
        elif event.type == KEYDOWN:
          if event.key == K_q:
            pygame.quit()
            running=False
            break
              
      screen.blit(background, (0, 0))
      for room in level.rooms:
        if not room.visited:
          screen.blit(blocks[room.name], (room.map_x, room.map_y))
        
        
      pygame.display.update()
  except:
    pygame.quit()
