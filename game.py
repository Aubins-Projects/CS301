def main():

  #Import all needed modules 
  import pygame, sys
  from pygame.locals import *
  import balls, tanks

  #assign all used images to variables
  bg_image = "bg.jpg"
  ball_img = balls.ball_img()
  tank_body = tanks.tank_body()
  tank_tube = tanks.tank_tube()

  #initialize pygame
  pygame.init()

  #create a game screen
  screen = pygame.display.set_mode((1280,720), 0, 32)

  #load and convert images for game
  background = pygame.image.load(bg_image).convert()
  ball = pygame.image.load(ball_img).convert_alpha()
  tank = pygame.image.load(tank_body).convert_alpha()
  tube = pygame.image.load(tank_tube).convert_alpha()

  #set inital values for game objects
  tank_x, tank_y = 0, 670
  tank_x_m = 0
  ball_x, ball_y = 0, 720
  cursor_pos = [0,0]
  clock = pygame.time.Clock()
  time = 0

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        

      if event.type == KEYDOWN:
        if event.key == K_a:
          tank_x_m = - 3
        if event.key == K_d:
          tank_x_m = + 3
        if event.key == K_q:
          pygame.quit()
          
      
      if event.type == KEYUP:
        if event.key == K_a:
          tank_x_m = 0
        if event.key == K_d:
          tank_x_m = 0
      
      if event.type == MOUSEBUTTONUP:
        cursor_pos = pygame.mouse.get_pos()
        dist = balls.distance(tank_x, cursor_x, tank_y, cursor_y)
        print (dist)
    
    tank_x += tank_x_m
    cursor_x = cursor_pos[0]
    cursor_y = cursor_pos[1]
    
    screen.blit(background, (0,0))
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(tank, (tank_x, tank_y))

    milli = 0

    while milli < 50:
      milli += clock.tick()

    time += 0.25

    import tanks

    ball_x = balls.xPos(120, 45, time)
    ball_y = 720 - balls.yPos(120, 45, time)

    if ball_x > 1280 or ball_y < 0:
      ball_x, ball_y = 0, 720
      time = 0
  
    pygame.display.update()


