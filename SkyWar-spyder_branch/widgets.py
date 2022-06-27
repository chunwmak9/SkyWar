# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:53:33 2022

@author: ic2140
"""
import pygame


class Button:
    def __init__(self,x,y,sw,sh,text):
    
        self.surf  = pygame.Surface((60,40), pygame.SRCALPHA)
        self.surf.fill((0,0,0))
        self.font =  pygame.font.SysFont(None, 22)
        self.font.render(text,False)