
#Import all needed modules 
import pygame, sys
from pygame.locals import *

def main(thingsInRoom):
  import copy
  #assign all used images to variables
  bg_image = "bg.jpg"
  #initialize pygame
  pygame.init()

  #create a game screen
  screen = pygame.display.set_mode((1280,720), 0, 12)
  if len(thingsInBag)<16:
    scaledsz=150
  else:
    scaledsz=100

  x=100
  y=200

  TheItemsLoc=dict()
  for item in thingsInBag:
    key=str(item)
    x+=scaledsz+10
    if x>1000:
      x=110+scaledsz
      y+=scaledsz+10
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
    value=pygame.transform.smoothscale(value,(scaledsz,scaledsz))
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

