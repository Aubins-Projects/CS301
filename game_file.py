import os.path
import string
import random


'''
How you can make this your own game:

DO NOT MESS WITH THE FUNCTIONS other than location
DO NOT MESS WITH THE CLASSES

you can add objects by just following the format. If it is a shield/weapon, make sure you say so in the equip spot

you can add monsters by following the format, just make sure you say where it is from by putting the [room].baddies

you can add a room by adding the rooms to the room object and the floor object

New idea make common, uncommon, good, and rare items that are based off a pool and the enemies can have on
them by chance and randomness

so basically three classes more :D

'''
#these are the global variables for the system


points=0
lives=3
relive=1
contents={}
response=""
holder=list
HnDmultiplier=[1,1]
HnDmultiplier[0]=1
HnDmultiplier[1]=1


#This is what lets you put your name in and then checks your score
def namechecker():
  name=raw_input("Enter your name please \n")
  if name in ('Aubin','aubin'):
    print("Welcome your highness")
  elif name in ('K','k', 'carolina', 'Carolina'):
    print("Oh...its you, well you can still play me I guess...")
    name="Smelly"
  else:
    print("Welcome: "+name +"\nGood Luck! \n")
  return name


#this is to initialize your character its commented out below for testing purposes
def initial(name, HnDmultiplier):
  while True:
    answer2=raw_input("What is your class (warrior or fighter)? \n")
    if answer2 in ("warrior","fighter"):
      break
  answer3=100
  user=player(name,answer3,answer2)
  print("\n")
  print("Your name: "+str(user.name))
  print("Your class: "+str(user.classs))
  HnDmultiplier=class_adaption(user.classs,HnDmultiplier)
  print("Your health: "+str(int(user.health)*HnDmultiplier[0]))
  print("Your damage: "+str(int(user.damage)*HnDmultiplier[1]))
  return user

def class_adaption(classs,HnDmultiplier):
  if classs=="warrior":
    HnDmultiplier[0]=2
    HnDmultiplier[1]=1
  if classs=="fighter":
    HnDmultiplier[0]=1
    HnDmultiplier[1]=2
  return HnDmultiplier


#This is for looking specifically at one thing
def look(what):
  print(what.description)


#This if for looking at the entire room
def room_contents_look(what):
  print("************************** \n")
  i=0
  for x in range(len(what.contents)):
    print(what.contents[i].name)
    i=1+i
  if what.east== None:
    i=0
  else:
    print(str(what.east)+" is East")
  if what.north== None:
    i=0
  else:
    print(str(what.north)+" is North")
  if what.west== None:
    i=0
  else:
    print(str(what.west)+" is West")
  if what.south== None:
    i=0
  else:
    print(str(what.south)+" is South")
    print("************************** \n")


#This is the reassurance for trying to quit
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
  while True:
    global relive
    ok = raw_input( prompt + '\n')
    if ok in ('y', 'ye', 'yes'):
      print("you are alive once more!")
      relive=1
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      print("You chose to be a quitter")
      logfile = open("Highscores.txt", "a")
      logfile.write(str(points)+"\t" + name+"\n")
      logfile.close()
      relive=0
      return False
    retries = retries - 1
    if retries < 0:
      print('You cannot follow instructions')
      return False
    print(complaint)

#This is part of the reassurance from above
def infunc(what_you_want_asked):
  tobeused=raw_input(what_you_want_asked)
  if not ask_ok(tobeused):
    return False
  else:
    return True

def item_randomer(thelist):
  randomnum=random.randrange(1,len(thelist.items))
  for item in thelist.items:
    if randomnum == item.uid:
      return item
      break    
def loot_size_randomer(monster,thelist):
  randonum=random.randrange(2,4)
  for num in range(0,randonum):
      monster.contents.append(item_randomer(thelist))
      
    
