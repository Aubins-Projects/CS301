import os.path
import string
import random
import copy


#these are the global variables for the system

player=dict()
player["points"]=0
player["lives"]=3
player["relive"]=1
player["Hmultiplier"]=1
player["Dmultiplier"]=1
player["x"]=10
player["y"]=10


response=""
holder=list

#
#This is what lets you put your name in and then checks your score
def namechecker():
  name=raw_input("Enter your name please \n")
  if name in ('Aubin','aubin'):
    print("Welcome your highness")
  else:
    print("Welcome: "+name +"\nGood Luck! \n")
  return name


#this is to initialize your character its commented out below for testing purposes
def initial(name, player):
  while True:
    answer2=raw_input("What is your class (warrior or fighter)? \n")
    if answer2 in ("warrior","fighter"):
      break
  answer3=100
  user=players(name,answer3,answer2)
  print("\n")
  print("Your name: "+str(user.name))
  print("Your class: "+str(user.classs))
  player=class_adaption(user.classs,player)
  print("Your health: "+str(int(user.health)*player["Hmultiplier"]))
  print("Your damage: "+str(int(user.damage)*player["Dmultiplier"]))
  return user

def class_adaption(classs,player):
  if classs=="warrior":
    player["Hmultiplier"]=2
    player["Dmultiplier"]=1
  if classs=="fighter":
    player["Hmultiplier"]=1
    player["Dmultiplier"]=2
  return player


#This is for looking specifically at one thing
def look(what):
  print(what.description)


#This if for looking at the entire room
def room_contents_look(what):
  print("\n\n************************** \n")
  i=0
  for x in range(len(what.contents)):
    print(what.contents[i].name)
    i=1+i
  if what.east== None:
    i=0
  else:
    print(str(what.east)+" is East"),
    if (what.east.visited==False):
      print "--Not visited yet"
    else:
      print
  if what.north== None:
    i=0
  else:
    print(str(what.north)+" is North"),
    if (what.north.visited==False):
      print "--Not visited yet"
    else:
      print
  if what.west== None:
    i=0
  else:
    print(str(what.west)+" is West"),
    if (what.west.visited==False):
      print "--Not visited yet"
    else:
      print
  if what.south== None:
    i=0
  else:
    print(str(what.south)+" is South"),
    if (what.south.visited==False):
      print "--Not visited yet"
    else:
      print
    print("************************** \n")


#This is the reassurance for trying to quit
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
  while True:
    player["relive"]
    ok = raw_input( prompt + '\n')
    if ok in ('y', 'ye', 'yes'):
      print("you are alive once more!")
      player["relive"]=1
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      print("You chose to be a quitter")
      logfile = open("Highscores.txt", "a")
      logfile.write(str(player["points"])+"\t" + name+"\n")
      logfile.close()
      player["relive"]=0
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
  randonum=random.randrange(1,5)
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
  print("The your score is: "+ str(player["points"]))
  



#this is your starting coordinates
    


def coordinates(direction):
  for char in direction:
    global location
    sav_x=player["x"]
    sav_y=player["y"]
    
    if char in ["e"]:
       player["x"]=player["x"]+1
    elif char in ["w"]:
       player["x"]=player["x"]-1
    elif char in ["n"]:
       player["y"]=player["y"]+1
    elif char in ["s"]:
       player["y"]=player["y"]-1
    loc_finder(sav_x,sav_y)

###########################################################################################
#This is the automatic mapper once you add the grids in the room OBJECT and the floor OBJECT


def loc_finder(sav_x,sav_y):
  global location
  check =0
  for room in level1.rooms:
    if room.x==player["x"] and room.y==player["y"]:
      location= room
      check=1
  if check == 0:
      player["x"]=sav_x
      player["y"]=sav_y
  print(str(name)+", you are in the "+str(location))
  location.visitedFun()

def map_finder(x,y):
  for room in level1.rooms:
    if room.x==x and room.y==y:
      return room

def mapping():
  global location
  temp_location=location
  temp_x=player["x"]
  temp_y=player["y"]

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
      print ("\n\nthis place: "+location.description)
      room_contents_look(location)
      if location.baddies:
        print("Monster name: "+str(location.baddies.name))
        print("Monster health: "+str(location.baddies.health))
        print("Monster damage: "+str(location.baddies.damage))


