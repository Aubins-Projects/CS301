def distance(tank_x, cursor_x, tank_y, cursor_y):
	x_dist_sq = (float(cursor_x) - tank_x) ** 2
	y_dist_sq = (float(cursor_y) - tank_y) ** 2
	dist = (x_dist_sq + y_dist_sq) ** (.5)
	return dist
	
def power(distance):
	if distance == 0:
		return 0
	
	
# if __name__ == "__main__":
	# print distance(2, 6, 2, 5)