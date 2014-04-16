import math

def ball_img():
	return "ball.png"

def xPos(ini_vel, angle_of_fire, time):
	"""
	description: takes an initial velocity, angle of fire, and the time after being fired
	of a projectile and returns the position on the x axis the projectile will be at the 
	given time as an integer.
	
	assumptions: initial velocity will be in put in meters per second, the angle of fire
	will be in degrees, and the time will be in seconds.
	
	>>> xPos(120, 30 ,0)
	0
	>>> xPos(120, 30, 2)
	207
	>>> xPos(200, 45, 1)
	141
	>>> xPos(200, 45, 3)
	424
	"""
	x_pos = ini_vel *  math.cos(math.radians(angle_of_fire)) * time
	return int(x_pos)
	
def yPos(ini_vel, angle_of_fire, time):
	"""
	description: takes an initial velocity, angle of fire, and the time after being fired
	of a projectile and returns the position on the y axis the projectile will be at the 
	given time as an integer.
	
	assumptions: initial velocity will be in put in meters per second, the angle of fire
	will be in degrees, and the time will be in seconds.
	
	>>> yPos(120, 30 ,0)
	0
	>>> yPos(120, 30, 2)
	80
	>>> yPos(200, 45, 1)
	131
	>>> yPos(200, 45, 3)
	336
	"""
	g = 9.807
	y_pos = (ini_vel * math.sin(math.radians(angle_of_fire)) * time) - (g * time ** 2)
	return int(y_pos)

def distance(tank_x, cursor_x, tank_y, cursor_y):
	x_dist_sq = (float(cursor_x) - tank_x) ** 2
	y_dist_sq = (float(cursor_y) - tank_y) ** 2
	dist = (x_dist_sq + y_dist_sq) ** (.5)
	return dist
	
def power(distance):
	if distance == 0:
		return 0
	

#if __name__ == "__main__":
		
		
	