#This is so you can check your score with the text file
def scorecheck():
  i=0
  logfile = open("Highscores.txt", "r")
  data=logfile.readlines()
  data.sort(key=lambda l: float(l.split("\t")[0]),reverse=True)
  logfile.close()
  logfile = open("Highscores.txt", "w")
  for x in range(len(data)):
    logfile.write(data[i])
    i=i+1
  logfile.close()
  logfile = open("Highscores.txt", "r")
  print("************************** \n")
  print("The Top Scores so far are: \n")
  for x in range(0,3):
    print(logfile.readline())
  logfile.close()
  print("************************** \n")
  print("The your score is: "+ str(points))
  
#These are generic deaths
def crzy_death(how_they_died):
  crazy_death= (name + ", because you decided to "+ how_they_died +" you have incured the wrath of Om' Alde Ashko and he has smited your SOUL!")
  return str(crazy_death)

def gen_death(how_they_died):
  gen_death= (name + ", because you decided to "+ how_they_died +" you have incured the wrath of Om' Alde Ashko and he has smited your SOUL!")
  return str(gen_death)


#this is your starting coordinates
    
x=10
y=10

def coordinates(direction):
  global x
  global y
  global location
  sav_x=x
  sav_y=y
  if direction in ["east" , "e"]:
     x=x+1
  elif direction in ["west" , "w"]:
     x=x-1
  elif direction in ["north" , "n"]:
     y=y+1
  elif direction in ["south" , "s"]:
     y=y-1
  loc_finder(sav_x,sav_y)

###########################################################################################
#This is the automatic mapper once you add the grids in the room OBJECT and the floor OBJECT


def loc_finder(sav_x,sav_y):
  global x
  global y
  global location
  check =0
  for room in level1.rooms:
    if room.x==x and room.y==y:
      location= room
      check=1
  if check == 0:
      x=sav_x
      y=sav_y
  print(str(name)+", you are in the "+str(location))

def map_finder(x,y):
  for room in level1.rooms:
    if room.x==x and room.y==y:
      return room

def mapping():
  global x
  global y
  global location
  temp_location=location
  temp_x=x
  temp_y=y

  if not map_finder(temp_x-1,temp_y)==temp_location:
    location.west=map_finder(temp_x-1,temp_y)

  if not map_finder(temp_x+1,temp_y)==temp_location:
    location.east=map_finder(temp_x+1,temp_y)

  if not map_finder(temp_x,temp_y-1)==temp_location:
    location.south=map_finder(temp_x,temp_y-1)

  if not map_finder(temp_x,temp_y+1)==temp_location:
    location.north=map_finder(temp_x,temp_y+1)
  
###############################################################################################################    

#look command function
def look_command(holder):
  if holder[0] in ["look", "l"]:
    if holder[1] in ["east","e"]:
      print(location.east)
    elif holder[1] in ["west", "w"]:
      print(location.west)
    elif holder[1] in ["south","s"]:
      print(location.south)
    elif holder[1] in ["north", "n"]:
      print(location.north)
    elif holder[1]in ["around", "a"]:
      print ("this place: "+location.description)
      room_contents_look(location)
      if location.baddies:
        print("Monster name: "+str(location.baddies.name))
        print("Monster health: "+str(location.baddies.health))
        print("Monster damage: "+str(location.baddies.damage))


def level_upper(monsterh,monsterd):
  global user
  totalpoints=monsterh+monsterd
  print (str(int(monsterh)))
  print (str(int(monsterd)))
  totalexp=totalpoints
  user.exp+=totalexp
  while user.exp > 500:
    user.exp-=500
    user.level+=1
    user.exp=user.exp*(100-user.level)/150
    print("*******************")
    print("you just leveled up to: "+str(user.level))
    print("*******************")



def about_command(holder):
  if holder[0]=="about":
    import game
    try:
      game.main()
    except:
      fakevarforpuprose=1
    if location.baddies:
      if holder[1]==location.baddies.name:
        print("Monster name: "+str(location.baddies.name))
        print("Monster health: "+str(location.baddies.health))
        print("Monster damage: "+str(location.baddies.damage))
    holder.remove("about")
    otherholder=' '.join(holder) 
    if otherholder in user.contents:
      print("in my bag")
      print(user.contents[user.contents.index(otherholder)].description)
    if otherholder in location.contents:
      print("in this room")
      print(location.contents[location.contents.index(otherholder)].description) 
      
