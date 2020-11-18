import pygame

class Button():
	"""Class to describe the Play Button"""
	def __init__(self,ai,screen,msg):
		self.ai=ai
		self.screen=screen
		self.screen_rect=self.screen.get_rect()
		self.msg=msg
		self.width=200
		self.height=50
		self.button_color=(255,192,203)
		self.text_color=(255,255,255)
		self.font = pygame.font.SysFont(None, 48) #setting the font
		
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		#tells pygame to render the string text
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		"""Turn message into rendered image"""
		self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		self.screen.fill(self.button_color,self.rect) #draws rectangular potion on the screen
		self.screen.blit(self.msg_image,self.msg_image_rect) #draws rectangular image to the screen