def level_upper(monsterh,monsterd):
  global user
  totalpoints=monsterh+monsterd
  totalexp=totalpoints
  user.exp+=totalexp
  while user.exp > 500:
    user.exp-=500
    user.level+=1
    user.exp=user.exp*(100-user.level)/150
    print("*******************")
    print("you just leveled up to: "+str(user.level))
    print("*******************")
  count=0
  for r in level1.rooms:
    if r.baddies!=None:
      r.baddies.healthy()
      count+=1
  print "The monsters appear to have gained strength as well!"
  print "{0} monsters remaining!".format(count)

def about_command(holder):
  if holder[0]=="about":
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
    if otherholder == "all":
      for item in location.contents:
        user.contents.append(item)
        location.contents.remove(item)
        print("You just picked up something that/is: "+user.contents[user.contents.index(item)].description)
    if otherholder in location.contents:
      user.contents.append(location.contents[location.contents.index(otherholder)])
      location.contents.remove(otherholder)
      print(user.contents[user.contents.index(otherholder)].description)

def unlocked_rooms(item,loc):
  loc.x=item.x
  loc.y=item.y
  print "A room was just unlocked!"

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
        print("you just equipped a(n) "+str(otherholder)+" which "+str(user.weapon.description))

def unequip_command(holder):
  if holder[0] in ["unequip", "un"]:
    temp_word_holder=str(holder[0])
    holder.remove(temp_word_holder)
    otherholder=' '.join(holder)     
    if otherholder == user.weapon:
        user.contents.append(user.weapon)
        user.weapon=None
        print("you just took off a(n) "+str(otherholder))
    elif otherholder == user.shield:
        user.contents.append(user.shield)
        user.shield=None
        print("you just took off a(n) "+str(otherholder))

        
      
def bag_command(holder):
  if holder[0]=="bag":
    import bag
    bag.main(user.contents)
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
    if otherholder == "all":
      for item in user.contents:
        location.contents.append(item)
        user.contents.remove(item)
        print("you just dropped "+ str(item) + " in the " +str(location))
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
        if otherholder in location.usables or location.key.name==user.contents[user.contents.index("key")].name:
         cause_and_effect(otherholder)
      else:
        print(str(user.contents[user.contents.index(otherholder)])+" is not usable.")


def cause_and_effect(otherholder):
  global location
  if location.usables[location.usables.index(otherholder)].effect!="":
    print location.usables[location.usables.index(otherholder)].effect
  if (len(location.usables[location.usables.index(otherholder)].changer)>0):
    for item in location.usables[location.usables.index(otherholder)].changer:
      location.contents.append(item)
      location.usables[location.usables.index(otherholder)].changer.remove(item)
  if (location.usables[location.usables.index(otherholder)].world=="yes"):
    unlocked_rooms(location.usables[location.usables.index(otherholder)],location.usables[location.usables.index(otherholder)].atloc)
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
  if holder[0]=="attack":
    #holder.remove("attack")
    #otherholder=' '.join(holder)
    neitherdead=0
    #if otherholder == location.baddies:
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
  def __init__(self, name, value, description, power=0, equip="item",atloc='',usable="no",world="no",destroy="no"):
    self.name=name
    self.value=value
    self.description=description
    self.power=power
    self.equip=equip
    self.usable=usable
    self.world=world
    self.x=300000
    self.y=300000
    self.atloc=atloc
    self.destroy=destroy
    self.effect=""
    self.changer=list()

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
# name, value, description, power, equip="item",atloc='',usable="no",world="no",destroy="no" 

i1=Object("clock",100,"time is stuck at 11:11...that is precarious, precarious indeed")
i2=Object("broom",15,"a dusting device, with a long lever")
i3=Object("feather",20,"tickles the nose when placed ever so close to it")
i4=Object("match",25,"seems to be some sort of small relative to the torches")
i5=Object("Blood Diamond",150000,"a blood diamond, formed from vast amounts of blood and a fiery explosion", 20)
i6=Object("ball", 1500, "a ball that looks like a pong ball",10)
i7=Object("King's scepter", 10000, "a silver sceptre",30)
i8=Object("vorpel sword", 200, "a strange looking sword",1000)
i9=Object("bedpan", 3, "a smelly metal bowl",2)
i10=Object("skull", 15000, "a giant skull",100)
i11=Object("talon", 1500, "a giant talon",100)
i12=Object("lint", 100, "a piece of lint",100)
i13=Object("scrap metal", 150, "a gold crown with many jewels",10)
i14=Object("credit card", 1, "this seems out of place",78)
i15=Object("old movie",20,"looks like pokemon 1",300)
i16=Object("juice box", 3, "probably not good anymore",2)
i17=Object("plate", 20, "appears to be able to hold things on its surface",1000)
i18=Object("dead mouse", 100, "pretty sure you should not keep this",30)

