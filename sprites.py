import pygame
from utils import *

# Set the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 593))

# Load in all sprites
# Baby Types
BASEBABY = load_image("base-baby.png")
LARS = load_image("lars-baby.png")
WEREBABY_FULL = load_image("werebaby.png")
WEREBABY_PART = load_image("were-detected.png")
VAMPBABY_FULL = load_image("vampbaby.png")
VAMPBABY_PART = load_image("vamp-detected.png")
TENGUBABY_FULL = load_image("tengubaby.png")
TENGUBABY_PART = load_image("tengu-detected.png")

# Monster Parts
BABY_FANGS = load_image("fang-baby.png")
BABY_NOSE = load_image("big-nose-baby.png")
BABY_EYES = load_image("red-eye-baby.png")

# Items
BRAIN = load_image("images/brain.png")
DECAP = load_image("images/decapitation.png")
EXTING = load_image("images/fire-extinguisher.png")
FISH = load_image("images/fish.png")
SWAT = load_image("images/fly-swatter.png")
GARLIC = load_image("images/garlic.png")
GOAT = load_image("images/goat.png")
WATER = load_image("images/holy-water.png")
MIRROR = load_image("images/mirror.png")
RAZOR = load_image("images/razor.png")
RICE = load_image("images/rice.png")
SALT = load_image("images/salt.png")
BULLET = load_image("images/silver-bullet.png")
STAKE = load_image("images/stake.png")

