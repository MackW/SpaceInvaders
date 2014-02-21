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
    currentFrame=0

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
        clock=pygame.time.Clock()
        self.LoadSprites()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            
            self.Invaders_sprites.clear(self.screen,self.background)
            self.Invaders.move()
            self.Invaders_sprites.draw(self.screen)
            pygame.display.flip()
            """ elif event.type == KEYDOWN:
               invaderMap=invaderMap"""
            clock.tick(10)
                        
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.Invaders = Invader()
        self.Invaders_sprites = pygame.sprite.RenderPlain((self.Invaders))
        self.Invaders = Invader()
        self.Invaders_sprites = pygame.sprite.RenderPlain((self.Invaders))
 
class Invader(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.images=[]
        self.images.append(load_image('Row3Open.png',-1))
        self.images.append(load_image('Row3Closed.png',-1))
        self.image = self.images[0]
        self.rect=self.image.get_rect()
        self.xdirection =0
        self.currentFrame = 0
        
    def move(self):
        self.currentFrame=0 if self.currentFrame==1 else 1
        self.image = self.images[self.currentFrame]
        xMove = 10;
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