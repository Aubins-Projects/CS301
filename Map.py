import pygame, sys
from pygame.locals import *

def main(level):
	screen_h = 1012
	screen_w = 724

	background_img = "full_map2.png"
	block_img = "block.png"
	blocks = {}

	pygame.init()

	screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
	pygame.display.set_caption("Test")
	background = pygame.image.load(background_img).convert()
	for room in level.rooms:
		blocks[room.name] = pygame.image.load(block_img).convert()
		
		



	while True:
		
		for event in pygame.event.get():
		
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
						
		screen.blit(background, (0, 0))
		for room in level.rooms:
			if not room.visited:
				print room.map_x, room.map_y
				screen.blit(blocks[room.name], (room.map_x, room.map_y))
			
			
		pygame.display.update()
		
class floor:

  def __init__(self,name,rooms=list()):
    self.name=name
    self.rooms=rooms
	
  def __str__(self):
    return str(self.name)



class Room:

  def __init__(self,name,x,y,description="Just a plain wall"):
    self.name=name
    self.north=None
    self.east=None
    self.west=None
    self.south=None
    self.description=description
    self.contents=list()
    self.baddies=None
    self.used=list()
    self.usables=list()
    self.x=x
    self.y=y
    self.map_x = (x-9)*48
    self.map_y = (y-6)*48
    self.visited=False
    self.start_up()
    #self.key=i1
	
  def __str__(self):
    return str(self.name)
	
  def visitedFun(self):
    self.visited=True
	
  def start_up(self):
    level1.rooms.append(self)
    if self.name.lower() in ["hallway","room"]:
      if random.randint(0,5)>3:
        self.baddies=copy.deepcopy(random.choice(MonsterList))
        self.baddies.healthy()
        self.baddies.looter()
		
  def makekey(self,x,y,atloc,world):
    self.key=copy.deepcopy(key)
    self.key.x=x
    self.key.y=y
    self.key.atloc=atloc
    self.key.world=world   
    self.usables.append(self.key)
	
if __name__ == "__main__":
	level1= floor("ground level")
	r1 = Room("room1",10,10)
	r2 = Room("room2",12,12)
	main(level1)