import os, sys
import pygame
from pygame import * 
from pygame.locals import *

font.init()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
       image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', name)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def scrollText(text, font, color):
	try:
		mixer.music.load("data/music/IntroDialogue.ogg")
		mixer.music.play()
	except:
		pass

	try:
		text = text.decode('utf-8')
	except:
		pass

	try:
		color = Color(color)
	except:
		color = Color(*color)

	clock = time.Clock()

	screen = display.get_surface()
	screen_rect = screen.get_rect()
	bg = screen.copy()

	width, height = font.size(' ')
	Rright = screen_rect.centerx + width * 3
	Rleft = screen_rect.centerx - width * 3

	fullText = []
	for i, line in enumerate(text.splitlines()):
		rect = Rect((0, 0), font.size(line))
		rect.midtop = screen_rect.centerx, screen_rect.bottom + height * i
		fullText.append([line, rect, False])

	y = 0
	skip = False
	while fullText and not event.peek(QUIT):
		if skip:
			mixer.music.stop()
			break
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.KEYDOWN:
				skip = True
		event.clear()
		y -= 1
		for p in fullText[:]:
			r = p[1].move(0, y)
			if r.bottom < 0:
				fullText.pop(0)
				continue
			if not isinstance(p[0], Surface):
				if p[2]:
					font.set_underline(1)
				p[0] = font.render(p[0], 1, color)
				font.set_underline(0)
			screen.blit(p[0], r)
			if r.top >= screen_rect.bottom:
				break
		clock.tick(40)
		display.flip()
		screen.blit(bg, (0, 0))
	
	display.flip()
