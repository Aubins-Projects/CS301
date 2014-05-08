import pygame, sys, random
from pygame.locals import *

def createWall(img_path):
	images = []
	for val in range(10):
		images.append(pygame.image.load(img_path).convert())
	for val in random.sample(range(10), 4):
		images[val] = None
	return images
		
def createWallRects(wall_list):
	rects = []
	for img in wall_list:
		if not img == None:
			rects.append(img.get_rect())
		else:
			rects.append(None)
	return rects

def createWallY(wall_list):
	lst = []
	y = 0
	for x in wall_list:
		if not x == None:
			lst.append(y)
			y += 64
		else:
			lst.append(None)
			y += 64
	return lst

def fight():
	screen_h, screen_w = 640, 1024
	screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
	pygame.display.set_caption("Fight")

	background_img = "cave.png"
	background = pygame.image.load(background_img).convert()

	ball_img = "ball.png"
	ball = pygame.image.load(ball_img).convert_alpha()
	ball.set_colorkey((0,0,0), RLEACCEL)
	ball_x, ball_y = screen_h / 2, screen_w / 2
	ball_speed = 10
	ball_x_move, ball_y_move = -ball_speed, ball_speed
	ball_rect = ball.get_rect()
	ball_rect.topleft = (ball_x, ball_y)

	paddle_img = "paddle.png"
	paddle = pygame.image.load(paddle_img).convert_alpha()
	paddle_x, paddle_y = 1, screen_h / 2
	paddle_speed = 7
	paddle_move = 0
	paddle_rect = paddle.get_rect()
	paddle_rect.topleft = (paddle_x, paddle_y)

	wall_tile_img = "wall_tile.png"
	wall_list = createWall(wall_tile_img)
	wall_x = 1004
	wall_y_list = createWallY(wall_list)
	wall_rects = createWallRects(wall_list)
	for index in range(len(wall_rects)):
		if not wall_rects[index] == None:
			wall_rects[index].topleft = (wall_x, wall_y_list[index]) 
		
	clock = pygame.time.Clock()
	FPS = 30
	hits = 0
	speedUpHits = 2
	speedUpIncrement = 1
	end = False
	
	while not end:
		
		if hits == speedUpHits:
			ball_speed += speedUpIncrement
			hits = 0
			speedUpHits *= 1.25
			
		for event in pygame.event.get():
	
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
			if event.type == KEYDOWN:
				if event.key == K_w:
					paddle_move = -paddle_speed
				elif event.key == K_s:
					paddle_move = +paddle_speed
				elif event.key == K_UP:
					paddle_move = -paddle_speed
				elif event.key == K_DOWN:
					paddle_move = +paddle_speed
					
			if event.type == KEYUP:
				if event.key == K_w:
					paddle_move = 0
				elif event.key == K_s:
					paddle_move = 0
				elif event.key == K_UP:
					paddle_move = 0
				elif event.key == K_DOWN:
					paddle_move = 0
			
		if ball_rect.colliderect(paddle_rect):
			ball_x_move = +ball_speed
			hits += 10
			
		for rect in wall_rects:
			if not rect == None:
				if rect.colliderect(ball_rect):
					ball_x_move = -ball_speed
				
		if ball_x > 1024:
			end = True
			return True
			
		if ball_x < -24:
			end = True
			return False
			
		if ball_y < 0:
			ball_y_move = ball_speed
			
		if ball_y > 616:
			ball_y_move = -ball_speed
				
		ball_x += ball_x_move
		ball_y += ball_y_move
		ball_rect.topleft = (ball_x, ball_y)
		
		paddle_y += paddle_move
		paddle_rect.topleft = (paddle_x, paddle_y)
		
		screen.blit(background, (0, 0))
		screen.blit(ball, (ball_x, ball_y))
		screen.blit(paddle, (paddle_x, paddle_y))
		
		for index in range(len(wall_list)):
			if wall_list[index] != None:
				screen.blit(wall_list[index], (wall_x, wall_y_list[index]))
			
		clock.tick(FPS)

		pygame.display.update()
