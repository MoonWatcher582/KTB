import pygame, sys
from intro import intro
from utils import *
from sprites import *
from pygame.locals import *
from random import randint

intro()
DISPLAYSURF = pygame.display.set_mode((800, 593))
pygame.display.set_caption("Kill the Baby!")
background = load_image("KTBbackground2.png")
BASIN = pygame.Rect((20, 391), (250, 180))
TOP_RIGHT =     pygame.Rect((680, 20), (100, 100))
CENTER_RIGHT =  pygame.Rect((680, 220), (100, 100))
BOTTOM_RIGHT =  pygame.Rect((680, 420), (100, 100))
TOP_CENTER =    pygame.Rect((560, 20), (100, 100))
CENTER =        pygame.Rect((560, 220), (100, 100))
BOTTOM_CENTER = pygame.Rect((560, 420), (100, 100))

# Constants
BASIN_ITEM = 0
GARLIC_ITEM = 1
STAKE_ITEM = 2
FISH_ITEM = 3
SILVER_ITEM = 4
SWATTER_ITEM = 5
RAZOR_ITEM = 6

BASE_TYPE = 0
WERE_TYPE = 1
VAMP_TYPE = 2
TENGU_TYPE = 3
LARS_TYPE = 4

FULL_TIME = 6

# Vars
gameOver = False
currentBabySprite = BASEBABY
currentBabyType = None
message = ""
time = FULL_TIME
pygame.time.set_timer(USEREVENT+1, 1000)

# Decide if next baby is normal, or a monster
def getNextBabyType():
    prob = randint(0, 9)
    if prob == 0 or prob == 1:
        return WERE_TYPE
    elif prob == 3 or prob == 4:
        return VAMP_TYPE
    elif prob == 5 or prob == 6:
        return TENGU_TYPE
    elif prob == 2:
        return LARS_TYPE
    else:
        return BASE_TYPE

def getSprite(currentBabyType, time):
    if time == -1:
        if currentBabyType == LARS_TYPE:
            return LARS
        if currentBabyType == WERE_TYPE:
            return WEREBABY_FULL
        if currentBabyType == VAMP_TYPE:
            return VAMPBABY_FULL
        if currentBabyType == TENGU_TYPE:
            return TENGUBABY_FULL
        if currentBabyType == BASE_TYPE:
            prob = randint(0, 2)
            if prob == 0:
                return WEREBABY_FULL
            if prob == 1:
                return VAMPBABY_FULL
            if prob == 2:
                return TENGUBABY_FULL
    if currentBabyType == LARS_TYPE:
        return LARS
    elif currentBabyType == WERE_TYPE:
        if time > 4:
            return BASEBABY
        elif time > 2:
		   	return BABY_FANGS
        elif time > 0:
			   return WEREBABY_PART
        elif time == 0:
			   return WEREBABY_FULL
    elif currentBabyType == VAMP_TYPE:
        if time > 4:
            return BASEBABY
        elif time > 2:
            return BABY_FANGS
        elif time > 0:
            return VAMPBABY_PART
        elif time == 0:
			   return VAMPBABY_FULL
    elif currentBabyType == TENGU_TYPE:
        if time > 4:
            return BASEBABY
        elif time > 2:
		   	return BASEBABY
        elif time > 0:
			   return TENGUBABY_PART
        elif time == 0:
			   return TENGUBABY_FULL 
    else:
        return BASEBABY

