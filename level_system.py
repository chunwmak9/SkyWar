import pygame
import os
from pygame.locals import *

s_width = 500
s_height = 500
screen = pygame.display.set_mode([s_width,s_height])
DIR = os.getcwd()
pygame.init()
screen.fill((0, 0, 0))
class Token(pygame.sprite.Sprite):
    def __init__(self):
        super(Token, self).__init__()
        self.surf = pygame.image.load(DIR+"/level_token.png").convert()
        self.surf = pygame.transform.scale(self.surf,(200,200))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(0,s_height))

running = True
token = Token()
while running:

    screen.blit(token.surf, (0, s_height))
    pygame.display.update()
pygame.quit()