def grab_command(holder):
  if holder[0]=="grab":
    holder.remove("grab")
    otherholder=' '.join(holder) 
    if otherholder in location.contents:
      user.contents.append(location.contents[location.contents.index(otherholder)])
      location.contents.remove(otherholder)
      print(user.contents[user.contents.index(otherholder)].description)

def unlocked_rooms(item,loc):
  loc.x=item.x
  loc.y=item.y

def equip_command(holder):
  if holder[0]in ["equip","e"]:
    temp_word_holder=str(holder[0])
    holder.remove(temp_word_holder)
    otherholder=' '.join(holder)     
    if otherholder in user.contents:
      if user.contents[user.contents.index(otherholder)].equip == "shield":
        user.shield = user.contents[user.contents.index(otherholder)]
        user.contents.remove(otherholder)
        print("you just equipped a(n) "+str(otherholder)+" which "+str(user.shield.description))
      elif user.contents[user.contents.index(otherholder)].equip == "weapon":
        user.weapon = user.contents[user.contents.index(otherholder)]
        user.contents.remove(otherholder)
        print("you just equipped a(n) "+str(otherholder)+" which "+str(user.shield.description))

def unequip_command(holder):
  if holder[0] in ["unequip", "un"]:
    temp_word_holder=str(holder[0])
    holder.remove(temp_word_holder)
    otherholder=' '.join(holder)     
    if otherholder == user.weapon:
        user.contents.append(user.weapon)
        user.weapon=""
        print("you just took off a(n) "+str(otherholder))
    elif otherholder == user.shield:
        user.contents.append(user.shield)
        user.shield=""
        print("you just took off a(n) "+str(otherholder))

        
      
def bag_command(holder):
  if holder[0]=="bag":
    i=0
    print("************************** \n You currently have in your bag:")
    for x in range(len(user.contents)):
      print("a(n) "+str(user.contents[i]))
      i=i+1
    print("************************** \n You currently have equipped:")
    print("a(n) "+str(user.shield)+" as your shield")
    print("a(n) "+str(user.weapon)+" as your weapon")

def drop_command(holder):
  if holder[0]in ["drop","d"]:
    temp_word_holder=str(holder[0])
    holder.remove(temp_word_holder)
    otherholder=' '.join(holder)
    if otherholder in user.contents:
      location.contents.append(user.contents[user.contents.index(otherholder)])
      user.contents.remove(otherholder)
      print("you just dropped "+ otherholder + " in the " +str(location))

def use_command(holder):
  if holder[0]in ["use","u"]:
    temp_word_holder=str(holder[0])
    holder.remove(temp_word_holder)
    otherholder=' '.join(holder)
    if (otherholder in user.contents):
      if (user.contents[user.contents.index(otherholder)].usable=="yes"):
        location.used.append(user.contents[user.contents.index(otherholder)])
        print("you just used "+ otherholder + " in the " +str(location))
        if otherholder in location.usables:
         cause_and_effect(otherholder)
      else:
        print(str(user.contents[user.contents.index(otherholder)])+" is not usable.")


def cause_and_effect(otherholder):
  global location
  print(location.usables[location.usables.index(otherholder)].effect)
  if (len(location.usables[location.usables.index(otherholder)].changer)>0):
    for item in location.usables[location.usables.index(otherholder)].changer:
      location.contents.append(item)
      location.usables[location.usables.index(otherholder)].changer.remove(item)
  if (user.contents[user.contents.index(otherholder)].world=="yes"):
    unlocked_rooms(user.contents[user.contents.index(otherholder)],user.contents[user.contents.index(otherholder)].atloc)
    if (user.contents[user.contents.index(otherholder)].destroy=="yes"):
        user.contents.remove(otherholder)


