
#Import all needed modules 
import pygame, sys
from pygame.locals import *

def main(thingsInBag):
  import copy
  #assign all used images to variables
  bg_image = "bag.png"
  #initialize pygame
  pygame.init()

  #create a game screen
  screen = pygame.display.set_mode((1280,720), 0, 12)
  x=100
  y=200
  TheItemsLoc=dict()
  for item in thingsInBag:
    generic=list()
    key=str(item)
    x+=110
    if x>1000:
      x=210
      y+=110
    TheItemsLoc[key]=[x,y]
  

  #load and convert images for game
  background = pygame.image.load(bg_image)
  background=pygame.transform.smoothscale(background,(1280,720))

  loadedImg=dict()
  for item in thingsInBag:
    key=str(item)
    try:
      value=pygame.image.load(str(item)+".png")
    except:
      value=pygame.image.load("noImg.png")
    value=pygame.transform.smoothscale(value,(100,100))
    loadedImg[key]=value


  try:
    while True:
      for event in pygame.event.get():
        screen.blit(background,(0,0))
        for item in thingsInBag:
          listof=copy.deepcopy(TheItemsLoc[str(item)])
          x=listof[0]
          y=listof[1]
          screen.blit(loadedImg[str(item)],(x,y))
        

        if event.type == QUIT:
          pygame.quit()        
          raise Break()

        elif event.type == KEYDOWN:
          if event.key == K_q:
            pygame.quit()
            raise Break()

        pygame.display.update()
  except:
    pass

