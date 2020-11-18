#import sys #no loner needed now as we only needed it to check events in module game_functions
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullets import Bullets
from gamestats import GameStats
from time import sleep #allows us to pause the game for a bit
from button import Button
from scoreboard import ScoreBoard

def run_game(): 
	pygame.init()
	ai=Settings()
	screen=pygame.display.set_mode((ai.screen_width,ai.screen_length))
	#screen=pygame.display.set_mode((1200,800))
	play_button=Button(ai,screen,"PLAY")
	ship=Ship(ai,screen)
	bullets=Group() #A group to store bullets in it
	aliens=Group()
	gf.create_fleet(ai,screen,ship,aliens) #to create the fleet of aliens
	stats=GameStats(ai)
	sb=ScoreBoard(ai,screen,stats)
	while True:
		gf.check_events(ai,screen,ship,bullets,aliens,stats,play_button,sb)
		if stats.game_active: 
			ship.update() #The ship’s position will update after we’ve checked for keyboardevents and before we update the screen.
			gf.update_aliens(ai,screen,ship,aliens,bullets,stats,sb)
			gf.update_bullets(ai,screen,ship,aliens,bullets,stats,sb )
		gf.update_screen(ai,screen,ship,aliens,bullets,stats,play_button,sb)
		pygame.display.set_caption("Alien Invasion")
		
		
run_game()