def help_command(holder):
  if holder[0]=="help":
    if len(holder)>1:
      holder.remove("help")
      otherholder=' '.join(holder)
      if otherholder in commandlist:
        for command, description in commandlist[otherholder]:
          print(command + "\t - \t" + description)
    else: 
      for command, description in commandlist.items():
        print(command + "\t - \t" + description)

      
def attack_command(holder):
  global response
  global lives
  global points
  if holder[0]=="attack":
    holder.remove("attack")
    otherholder=' '.join(holder)
    neitherdead=0
    if otherholder == location.baddies:
      yourhealth=(int(user.health) + int(user.shield.power))*int(HnDmultiplier[0])*(user.level+100)/90
      yourdamage=(int(user.weapon.power)+user.damage)*int(HnDmultiplier[1])*(user.level+100)/90
      monsterdamage=int(location.baddies.damage)
      monsterhealth=int(location.baddies.health)
    while neitherdead==0:
      monsterhealth=monsterhealth-yourdamage
      print("you just attacked "+str(location.baddies.name) +" with: "+ str(user.weapon.name))
      if monsterhealth<1:
        print("you have just killed "+str(location.baddies.name))
        print("you have found :")
        points=points+int(location.baddies.health)
        level_upper(int(location.baddies.health),int(location.baddies.damage))   
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
        lives=lives-1
        if lives<0:
          response="dfhsergghj"
          break
        print("you only have: "+str(lives)+" lives/life left")
        break
      print("Your HP: "+str(int(yourhealth)))
      print(str(location.baddies.name)+"'s HP " +str(int(monsterhealth)))
      
    
#This holds ALL the functions that you could run    
def what_you_do(holder):
  global location
  if holder[0]=="go":
    coordinates(holder[1])
  use_command(holder)
  unequip_command(holder)
  drop_command(holder)  
  equip_command(holder)
  grab_command(holder)
  bag_command(holder)
  look_command(holder)
  about_command(holder)
  help_command(holder)
  attack_command(holder)
  if holder[0]=="points":
    scorecheck()


#Your items found in game
class Object:
  def __init__(self, name, value, description, power,uid, equip="item",atloc='',usable="no",world="no",destroy="no"):
    self.name=name
    self.value=value
    self.description=description
    self.power=power
    self.equip=equip
    self.uid=int(uid)
    self.usable=usable
    self.world=world
    self.x=x
    self.y=y
    self.atloc=atloc
    self.destroy=destroy

  def __str__(self):
    return str(self.name)

  def __eq__(self,other):
    return self.name == other
###################################################################################################################

#############################################################################################################

class itemlist:
  def __init__(self,name,items=list()):
    self.name=name
    self.items=items
  def __str__(self):
    return str(self.name)

############################################################################################################
#world ITEMS

crown = Object("crown", 15000, "a gold crown with many jewels",10,1)
crown.usable="yes"
scepter =Object("King's scepter", 10000, "a silver sceptre",30,2)
vorpel_sword=Object("vorpel sword", 200, "a strange looking sword",1000,3)
kbedpan=Object("bedpan", 3, "a smelly metal bowl",2,4)
kbedpan.usable="yes"
bedpan=Object("bedpan", 3, "a smelly metal bowl",2,4)
torch=Object("torch", 1, "fire attatched to a stick",78,5)
torch.usable="yes"
shield=Object("shield",200,"will mitigate some damage",300,6)
broken_shield=Object("broken shield",100,"will mitigate some damage",300,8, "shield")
broken_weapon=Object("broken weapon",100,"will cause some damage",300,9, "weapon")
perfect_w=Object("water tower",10000,"will mitigate some damage",30000,10, "weapon")
perfect_s=Object("best shield",10000,"will mitigate some damage",30000,11, "shield")
skull=Object("skull", 15000, "a giant skull",100,12)
talon=Object("talon", 1500, "a giant talon",100,13)
lint=Object("lint", 100, "a piece of lint",100,14)
key=Object("key",1200,"this might be useful for doing key things",12,15)
key.usable="yes"
key.destroy="yes"
blooddiamond=Object("Blood Diamond",150000,"a blood diamond, formed from vast amounts of blood and a fiery explosion", 20,1)