u1=Object("silver necklace", 100, "you could sell this if there was a shop",30)
u2=Object("bronze tube", 100, "pretty much just a burden to carry",30)
u3=Object("golden chalice", 100, "could store a liquid, or maybe your tears?",30)



kbedpan=Object("bedpan", 3, "a smelly metal bowl",2)
kbedpan.usable="yes"
torch=Object("torch", 1, "fire attatched to a stick",78)
torch.usable="yes"
crown = Object("crown", 15000, "a gold crown with many jewels",10)
crown.usable="yes"
key=Object("key",1200,"this might be useful for doing key things",12)
key.usable="yes"
key.destroy="yes"



a1=Object("paper shield",10,"will mitigate some damage",300, "shield")
shield=Object("shield",200,"will mitigate some damage",300,"shield")
good_s=Object("good shield",200,"will mitigate some damage",400,"shield")
best_s=Object("best shield",200,"will mitigate huge damage",1000,"shield")
broken_shield=Object("broken shield",100,"will mitigate some damage",30, "shield")
perfect_s=Object("best shield",10000,"will mitigate massive damage",30000, "shield")

paper_weapon=Object("paper weapon",10,"will cause some damage",300, "weapon")
good_w=Object("good weapon",100,"will cause decent damage",400, "weapon")
best_w=Object("best weapon",100,"will cause huge damage",1000, "weapon")
broken_weapon=Object("broken weapon",100,"will cause some damage",30, "weapon")
perfect_w=Object("best weapon",10000,"will deal massive damage",30000, "weapon")







# name, value, description, power,uid, equip="item",atloc='',usable="no",world="no",destroy="no"
##################################################################################################################    
    
    
    
    
    
############################################################################################################
uncommon=itemlist("uncommon")
#UNCOMMON ITEMS

uncommon.items.append(crown)
uncommon.items.append(u1)
uncommon.items.append(u2)
uncommon.items.append(u3)





##################################################################################################################


#COMMON ITEMS

common=itemlist("common")
common.items.append(i1)
common.items.append(i2)
common.items.append(i3)
common.items.append(i4)
common.items.append(i5)
common.items.append(i6)
common.items.append(i7)
common.items.append(i8)
common.items.append(i9)
common.items.append(i10)
common.items.append(i11)
common.items.append(i12)
common.items.append(i18)



#############################################################################################################


#This a player/your player called the user in the code  
class players:
  def __init__(self,name,health,classs,exp=0,level=1):
    self.name=name
    self.health=health
    self.classs=classs
    self.exp=exp
    self.contents=list()
    self.damage=10 
    self.shield=None
    self.weapon=None
    self.level=level
  def __str__(self):
    return str(self.name)
#####################################################################################################################
#add players here
#uncomment namechecker and initial




name=namechecker()
user=initial(name,player)







#####################################################################################################################

MonsterList=list()

#These are the monsters in game
class monster:
  def __init__(self,name,color,classs,lootTable=common,boss=False):
    self.name=name
    self.health=0
    self.color=color
    self.classs=classs
    self.damage=10
    self.contents=list()
    self.keys=""
    self.boss=boss
    self.starter() 
    self.healthy()
    self.lootTable=lootTable
    
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other
  def starter(self):
    if self.name!="test" and self.boss==False:
      MonsterList.append(self)
  def healthy(self):
    
    if self.boss==False:
      self.health=random.randint(100,200)*(user.level+random.randint(2,5))
      self.damage=random.randint(1,40)*(user.level+random.randint(0,5))
    else:
      self.health=random.randint(100,200)*(user.level+random.randint(8,12))
      self.damage=random.randint(1,40)*(user.level+random.randint(5,9))
  def looter(self):
    for i in range(random.randint(1,4)):
      self.contents.append(random.choice(self.lootTable.items))

######################################################################################################################
#Add monsters below

blob=monster("blob","yellow","warrior")
dragon=monster("dragon","yellow","warrior")
high_wizard=monster("high wizard","black","warrior")


#boss

bosslist=list()
Fbosslist=list()

class Boss(monster):
  def __init__(self,name,color,classs):
    monster.__init__(self,name,color,classs,uncommon,True)
    self.contents.append(key)
    self.bossStarter()
  def __str__(self):
    return monster.__str__(self)
  def bossStarter(self):
    bosslist.append(self)


