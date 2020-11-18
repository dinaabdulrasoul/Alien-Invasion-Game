import pygame
import pygame.font
from ship import Ship
from pygame.sprite import Group

class ScoreBoard():
	"""A class to report scoring info"""
	def __init__(self,ai,screen,stats):
		self.screen=screen
		self.ai=ai
		self.stats=stats
		self.screen_rect=screen.get_rect()
		
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		
		self.high_score=0
		
		self.prep_score()		
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		
	def prep_score(self):
		"""Turn score into a rendered image"""
		self.rounded_score=int(round(self.stats.score,-1))
		score_str="{:,}".format(self.rounded_score)
		self.score_image= self.font.render(score_str, True,self.text_color)
		
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20
		
	def prep_high_score(self):
		"""Display high score"""
		self.high_score=int(round(self.stats.high_score,-1))
		self.high_score_str="{:,}".format(self.high_score)
		
		self.high_score_image=self.font.render(self.high_score_str,True,self.text_color)
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.top=self.score_rect.top
		self.high_score_rect.centerx=self.screen_rect.centerx
		
	def prep_level(self):
		"""Shows your current level"""
		self.level=str(self.stats.level)
		self.level_image=self.font.render(self.level,True,self.text_color)
		self.level_rect=self.level_image.get_rect()
		self.level_rect.top=self.score_rect.bottom+10
		self.level_rect.right=self.score_rect.right
	
	def prep_ships(self):
		"""Shows how many ships are left"""
		self.ships=Group()
		for ship_number in range(0,self.stats.ships_left):
			ship=Ship(self.ai,self.screen)
			ship.rect.x=10+ship_number*ship.rect.width
			ship.rect.y=10
			self.ships.add(ship)
		
	def show_score(self):
		"""Draw score to screen"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen) #Draws whole sprite to screen
			

