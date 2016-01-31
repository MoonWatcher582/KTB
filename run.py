import pygame, sys
from utils import *
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 593))
pygame.display.set_caption("Kill the Baby!")
background = load_image("KTBbackground2.png")
BASIN = pygame.Rect((20, 391), (250, 180))

# Load Sprites
BASEBABY = load_image("base-baby.png")
LARS = load_image("lars-baby.png")
WEREBABY_FULL = load_image("werebaby.png")
WEREBABY_PART = load_image("were-detected.png")
VAMPBABY_FULL = load_image("vampbaby.png")
VAMPBABY_PART = load_image("vamp-detected.png")
TENGUBABY_FULL = load_image("tengubaby.png")
TENGUBABY_PART = load_image("tengu-detected.png")

BABY_FANGS = load_image("fang-baby.png")
BABY_NOSE = load_image("big-nose-baby.png")
BABY_EYES = load_image("red-eye-baby.png")

currentBabySprite = BASEBABY

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			if BASIN.collidepoint(pos):
				print "FUUUUUUUUU"
	pygame.display.update()
	DISPLAYSURF.blit(background, (0, 0))
	DISPLAYSURF.blit(currentBabySprite, (300, 300))

