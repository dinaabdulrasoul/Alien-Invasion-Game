import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai,screen):
		"""A class to represent the ship"""
		super(Ship,self).__init__()
		self.screen=screen
		self.image=pygame.image.load('Webp.net-resizeimage (5).png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		self.moving_right=False
		self.moving_left=False
		
		self.ai=ai
		
		self.center=float(self.rect.centerx) #initial position of the shhip
		
		
		
	def blitme(self):
		self.screen.blit(self.image,self.rect) #draws the image to the screen at position self.rect
	
	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai.speed_factor  #right flag movement with speed factor
		if self.moving_left and self.rect.left>0:
			self.center-= self.ai.speed_factor  #left movement flag with speed factor
			
		self.rect.centerx=self.center #returning rect back to center 
		
	def center_ship(self):
		self.center=self.screen_rect.centerx
