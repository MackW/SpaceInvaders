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
            self.snake.move()
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()
            """ elif event.type == KEYDOWN:
               invaderMap=invaderMap"""
                        
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.snake = Invader()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
        
        """nNumHorizontal = int(self.width/64)
        nNumVertical = int(self.height/64)       
        self.pellet_sprites = pygame.sprite.Group()
        for x in range(nNumHorizontal):
            for y in range(nNumVertical):
                self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))  """       
 
class Invader(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    xdirection =1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('Invader_Row2.png',-1)
        self.pellets = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 5
        self.y_dist = 5 
        
    def move(self):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 1;
        yMove = 0;
        xdirection=1
        if self.rect.right <=0:
            xdirection=1
        elif self.rect.right >= 950: 
            xdirection=-1   
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove*xdirection,yMove); 
 
 
        
if __name__ == "__main__":
    MainWindow = SInvaders()
    MainWindow.MainLoop()