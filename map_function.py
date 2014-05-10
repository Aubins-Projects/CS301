import pygame, sys
from pygame.locals import *

def display(level, curr_x, curr_y):
  screen_h = 1012
  screen_w = 724

  background_img = "full_map2.png"
  block_img = "block.png"
  curr_room_img = "curr_room.png"
  blocks = {}

  pygame.init()
  running=True
  screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
  pygame.display.set_caption("MAP")
  background = pygame.image.load(background_img).convert()
  curr_room = pygame.image.load(curr_room_img).convert()
  curr_room.set_colorkey((255,255,255), RLEACCEL)
  for room in level.rooms:
    blocks[room.name] = pygame.image.load(block_img).convert()

  

  try:
    while running==True:
      
      for event in pygame.event.get():
        
        if event.type == QUIT:
          pygame.quit()
          return
          
        elif event.type == KEYDOWN:
          if event.key == K_q:
            pygame.quit()
            return
              
      screen.blit(background, (0, 0))
      for room in level.rooms:
        if not room.visited:
          screen.blit(blocks[room.name], (room.map_x, room.map_y))
        
      screen.blit(curr_room, (curr_x - 1 , curr_y - 1))
      
      pygame.display.update()
  except:
    pygame.quit()
    return