def clickHandler(babyType, item, time, currMessage, gameOver):
    if gameOver:
        return currMessage, currentBabyType
    elif item == BASIN_ITEM:
        if babyType == BASE_TYPE:
            return "You've saved this young one!", FULL_TIME 
        else:
            return "You've given this beast our Goddess's protection! You monster!", -1 
    elif item == GARLIC_ITEM:
        if babyType == VAMP_TYPE:
            return "It's a vampire!", time
        else:
            return "The baby sniffs the garlic, wholly apathetic.", time
    elif item == STAKE_ITEM:
        if babyType == VAMP_TYPE:
            return "You've staked the vampire's heart!", FULL_TIME
        else:
            return "It wasn't a vampire and you staked it :(", time
    elif item == FISH_ITEM:
        if babyType == TENGU_TYPE:
            return "It's a tengu! It hates the fish so much it flees.", FULL_TIME
        else:
            return "The baby does not appreciate the smell of fish.", time
    elif item == SWATTER_ITEM:
        if babyType > 0:
            return "You hit the baby with a fly swatter. It cries.", time
    elif item == SILVER_ITEM:
        if babyType == WERE_TYPE:
            return "A silver bullet! You shoot the werewolf.", FULL_TIME
        elif babyType != BASE_TYPE:
            return "You've shot it, but it isn't a werewolf", time
        else:
            return "You've killed that baby ;-;", -1
    elif item == RAZOR_ITEM:
        if babyType == LARS_TYPE:
            return "You shaved its beard, the source of its power!", FULL_TIME
        elif babyType == BASE_TYPE:
            return "You attack the baby with the razor. What is wrong with you?", -1
        else:
            return "The baby sees your razor but shows no fear.", time
    return "Error", -1

# Game loop
while True:
    currentBabySprite = getSprite(currentBabyType, time)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # event.button means left-mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameOver:
            pos = pygame.mouse.get_pos()
            if BASIN.collidepoint(pos):
                message, time = clickHandler(currentBabyType, BASIN_ITEM, time, message, gameOver)
                if time == FULL_TIME:
                    currentBabyType = None
            # HERE
            elif TOP_RIGHT.collidepoint(pos):
                message, time = clickHandler(currentBabyType, GARLIC_ITEM, time, message, gameOver)
                if currentBabyType == VAMP_TYPE:
                    currentBabySprite = VAMPBABY_PART
            elif CENTER_RIGHT.collidepoint(pos):
                message, time = clickHandler(currentBabyType, STAKE_ITEM, time, message, gameOver)
                if time == FULL_TIME:
                    currentBabyType = None
            elif BOTTOM_RIGHT.collidepoint(pos):
                message, time = clickHandler(currentBabyType, RAZOR_ITEM, time, message, gameOver)
                if time == FULL_TIME:
                    currentBabyType = None
            elif TOP_CENTER.collidepoint(pos):
                message, time = clickHandler(currentBabyType, FISH_ITEM, time, message, gameOver)
                if time == FULL_TIME:
                    currentBabyType = None
            elif CENTER.collidepoint(pos):
                message, time = clickHandler(currentBabyType, SILVER_ITEM, time, message, gameOver)
                if time == FULL_TIME:
                    currentBabyType = None
            elif BOTTOM_CENTER.collidepoint(pos):
                message, time = clickHandler(currentBabyType, SWATTER_ITEM, time, message, gameOver)
                if time == FULL_TIME:
                    currentBabyType = None
        elif event.type == pygame.KEYDOWN and gameOver:
            message = "RESTART"
            gameOver = False
            time = FULL_TIME
        elif event.type == USEREVENT+1:
            if time >= 0:
                time -= 1
    if currentBabyType == None:
        currentBabyType = getNextBabyType()
    pygame.display.update()
    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(currentBabySprite, (300, 300))
    if time == 0:
        message = "The beasts claim this one!"
        time = -1
    if time == -1:
        gameOver = True
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(message, 1, (255, 0, 0))
        textpos = text.get_rect(centerx=DISPLAYSURF.get_width()/2)
        DISPLAYSURF.blit(text, textpos)
        if time > -1:
            text = font.render("Time: " + str(time), 1, (255, 0, 0))
            textpos = text.get_rect(centerx=50)
            DISPLAYSURF.blit(text, textpos)

    background.blit(FISH, TOP_CENTER)
    background.blit(GARLIC, TOP_RIGHT)
    background.blit(BULLET, CENTER)
    background.blit(STAKE, CENTER_RIGHT)
    background.blit(SWAT, BOTTOM_CENTER)
    background.blit(RAZOR, BOTTOM_RIGHT)