b1=Boss("Giant Gnarlk","black", "warrior")
b2=Boss("Werewolf","pink","warrior")
b3=Boss("Angry Miner","red","warrior")
b4=Boss("Troll","camo","warrior")
b5=Boss("Kirbal","purple","warrior")
b6=Boss("Deranged Prisoner","green","warrior")
b7=Boss("Mutant Gorilla","black","warrior")




class FinalBoss(monster):
  def __init__(self,name,color,classs):
    monster.__init__(self,name,color,classs,uncommon,True)
    self.bossStarter()
  def __str__(self):
    return monster.__str__(self)
  def bossStarter(self):
    Fbosslist.append(self)
  def killed(self):
    print("YOU HAVE WON THE GAME!!!")

f1=FinalBoss("EECS Instructor","gray","warrior")


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
fire_spolde.changer.append(i5)
#################
############################################################################################
class floor:
  def __init__(self,name,rooms=list()):
    self.name=name
    self.rooms=rooms
  def __str__(self):
    return str(self.name)

############################################################################################################
level1= floor("ground level")

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
    self.visited=False
    self.start_up()
    self.key=i1
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
############################################################################################################
#Add rooms Below

castle_entrance=Room("The Castle Entrance")
castle_entrance.description="the starting place of the dungeon"
castle_entrance.x=10
castle_entrance.y=10
castle_entrance.contents.append(key)

cell1=Room("Prison Cell")
cell1.description="just your average cell"
cell1.x=10
cell1.y=16

cell2=Room("Prison Cell")
cell2.description="just your average cell"
cell2.x=9
cell2.y=15

cell3=Room("Prison Cell")
cell3.description="just your average cell"
cell3.x=9
cell3.y=16

hallway1=Room("Hallway")
hallway1.description="links other rooms, and may contain a torch or two"
hallway1.x=11
hallway1.y=8

hallway2=Room("Hallway")
hallway2.description="links other rooms, and may contain a torch or two"
hallway2.x=11
hallway2.y=9

hallway3=Room("Hallway")
hallway3.description="links other rooms, and may contain a torch or two"
hallway3.x=11
hallway3.y=10

hallway4=Room("Hallway")
hallway4.description="links other rooms, and may contain a torch or two"
hallway4.x=11
hallway4.y=11

hallway5=Room("Hallway")
hallway5.description="links other rooms, and may contain a torch or two"
hallway5.x=11
hallway5.y=12

hallway6=Room("Hallway")
hallway6.description="links other rooms, and may contain a torch or two"
hallway6.x=12
hallway6.y=10

hallway7=Room("Hallway")
hallway7.description="links other rooms, and may contain a torch or two"
hallway7.x=13
hallway7.y=10

hallway8=Room("Hallway")
hallway8.description="links other rooms, and may contain a torch or two"
hallway8.x=14
hallway8.y=8

hallway9=Room("Hallway")
hallway9.description="links other rooms, and may contain a torch or two"
hallway9.x=14
hallway9.y=9

hallway10=Room("Hallway")
hallway10.description="links other rooms, and may contain a torch or two"
hallway10.x=14
hallway10.y=10

hallway11=Room("Hallway")
hallway11.description="links other rooms, and may contain a torch or two"
hallway11.x=14
hallway11.y=11

hallway12=Room("Hallway")
hallway12.description="links other rooms, and may contain a torch or two"
hallway12.x=14
hallway12.y=12

hallway13=Room("Hallway")
hallway13.description="links other rooms, and may contain a torch or two"
hallway13.x=15
hallway13.y=10

hallway14=Room("Hallway")
hallway14.description="links other rooms, and may contain a torch or two"
hallway14.x=16
hallway14.y=10

hallway15=Room("Hallway")
hallway15.description="links other rooms, and may contain a torch or two"
hallway15.x=17
hallway15.y=10

hallway16=Room("Hallway")
hallway16.description="links other rooms, and may contain a torch or two"
hallway16.x=17
hallway16.y=11

hallway17=Room("Hallway")
hallway17.description="links other rooms, and may contain a torch or two"
hallway17.x=17
hallway17.y=12

hallway18=Room("Hallway")
hallway18.description="links other rooms, and may contain a torch or two"
hallway18.x=17
hallway18.y=13

hallway19=Room("Hallway")
hallway19.description="links other rooms, and may contain a torch or two"
hallway19.x=17
hallway19.y=14

