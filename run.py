import pygame, sys
from utils import *
from pygame.locals import *
from random import randint

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

# Constants
BASIN_ITEM = 0
GARLIC_ITEM = 1
STAKE_ITEM = 2
FISH_ITEM = 3
SILVER_ITEM = 4
SILVERBULLET_ITEM = 5
RAZOR_ITEM = 6

BASE_TYPE = 0
WERE_TYPE = 1
VAMP_TYPE = 2
TENGU_TYPE = 3
LARS_TYPE = 4

# Vars
gameOver = False
currentBabySprite = BASEBABY
currentBabyType = None
message = ""
time = 6
pygame.time.set_timer(USEREVENT+1, 1000)

# Decide if next baby is normal, or a monster
def getNextBabyType():
	prob = randint(0, 9)
	if prob < 4:
		return LARS_TYPE
	else:
		return BASE_TYPE

def getSprite(babyType):
	if currentBabyType == LARS_TYPE:
		return LARS 
	else:
		return BASEBABY

def clickHandler(babyType, item, time, currMessage, gameOver):
	if gameOver:
		return currMessage
	elif item == BASIN_ITEM:
		if babyType == BASE_TYPE:
			time = 6
			return "You've saved this young one!"
		else:
			time = -1
			gameOver = True
			return "You've given this beast our Goddess's protection! You monster!"

# Game loop
while True:
	if currentBabyType == None:
		currentBabyType = getNextBabyType()
		currentBabySprite = getSprite(currentBabyType)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			if BASIN.collidepoint(pos):
				message = clickHandler(currentBabyType, BASIN_ITEM, time, message, gameOver)
		elif event.type == USEREVENT+1:
			if time >= 0:
				time -= 1
	pygame.display.update()
	DISPLAYSURF.blit(background, (0, 0))
	DISPLAYSURF.blit(currentBabySprite, (300, 300))
	if time == 0:
		gameOver = True
		message = "The beasts claim this one!"
	if pygame.font:
		font = pygame.font.Font(None, 36)
		text = font.render(message, 1, (255, 0, 0))
		textpos = text.get_rect(centerx=DISPLAYSURF.get_width()/2)
		DISPLAYSURF.blit(text, textpos)
