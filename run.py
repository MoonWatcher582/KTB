import pygame, sys
from utils import *
from sprites import *
from pygame.locals import *
from random import randint

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
    prob = randint(0, 5)
    if prob == 1:
        return WERE_TYPE
    elif prob == 2:
        return VAMP_TYPE
    elif prob == 3:
        return TENGU_TYPE
    elif prob == 4:
        return LARS_TYPE
    else:
        return BASE_TYPE

def getSprite(currentBabyType):
    if currentBabyType == LARS_TYPE:
        return LARS
    elif currentBabyType == WERE_TYPE:
        return WEREBABY_PART
    elif currentBabyType == VAMP_TYPE:
        return VAMPBABY_PART
    else:
        return BASEBABY

def clickHandler(babyType, item, time, currMessage, gameOver):
    #print(currentBabyType)
    if gameOver:
        return currMessage, currentBabyType
    elif item == BASIN_ITEM:
        #print("Else if")
        if babyType == BASE_TYPE:
            time = 6
            return "You've saved this young one!", None
        else:
            #print("Else")
            time = -1
            gameOver = True
            return "You've given this beast our Goddess's protection! You monster!", currentBabyType
    elif item == GARLIC_ITEM:
        if babyType == VAMP_TYPE:
            time = 6
            return "It's a vampire!", None
        else:
            return "That's not it...", None
    elif item == STAKE_ITEM:
        if babyType == VAMP_TYPE:
            time = 6
            return "You killed it", None
        else:
            return "It wasn't a vampire and you staked it...", None
    elif item == RAZOR_ITEM:
        if babyType == LARS_TYPE:
            time = 6
            return "You shaved the unshaved!", None
        else:
            return "You're shaving something with no hair...", None
    return "Error", None

# Game loop
while True:
    if currentBabyType == None:
        currentBabyType = getNextBabyType()
        currentBabySprite = getSprite(currentBabyType)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # event.button means left-mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if BASIN.collidepoint(pos):
                message, currentBabyType = clickHandler(currentBabyType, BASIN_ITEM, time, message, gameOver)
            # HERE
            elif TOP_RIGHT.collidepoint(pos):
                message, currentBabyType = clickHandler(currentBabyType, GARLIC_ITEM, time, message, gameOver)
            elif CENTER_RIGHT.collidepoint(pos):
                message, currentBabyType = clickHandler(currentBabyType, STAKE_ITEM, time, message, gameOver)
            elif BOTTOM_RIGHT.collidepoint(pos):
                message, currentBabyType = clickHandler(currentBabyType, RAZOR_ITEM, time, message, gameOver)
            elif TOP_CENTER.collidepoint(pos):
                message, currentBabyType = clickHandler(currentBabyType, FISH_ITEM, time, message, gameOver)
        elif event.type == USEREVENT+1:
            if time >= 0:
                time -= 1
    pygame.display.update()
    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(currentBabySprite, (300, 300))
    if time == 0 and not gameOver:
        gameOver = True
        message = "The beasts claim this one!"
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(message, 1, (255, 0, 0))
        textpos = text.get_rect(centerx=DISPLAYSURF.get_width()/2)
        DISPLAYSURF.blit(text, textpos)
    #background.blit(GARLIC, (560, 20))
    pygame.draw.rect(background, (255, 0, 0, 0), TOP_RIGHT)
    pygame.draw.rect(background, (255, 255,  0, 0), CENTER_RIGHT)
    pygame.draw.rect(background, (255, 0, 0, 0), BOTTOM_RIGHT)
    pygame.draw.rect(background, (255, 0, 0, 0), TOP_CENTER)
    pygame.draw.rect(background, (255, 0, 0, 0), CENTER)
    pygame.draw.rect(background, (255, 0, 0, 0), BOTTOM_CENTER)
