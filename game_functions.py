import sys
import pygame
from bullets import Bullets
from pygame.sprite import Group
from alien import Alien
from time import sleep
from gamestats import GameStats

def check_events(ai,screen,ship,bullets,aliens,stats,play_button,sb):
	""""Functions to wait for user's event"""
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				with open('high_score.txt','w') as file_object:
					file_object.write(str(stats.high_score))
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ai,screen,ship,bullets,stats,aliens)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ship)
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y=pygame.mouse.get_pos()
				check_play_button(mouse_x,mouse_y,stats,play_button,ship,aliens,bullets,ai,screen,sb)
				
def check_play_button(mouse_x,mouse_y,stats,play_button,ship,aliens,bullets,ai,screen,sb):
	button_clicked= play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		pygame.mouse.set_visible(False) #To hide mouse cursor once the game starts
		stats.reset_stats()
		ai.initialize_dynamic_settings()
		stats.game_active=True
		aliens.empty()
		bullets.empty()
		create_fleet(ai,screen,ship,aliens)
		ship.center_ship()
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
	
def check_keydown_events(event,ai,screen,ship,bullets,stats,aliens):	
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True	
	elif event.key==pygame.K_SPACE:
		fire_bullets(ai,screen,ship,bullets)
	elif event.key==pygame.K_q: #exits the game when q is pressed
		sys.exit()	
	elif event.key==pygame.K_p:
		pygame.mouse.set_visible(False) #To hide mouse cursor once the game starts
		stats.reset_stats()
		stats.game_active=True
		aliens.empty()
		bullets.empty()
		create_fleet(ai,screen,ship,aliens)
		ship.center_ship()
 		
def check_keyup_events(event,ship):	
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT: 
		ship.moving_left=False
	
def update_screen(ai,screen,ship,aliens,bullets,stats,play_button,sb):
	"""update images on the screen and flip to new screen"""
	#screen.fill(ai.bg_color)
	screen.blit(ai.background, [0, 0])
	ship.blitme()
	aliens.draw(screen)
	sb.show_score()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()
	
def update_bullets(ai,screen,ship,aliens,bullets,stats,sb):
	"""Removes bullets when they reach the screen's edges"""
	bullets.update()
	for bullet in bullets.copy(): #to get rid of the bullets after they have disappeared and we shouldn't ever work with an active list instead work with a copy
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)
		#print(len(bullets)) #I just used this to make sure of that the bullets that disappear are completely removed
	check_bullet_collision(ai,screen,ship,aliens,bullets,stats,sb)
	
def check_bullet_collision(ai,screen,ship,aliens,bullets,stats,sb):
	"""Respond to collisions with bullets"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) #check for collisons between bullets and aliens
	if collisions:
		for aliens in collisions.values():
			stats.score+=ai.alien_points*len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)
	if len(aliens)==0:
		bullets.remove()
		ai.increase_speed()
		create_fleet(ai,screen,ship,aliens)
		stats.level+=1
		sb.prep_level()	
		
def fire_bullets(ai,screen,ship,bullets):
	"""Creating new bullets and adding them to our group"""
	if len(bullets)<=ai.bullets_num:
		new_bullet=Bullets(ai,screen,ship) #creating a new bullet each time the space bar is pressed
		bullets.add(new_bullet) #adding the bullet to the group
		
		
def get_aliens_number(ai,alien_width):
	"""calculating number of aliens"""
	#alien_width=alien.rect.width
	space_x=ai.screen_width-(2*alien_width) #2*alien_width is the margins we need
	numbers_alien_x=int(space_x/(2*alien_width)) #size of each alien on the screen is twice its width to conserve the spaceings
	return numbers_alien_x
		
def get_rows_number(ai,ship_height,alien_height):
	"""calcuating the number of rows"""
	space_y=(ai.screen_length- (3*alien_height)-ship_height)
	number_rows=int(space_y/(2*alien_height))
	return number_rows
	
def create_alien(ai,screen,aliens,alien_number, row_number):
	"""creating an alien"""
	alien=Alien(ai,screen)
	alien_width=alien.rect.width
	alien.x=alien_width + 2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+(2*alien.rect.height*row_number)
	aliens.add(alien)

def create_fleet(ai,screen,ship,aliens):
	"""Create a full fleet of aliens"""
	alien=Alien(ai,screen) #this instance is only you used to get the aliens dimensions
	aliens_number_x=get_aliens_number(ai,alien.rect.width)
	rows_number=get_rows_number(ai,ship.rect.height,alien.rect.height)
	#print(rows_number)
	
	#creating the first row of aliens
	for row in range(0,rows_number):
		for alien_number in range(aliens_number_x):
			create_alien(ai,screen,aliens,alien_number,row)
			
def update_aliens(ai,screen,ship,aliens,bullets,stats,sb):
	"""check if fleet is at the edge then update its position"""
	check_fleet_edges(ai,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai,screen,ship,aliens,bullets,stats,sb)
	check_bottom_aliens(ai,screen,ship,aliens,bullets,stats)
	
def check_fleet_edges(ai,aliens):
	"""respond is an alien has reached the edge"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai,aliens)
			break
			
def change_fleet_direction(ai,aliens):
	"""Drop entire fleet and change its direction"""
	for alien in aliens.sprites():
		alien.rect.y+=ai.fleet_drop_speed
	ai.fleet_direction*=-1
	
def ship_hit(ai,screen,ship,aliens,bullets,stats,sb):
	"""What happens when the ship is hit"""
	if stats.ships_left>0:
		stats.ships_left-=1	
		sb.prep_ships()
		aliens.empty()
		bullets.empty()
		create_fleet(ai,screen,ship,aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active=False
		pygame.mouse.set_visible(True) #The cursor reappears so that the player can click on the button again
	
	
def check_bottom_aliens(ai,screen,ship,aliens,bullets,stats):
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(ai,screen,ship,aliens,bullets,stats)
			break
			
def check_high_score(stats,sb):
	"""Checks to see if there is a new high score"""
	if stats.score>stats.high_score:
		stats.high_score=stats.score
		sb.prep_high_score()
	
		
		
		
	
		
