from pygame import *
from utils import scrollText


def intro():
	display.set_mode((800, 500))

	text = """In a distant hamlet, the village priest prepares the rites.
	As he knows, the Fertility Goddess has promised prosperity
	so long as each hamlet baby is quickly baptized in her name.

	Without the ritual protection of the Goddess wrought through baptism
	each newborn is vulnerable to be claimed by the monsters of the forest.
	Indeed, many are claimed before they reach the holy waters.

	A claimed child is lost to the wood; redemption is impossible.
	Letting the beast grow would be to put the children of the Goddess
	in grave danger.

	Therefore, even if it means the priest must sacrifice his precious soul,



	He must...




	KILL THE BABY"""

	fnt = font.Font("Roboto-MediumItalic.ttf", 20)
	color = 0xa0a0a000

	scrollText(text, fnt, color)

