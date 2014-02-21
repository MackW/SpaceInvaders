'''
Created on Feb 20, 2014

@author: mack
'''

import os
import pygame
from pygame.locals import RLEACCEL

def load_image(name, colorkey=None):
    fullname = os.path.join('', 'Images')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
        