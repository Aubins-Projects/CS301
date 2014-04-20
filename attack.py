
#Import all needed modules 
import pygame, sys
from pygame.locals import *

'''
def attack_command():
  if user.shield!= None:
    yourhealth=(int(user.health) + int(user.shield.power))*int(player["Hmultiplier"])*(user.level+100)/90
  else:
    yourhealth=(int(user.health))*int(player["Hmultiplier"])*(user.level+100)/90
  if user.weapon!= None:
    yourdamage=(int(user.weapon.power)+user.damage)*int(player["Dmultiplier"])*(user.level+100)/90
  else:
    yourdamage=(user.damage)*int(player["Dmultiplier"])*(user.level+100)/90
  monsterdamage=int(location.baddies.damage)
  monsterhealth=int(location.baddies.health)
  while neitherdead==0:
    monsterhealth=monsterhealth-yourdamage
    if user.weapon!= None: 
      print("you just attacked "+str(location.baddies.name) +" with: "+ str(user.weapon.name))
    else:
      print("you just attacked "+str(location.baddies.name) +" with: your mighty fists")
    if monsterhealth<1:
      print("you have just killed "+str(location.baddies.name))
      
      player["points"]=player["points"]+int(location.baddies.health)
      level_upper(int(location.baddies.health),int(location.baddies.damage))
      print("you have found :")
      for item in location.baddies.contents:
        if item==None:
          break
        
        print("a(n) "+str(item))
        print("\tDescription: "+str(item.description)+"\n")
        user.contents.append(item)
      location.baddies=None
      break
    yourhealth=yourhealth-monsterdamage
    print(str(location.baddies.name)+" just attacked you for: "+str(monsterdamage))
    if yourhealth<1:
      print("you have just been killed by "+str(location.baddies.name))
      player["lives"]=player["lives"]-1
      if player["lives"]<0:
        response="dfhsergghj"
        break
      print("you only have: "+str(player["lives"])+" lives/life left")
      break
    print("Your HP: "+str(int(yourhealth)))
    print(str(location.baddies.name)+"'s HP " +str(int(monsterhealth)))



'''


def main(thingsInBag):
  import copy
  #assign all used images to variables
  bg_image = "bag.png"
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