hallway20=Room("Hallway")
hallway20.description="links other rooms, and may contain a torch or two"
hallway20.x=17
hallway20.y=15

hallway21=Room("Hallway")
hallway21.description="links other rooms, and may contain a torch or two"
hallway21.x=17
hallway21.y=16

hallway22=Room("Hallway")
hallway22.description="links other rooms, and may contain a torch or two"
hallway22.x=17
hallway22.y=17

hallway23=Room("Hallway")
hallway23.description="links other rooms, and may contain a torch or two"
hallway23.x=17
hallway23.y=18

hallway24=Room("Hallway")
hallway24.description="links other rooms, and may contain a torch or two"
hallway24.x=17
hallway24.y=19

hallway25=Room("Hallway")
hallway25.description="links other rooms, and may contain a torch or two"
hallway25.x=16
hallway25.y=19

hallway26=Room("Hallway")
hallway26.description="links other rooms, and may contain a torch or two"
hallway26.x=15
hallway26.y=19

hallway27=Room("Hallway")
hallway27.description="links other rooms, and may contain a torch or two"
hallway27.x=15
hallway27.y=20

hallway28=Room("Hallway")
hallway28.description="links other rooms, and may contain a torch or two"
hallway28.x=15
hallway28.y=21

hallway34=Room("Hallway")
hallway34.description="links other rooms, and may contain a torch or two"
hallway34.x=13
hallway34.y=20

hallway35=Room("Hallway")
hallway35.description="links other rooms, and may contain a torch or two"
hallway35.x=13
hallway35.y=21

hallway41=Room("Hallway")
hallway41.description="links other rooms, and may contain a torch or two"
hallway41.x=14
hallway41.y=19

hallway42=Room("Hallway")
hallway42.description="links other rooms, and may contain a torch or two"
hallway42.x=13
hallway42.y=19

hallway43=Room("Hallway")
hallway43.description="links other rooms, and may contain a torch or two"
hallway43.x=18
hallway43.y=14

hallway44=Room("Hallway")
hallway44.description="links other rooms, and may contain a torch or two"
hallway44.x=19
hallway44.y=14
hallway44.baddies=random.choice(bosslist)

hallway45=Room("Hallway")
hallway45.description="links other rooms, and may contain a torch or two"
hallway45.x=20
hallway45.y=14

hallway46=Room("Hallway")
hallway46.description="links other rooms, and may contain a torch or two"
hallway46.x=21
hallway46.y=14

hallway47=Room("Hallway")
hallway47.description="A mystical item calls you nearby. '{0}? {0}, is that you?' ".format(user.name)
hallway47.x=22
hallway47.y=14

hallway49=Room("Hallway")
hallway49.description="links other rooms, and may contain a torch or two"
hallway49.x=18
hallway49.y=16

hallway50=Room("Hallway")
hallway50.description="links other rooms, and may contain a torch or two"
hallway50.x=19
hallway50.y=16

hallway51=Room("Hallway")
hallway51.description="links other rooms, and may contain a torch or two"
hallway51.x=20
hallway51.y=16

hallway52=Room("Hallway")
hallway52.description="links other rooms, and may contain a torch or two"
hallway52.x=21
hallway52.y=16

hallway53=Room("Hallway")
hallway53.description="A mystical item calls you nearby. '{0}? {0}, is that you?' ".format(user.name)
hallway53.x=22
hallway53.y=16

goodWeapon=Room("Hidden Armory")
goodWeapon.description="A grand weapon sits in the middle of the room"
goodWeapon.x=1900
goodWeapon.y=1500
hallway44.makekey(19,15,goodWeapon,"yes")
hallway50.makekey(19,15,goodWeapon,"yes")

room1=Room("Room")
room1.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room1.x=11
room1.y=13


room2=Room("Room")
room2.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room2.x=11
room2.y=7


room20=Room("Secret Room")
room20.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room20.x=600
room20.y=600
room1.makekey(10,13,room20,"yes")


room3=Room("Room")
room3.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room3.x=12
room3.y=9

room4=Room("Room")
room4.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room4.x=12
room4.y=11

room5=Room("Room")
room5.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room5.x=13
room5.y=7

room6=Room("Room")
room6.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room6.x=14
room6.y=6

room7=Room("Room")
room7.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room7.x=15
room7.y=7

room8=Room("Room")
room8.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room8.x=13
room8.y=12

room9=Room("Room")
room9.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room9.x=14
room9.y=13