##################################################################################################################    
    
    
    
    
    
############################################################################################################
uncommon=itemlist("uncommon")
#UNCOMMON ITEMS

uncommon.items.append(crown)
uncommon.items.append(scepter)
uncommon.items.append(vorpel_sword)
uncommon.items.append(bedpan)
uncommon.items.append(torch)
uncommon.items.append(Object("shield",200,"will mitigate some damage",300,6))
uncommon.items.append(Object("broken shield",100,"will mitigate some damage",300,8, "shield"))
uncommon.items.append(Object("broken weapon",100,"will cause some damage",300,9, "weapon"))
uncommon.items.append(Object("water tower",10000,"will mitigate some damage",30000,10, "weapon"))
uncommon.items.append(Object("best shield",10000,"will mitigate some damage",30000,11, "shield"))
uncommon.items.append(Object("skull", 15000, "a giant blob skull",100,12))
uncommon.items.append(Object("talon", 1500, "a giant dragon talon",100,13))
uncommon.items.append(Object("lint", 100, "a piece of lint",100,14))





##################################################################################################################


#COMMON ITEMS

common= itemlist("common")
common.items.append(Object("scrap metal", 150, "a gold crown with many jewels",10,1))
common.items.append(Object("dead mouse", 100, "a silver sceptre",30,2))
common.items.append(Object("plate", 20, "a strange looking sword",1000,3))
common.items.append(Object("juice box", 3, "a smelly metal bowl",2,4))
common.items.append(Object("credit card", 1, "fire attached to a stick",78,5))
common.items.append(Object("old movie",20,"will mitigate some damage",300,6))
common.items.append(Object("paper shield",10,"will mitigate some damage",300,7, "shield"))
common.items.append(Object("paper weapon",10,"will cause some damage",300,8, "weapon"))
common.items.append(Object("skull", 15, "a giant blob skull",100,9))
common.items.append(Object("talon", 15, "a giant dragon talon",100,10))
common.items.append(lint)



#############################################################################################################


#This a player/your player called the user in the code  
class player:
  def __init__(self,name,health,classs,exp=0,level=1):
    self.name=name
    self.health=health
    self.classs=classs
    self.exp=exp
    self.contents=list()
    self.damage=10 
    self.shield=""
    self.weapon=""
    self.level=level
  def __str__(self):
    return str(self.name)
#####################################################################################################################
#add players here
#uncomment namechecker and initial




name=namechecker()
user=initial(name,HnDmultiplier)







#####################################################################################################################

#These are the monsters in game
class monster:
  def __init__(self,name,health,color,classs):
    self.name=name
    self.health=health
    self.color=color
    self.classs=classs
    self.damage=10
    self.contents=list()
    self.keys="" 
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other


######################################################################################################################
#Add monsters below

blob=monster("blob",10000,"yellow","warrior" )
blob.damage=10
loot_size_randomer(blob,common)

dragon=monster("dragon",1000,"yellow","warrior" )
dragon.damage=10
loot_size_randomer(dragon,common)

high_wizard=monster("high wizard",random.randrange(1000,2000),"black","warrior")
high_wizard.damage=random.randrange(100,200)
loot_size_randomer(high_wizard,common)

######################################################################################################################

class cause_n_effect:
  def __init__(self,name,effect,uses=''):
    self.name=name
    self.effect=effect
    self.changer=list()
    self.uses=uses
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other


#the name part is your trigger, so in this case it is the crown, if you use the crown in the bedroom you will see this effect
crown_explosion= cause_n_effect("crown", "you dawn the crown of a dead king!\n The walls begin to BLEEEEDDDDDDD! Why would you do such a thing!")
bedpan_massacre= cause_n_effect("bedpan","you just spilled feces all over the place...you are a disgusting man, but a key dropped")
bedpan_massacre.changer.append(key)
key_use = cause_n_effect("key", "a door slides open and behind it is a CAVE! Nice find "+str(name)+"!")
fire_spolde= cause_n_effect("torch", "The prison bursts in flames, revealing a hidden gem! Nice find "+str(name)+"!")
fire_spolde.changer.append(blooddiamond)


