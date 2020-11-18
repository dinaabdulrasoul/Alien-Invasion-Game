import pygame
from pygame.sprite import Sprite  #To import Sprite module

class Bullets(Sprite):
	"""A class to represent a single bullet"""
	def __init__(self,ai,screen,ship):
		super(Bullets,self).__init__()
		self.screen=screen
		
		#self.image=pygame.image.load('bullet_small.png')
		
		#creating the bullets as rectangles then positioning them with the ship
		self.ship=ship
		
		#self.rect=self.image.get_rect()
		
		self.rect=pygame.Rect(0,0,ai.bullet_width,ai.bullet_height)
		
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		
		#storing the bullet's position (y-coordinates)
		self.y=float(self.rect.y)
		
		self.color=ai.bullet_color
		self.speed_factor=ai.bullet_speed_factor
		
	def draw_bullet(self):
			#pygame.draw(self.image,self.rect) #draws the image to the screen at position self.rect
			pygame.draw.rect(self.screen,self.color,self.rect)
			
	def update(self):
		self.y-=self.speed_factor
		self.rect.y=self.y #update the rectangle position
			
		
