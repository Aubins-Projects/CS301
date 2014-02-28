def main():

  #Import all needed modules 
  import pygame, sys
#  from pygame.locals import *
  import balls, tanks

  #assign all used images to variables
  bg_image = "bag.png"


  #initialize pygame
  pygame.init()

  #create a game screen
  screen = pygame.display.set_mode((1280,720), 0, 32)

  #load and convert images for game
  background = pygame.image.load(bg_image).convert()


  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()        

      if event.type == KEYDOWN:
        if event.key == K_q:
          pygame.quit()
    milli = 0
    while milli < 50:
      milli += clock.tick()
    time += 0.25  
    pygame.display.update()


