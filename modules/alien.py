import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""
	def __init__(self,ai,screen):
		super(Alien,self).__init__()
		self.screen=screen
		self.ai=ai
		self.image=pygame.image.load('alien_small.png')
		self.rect=self.image.get_rect()
		
		#start each alien near the top left of the screen (where the origin is)
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
		#storing the alien's position 
		self.x=float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	
	def update(self):
		self.x+=self.ai.alien_speed_factor*self.ai.fleet_direction
		self.rect.x=self.x
		
	def check_edges(self):
		"""returns true if the alien is at the edge of the screen"""
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True
		
	
	
