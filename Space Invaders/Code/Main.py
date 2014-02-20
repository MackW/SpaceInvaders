'''
Created on Feb 20, 2014

@author: mack
'''

import os, sys,random
import pygame
from pygame.locals import *
from Helpers import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class SInvaders:

    invaderMap =[[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

    def __init__(self, width=1024,height=768):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        
    def MainLoop(self):
        pygame.key.set_repeat(500, 30)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        self.DemoMode()
        while 1:          
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN and self.CheckForWin()==0:
                    """if self.KeyPressed(event.key) == 1:"""
             
            pygame.display.flip()

    def DemoMode(self):
        self.LoadSprites()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            self.Invaders.move()
            self.Invaders_sprites.clear(self.screen,self.background)
            self.Invaders_sprites.draw(self.screen)
            pygame.display.flip()
            """ elif event.type == KEYDOWN:
               invaderMap=invaderMap"""
                        
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.Invaders = Invader()
        self.Invaders_sprites = pygame.sprite.RenderPlain((self.Invaders))

 
class Invader(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('Invader_Row2.png',-1)
        self.image.set_colorkey((255,255,255))
        self.x_dist = 5
        self.y_dist = 5 
        self.xdirection =1
        
    def move(self):

        xMove = 5;
        yMove = 0;
        if self.rect.x <=0:
            self.xdirection=1
        elif self.rect.x >= 950: 
            self.xdirection=-1   
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove*self.xdirection,yMove); 
 
 
        
if __name__ == "__main__":
    MainWindow = SInvaders()
    MainWindow.MainLoop()