room10=Room("Room")
room10.description="might hold a secret or {0}".format(random.choice(["two","three","four","five","six","none","not a secret, that is the question"]))
room10.x=15
room10.y=12

boss1=Room("Boss Room")
boss1.description="A boss lies in wait"
boss1.x=13
boss1.y=22
boss1.baddies=random.choice(bosslist)

boss2=Room("Boss Room")
boss2.description="A boss lies in wait"
boss2.x=1300
boss2.y=2300
boss1.makekey(13,23,boss2,"yes")
boss2.baddies=random.choice(bosslist)


boss3=Room("Boss Room")
boss3.description="A boss lies in wait"
boss3.x=1300
boss3.y=2400
boss2.makekey(13,24,boss3,"yes")
boss3.baddies=random.choice(bosslist)

boss4=Room("Boss Room")
boss4.description="A boss lies in wait"
boss4.x=13
boss4.y=2500
boss3.makekey(13,25,boss4,"yes")
boss4.baddies=random.choice(bosslist)

boss5=Room("Boss Room")
boss5.description="A boss lies in wait"
boss5.x=13
boss5.y=2600
boss4.makekey(13,26,boss5,"yes")
boss5.baddies=random.choice(bosslist)

boss6=Room("Boss Room")
boss6.description="A boss lies in wait"
boss6.x=15
boss6.y=22
boss6.baddies=random.choice(bosslist)

boss7=Room("Boss Room")
boss7.description="A boss lies in wait"
boss7.x=15
boss7.y=2300
boss6.makekey(15,23,boss7,"yes")
boss7.baddies=random.choice(bosslist)

boss8=Room("Boss Room")
boss8.description="A boss lies in wait"
boss8.x=15
boss8.y=2400
boss7.makekey(15,24,boss8,"yes")
boss8.baddies=random.choice(bosslist)

boss9=Room("Boss Room")
boss9.description="A boss lies in wait"
boss9.x=15
boss9.y=2500
boss8.makekey(15,25,boss9,"yes")
boss9.baddies=random.choice(bosslist)

boss10=Room("Boss Room")
boss10.description="A boss lies in wait"
boss10.x=15
boss10.y=2600
boss9.makekey(15,26,boss10,"yes")
boss10.baddies=random.choice(bosslist)

boss11=Room("Boss Room")
boss11.description="The Final boss lies in wait {0}. You had better be prepared".format(user.name)
boss11.x=14
boss11.y=2600
boss10.makekey(14,26,boss11,"yes")
boss5.makekey(14,26,boss11,"yes")
boss11.baddies=random.choice(Fbosslist)

treasureRoom1=Room("Treasure Room")
treasureRoom1.description="Contains a vast amount of treasure"
treasureRoom1.x=900
treasureRoom1.y=1700
cell3.makekey(9,17,treasureRoom1,"yes")


cave1=Room("Cave")
cave1.description=("Seems pretty damp")
cave1.x=10
cave1.y=14

prison1=Room("Prison")
prison1.description=("Seems pretty cramped")
prison1.x=10
prison1.y=15

best_room1=Room("Altar of a grand Weapon")
best_room1.description=("Emense power eminates from the room...and possibly else where?")
best_room1.x=2200
best_room1.y=1500
best_room1.contents.append(best_w)
hallway47.makekey(22,15,best_room1,"yes")
hallway53.makekey(22,15,best_room1,"yes")

best_room2=Room("Altar of a grand shield")
best_room2.description=("Emense power eminates from the room...and possibly else where?")
best_room2.x=2300
best_room2.y=1500
best_room2.contents.append(best_s)
best_room1.makekey(23,15,best_room2,"yes")

user.contents.append(key)
user.contents.append(key)
user.contents.append(key)
user.contents.append(key)
user.contents.append(key)

#These are all of the commands in the game
commandlist = dict()

commandlist['points']="type points to get your current points"
commandlist['go']="type go and then a cardinal direction"
commandlist['look']="type look and then a cardinal direction (n,s,e,w), or around to look around"
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
location= castle_entrance
castle_entrance.visitedFun()
#to test bag functionality

user.shield=perfect_w
user.weapon=perfect_s

#This is really the only executed code for the whole game, its long because of the quitting functionality
#You can only save your score if you quit properly
#that means typing the word quit and then no



#import fixer as f

while not response  == "dfhsergghj":
  response=raw_input("\nCommand: \n")
  for i in range(40):
    print
  if response == "quit":
    ask_ok("You are about to quit, type no to quit")
    if player["relive"]==0:
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


