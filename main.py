import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int (0.8 * SCREEN_WIDTH)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minh\'s Shooter')

class Soldier(pygame.sprite.Sprite):
	def __init__(self, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('Assets/img/player/Idle/0.png')
		self.img = pygame.transform.scale(img, ( int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.img.get_rect()
		self.rect.center = (x,y)


	def draw(self):
		screen.blit(self.img, self.rect)

player = Soldier(200, 200, 3)
player2 = Soldier(400, 200, 3)



run = True
while run:




	player.draw()
	player2.draw()

	
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False


	pygame.display.update()

pygame.quit()