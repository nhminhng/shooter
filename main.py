import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int (0.8 * SCREEN_WIDTH)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minh\'s Shooter')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False

#define color
BG_COLOR = (125,125,125)

def draw_bg():
	screen.fill(BG_COLOR)


class Soldier(pygame.sprite.Sprite):
	def __init__(self, char_type, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.direction = 1
		self.char_type = char_type
		self.flip = False
		img = pygame.image.load(f'Assets/img/{self.char_type}/Idle/0.png')
		self.img = pygame.transform.scale(img, ( int(img.get_width() * scale), int(img.get_height() * scale)))
		self.rect = self.img.get_rect()
		self.rect.center = (x,y)
		self.speed = speed


	def move(self, moving_left, moving_right):

		#reset movement variables
		dx, dy = 0, 0

		#assign movement variables if moving left or right
		if moving_left:
			dx = -self.speed
			self.flip = True
			self.direction = -1
		if moving_right:
			dx = self.speed
			self.flip = False
			self.direction = 1

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy


	def draw(self):
		screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)
 
player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 200, 3, 5)

run = True
while run:

	clock.tick(FPS)

	draw_bg()
	player.draw()
	enemy.draw()

	player.move(moving_left, moving_right)
	
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#keyboard presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = True
			if event.key == pygame.K_d:
				moving_right = True

			if event.key == pygame.K_ESCAPE:
				run = False

		#keyboard releases
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				moving_left = False
			if event.key == pygame.K_d:
				moving_right = False






	pygame.display.update()

pygame.quit()