#Your room object
class Room:
  def __init__(self,name,north="wall",east="wall",west="wall",south="wall",description="Just a plain wall"):
    self.name=name
    self.north=north
    self.east=east
    self.west=west
    self.south=south
    self.description=description
    self.contents=list()
    self.baddies=None
    self.used=list()
    self.usables=list()
    self.x=0
    self.y=0
  def __str__(self):
    return str(self.name)
############################################################################################################
#Add rooms Below don't forget them to the



bedroom = Room("King\'s bedroom")
bedroom.description="This is a room fit for a King"
bedroom.contents.append(crown)
bedroom.contents.append(scepter)
bedroom.contents.append(vorpel_sword)
bedroom.contents.append(kbedpan)
bedroom.contents.append(broken_shield)
bedroom.contents.append(broken_weapon)
bedroom.usables.append(crown_explosion)
bedroom.usables.append(bedpan_massacre)
bedroom.x=10
bedroom.y=10

hallway=Room("corridor")
hallway.description="just a long hallway"
hallway.contents.append(torch)
hallway.x=11
hallway.y=10

lair=Room("lair")
lair.description="just a long hallway, but wait is that a key hole?"
lair.contents.append(torch)
lair.baddies=blob
lair.usables.append(key_use)
lair.x=11
lair.y=9

keep=Room("keep")
keep.description="Large room, could probably hold a dragon"
keep.baddies=dragon
keep.x=11
keep.y=8

cave=Room("cave")
cave.description="a bad aura lingers here"
cave.baddies=high_wizard
cave.contents.append(torch)
cave.contents.append(perfect_w)
cave.contents.append(perfect_s)
cave.x=150000
cave.y=900000
key.world="yes"
key.x=12
key.y=9
key.atloc=cave


prison=Room("prison")
prison.description="the stench of blood is thick here, but where did it all go. Is that oil?"
prison.contents.append(torch)
prison.contents.append(lint)
prison.usables.append(fire_spolde)
prison.x=13
prison.y=9








class floor:
  def __init__(self,name,rooms=list()):
    self.name=name
    self.rooms=rooms
  def __str__(self):
    return str(self.name)

############################################################################################################
level1= floor("ground level")
level1.rooms.append(lair)
level1.rooms.append(bedroom)
level1.rooms.append(hallway)
level1.rooms.append(keep)
level1.rooms.append(cave)
level1.rooms.append(prison)



#These are all of the commands in the game
commandlist = dict()

commandlist['points']="type points to get your current points"
commandlist['go']="type go and then a cardinal direction"
commandlist['look']="type look and then a cardinal direction, or around to look around"
commandlist['quit']="type quit and then follow the directions to quit"
commandlist['about']="type about [item] and then what object you want to learn about"
commandlist['bag']="type bag to see whats in your bag"
commandlist['drop']="type drop [item] to drop the item from you bag"
commandlist['equip']="type equip [item] to equip whats in your bag"
commandlist['unequip']="type unequip [item] to take off what you are wearing"
commandlist['help']="type help [command] learn about command"
commandlist['attack']="type attack [monster] to attack monster"
commandlist['grab']="type grab [item] to take an item and place it in your bag"
commandlist['use']="type use [item] to use an item that is in your bag"

print("\ntype help for a list of all commands\n")


#Starting location:
location= bedroom




user.shield=broken_shield
user.weapon=broken_weapon
#This is really the only executed code for the whole game, its long because of the quitting functionality
#You can only save your score if you quit properly
#that means typing the word quit and then no



#import fixer as f

while not response  == "dfhsergghj":
  response=raw_input("\nCommand: \n")
  if response == "quit":
    ask_ok("You are about to quit, type no to quit")
    if relive==0:
      response="dfhsergghj"
#  try:
  holder=(response.split())
  mapping()
  what_you_do(holder)
#  except:

#    print("type a command please")

#f.file_fixer()


'''
if __name__== "__main__" :
  import doctest
  doctest.testmod()

'''


