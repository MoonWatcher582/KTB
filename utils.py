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

	lst = []
	for i, l in enumerate(text.splitlines()):
		a, b, c = l.partition('\\')
		u = False
		if a:
			if a.startswith('_') and a.endswith('_'):
				u = True
				a = a.strip('_')
			rect = Rect((0, 0), font.size(a))
			if b:
				rect.topright = Rleft, screen_rect.bottom + height * i
			else: 
				rect.midtop = screen_rect.centerx, screen_rect.bottom + height * i
			lst.append([a, rect, u])
		u = False
		if c:
			if c.startswith('_') and c.endswith('_'):
				u = True
				c = c.strip('_')
			rect = Rect((0, 0), font.size(c))
			rect.topleft = Rright, screen_rect.bottom + height * i
			lst.append([c, rect, u])

	y = 0
	while lst and not event.peek(QUIT):
		event.clear()
		y -= 1
		for p in lst[:]:
			r = p[1].move(0, y)
			if r.bottom < 0:
				lst.pop(0)
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
