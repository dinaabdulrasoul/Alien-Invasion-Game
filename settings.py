import pygame
class Settings():
	"""A class to intialize all the values in our game: controlling the appearance of the game and the speed of the ship and bullet details"""
	def __init__(self):
		"""Initiliazting the static game settings"""
		self.screen_width=1200
		self.screen_length=800
		self.bg_color=(230,230,230)
		self.background=pygame.image.load("Webp.net-resizeimage (4).png")
		self.bullet_width=4
		self.bullet_height=15
		self.bullet_color=(255,255,255)
		self.bullets_num=10 #To limit the number of bullets per screen to encourage accuracy
		self.fleet_drop_speed=20
		self.ship_limit=3
		self.speedup_scale=1.2 #How quickly the game speeds up
		self.score_scale=1.5
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.speed_factor= 7   #Speed of the ship
		self.bullet_speed_factor=15
		self.alien_speed_factor= 5
		self.fleet_direction= 1 # 1 means right
		self.alien_points=50
		
	def increase_speed(self):
		self.speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points=int(self.alien_points*self.score_scale)
	
		
	

