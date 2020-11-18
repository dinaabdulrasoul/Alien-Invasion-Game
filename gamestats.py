import pygame

class GameStats():
	"""Tracking the statistics of the alien invasion game"""
	def __init__(self,ai):
		self.ai=ai
		self.high_score=0
		with open('high_score.txt','r') as file_object:
			self.high_score=int(file_object.read())
		self.reset_stats()
	
	def reset_stats(self):
		"""Initalize statistics that can change during the game"""
		self.score=0
		self.ships_left=self.ai.ship_limit
		self.game_active=False
		self.level=1
