# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:33:05 2022

@author: Benny Mak
"""

#Mini Ex. 1

# import turtle

 

# t = turtle.Turtle("turtle")

# t.shape("triangle")

# t.pencolor("purple")

# t.fillcolor("orange")

# t.pensize(18)

# t.speed(9)

# t.begin_fill()

# for _ in range(4):

#     t.fd(100)

#     t.lt(90)

# t.end_fill()

# turtle.mainloop()

 

#Ex. 2 Turtle Race

# import turtle

# import random

 

 

 

# #Initialize Turtle

# player_one = turtle.Turtle()

# player_one.color("green")

# player_one.shape("turtle")

# player_one.penup()

# player_one.goto(-200,100)

# player_two = player_one.clone()

# player_two.color("blue")

# player_two.penup()

# player_two.goto(-200,-100)

 

# #Initialize goal point

 

# player_one.goto(300,60)

# player_one.pendown()

# player_one.circle(40)

# player_one.penup()

# player_one.goto(-200,100)

 

# player_two.goto(300,-140)

# player_two.pendown()

# player_two.circle(40)

# player_two.penup()

# player_two.goto(-200,-100)

 

 

# die = [1,2,3,4,5,6]

 

# for i in range(20):

#     if player_one.pos()>=(300,100):

#         print("Player One Wins!")

#         break

#     elif player_two.pos() >= (300,-100):

#         print("Player Two Wins!")

#         break

#     else:

#         player_one_turn = input("Press 'Enter' to roll the die.")

#         die_outcome = random.choice(die)

#         print("The die roll result is: ")

#         print(die_outcome)

#         print("The number of steps will be: ")

#         print(20*die_outcome)

#         player_two.fd(20*die_outcome)

#         player_two_turn = input("Press 'Enter' to roll the die.")

#         die_outcome = random.choice(die)

#         print("The die roll result is: ")

#         print(die_outcome)

#         print("The number of steps will be: ")

#         print(20*die_outcome)

#         player_two.fd(20*die_outcome)
# turtle.mainloop()

 

##Ex1. OOP

# class String:

#     def __init__(self,word):

#         self.word = word

       

#     def __add__(self,other):

#         return self.word+" - " + other

       

       

       

 

# STR = String("TM1117")

# print(STR+"PyGame")

 










 

#Ex. 1 Pygame Draw a Circle

# import pygame

 

# pygame.init()

# screen = pygame.display.set_mode([500,500])

 

# running = True

# while running:

 

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             running = False

           

#     screen.fill((255,255,255))

#     pygame.draw.circle(screen,(0,0,255),(250,250),75)

#     #circle(Surface,color,pos,radius,width)

 

#     pygame.display.flip()

   

# pygame.quit()

 

#Ex. 1 Display a rectangle on window

 

 

 

# import pygame

 

# pygame.init()

# SCREEN_WIDTH = 500

# SCREEN_HEIGHT = 500

 

# screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

# screen.fill((255,255,255))

# surf = pygame.Surface((50,50))

# surf.fill((0,0,0))

 

# rect = surf.get_rect()

# #Tracking the rect shape of surf object

 

# running = True

# while running:

 

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:

#             running = False

           

#     screen.blit(surf,(SCREEN_WIDTH/2-25,SCREEN_HEIGHT/2-25))

#     pygame.display.flip()

   

# pygame.quit()

 

 

#Ex.2 Create your first sprite

# import pygame

# from pygame.locals import *

 

 

 

# pygame.init()

 

 

# SCREEN_WIDTH = 800

# SCREEN_HEIGHT = 600

 

# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

 

# class Player(pygame.sprite.Sprite):

#     def __init__(self):

#         super(Player,self).__init__()

#         self.surf = pygame.Surface((75,25))

#         self.surf.fill((255,255,255))

#         self.rect = self.surf.get_rect()

       

# player = Player()

 

# running = True

# while running:

#     screen.fill((0,0,0))

#     screen.blit(player.surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

#     for event in pygame.event.get():

#         if event.type == QUIT:

#             running = False

#             break

       

#     pygame.display.flip()

# pygame.quit()

 

#Ex.3 Keyboard control of sprite

 

# import pygame

# from pygame.locals import *

 

# pygame.init()

 

# SCREEN_WIDTH = 800

# SCREEN_HEIGHT = 600

# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# clock = pygame.time.Clock()

# class Player(pygame.sprite.Sprite):

#     def __init__(self):

#         super(Player,self).__init__()

#         self.surf = pygame.Surface((75,25))

#         self.surf.fill((255,255,255))

#         self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2,

#                                                  SCREEN_HEIGHT/2))

#         self.speed = 5

#     def update(self,keys):

#         if keys[K_w]:

 

#             self.rect.move_ip(0,-self.speed)

           

#         elif keys[K_s]:

 

#             self.rect.move_ip(0,self.speed)

#         elif keys[K_a]:

 

#             self.rect.move_ip(-self.speed,0)

#         elif keys[K_d]:

 

#             self.rect.move_ip(self.speed,0)

# player = Player()

# running = True

# while running:

#     keys = pygame.key.get_pressed()

#     screen.fill((0,0,0))

#     screen.blit(player.surf,player.rect)

#     for event in pygame.event.get():

#         if event.type == QUIT:

#             running = False

#             break

#     pygame.display.flip()

#     player.update(keys)

#     clock.tick(30)

#     #Ensure program maintains a rate of 30 frames per second

# pygame.quit()

 

 

#Ex.4 Random-generated enemies

 

# import pygame

# from pygame.locals import *

# import random

# pygame.init()

# SCREEN_WIDTH = 800

# SCREEN_HEIGHT = 600

# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# clock = pygame.time.Clock()

# class Player(pygame.sprite.Sprite):

#     def __init__(self):

#         super(Player,self).__init__()

#         self.surf = pygame.Surface((75,25))

#         self.surf.fill((255,255,255))

#         self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2,

#                                                   SCREEN_HEIGHT/2))

#         self.speed = 5

#     def update(self,keys):

#         if keys[K_w]:

#             self.rect.move_ip(0,-self.speed)

#         elif keys[K_s]:

 

#             self.rect.move_ip(0,self.speed)

#         elif keys[K_a]:

 

#             self.rect.move_ip(-self.speed,0)

#         elif keys[K_d]:

 

#             self.rect.move_ip(self.speed,0)

#         if self.rect.left<0:

#             self.rect.left = 0

#         if self.rect.right>SCREEN_WIDTH:

#             self.rect.right = SCREEN_WIDTH

#         if self.rect.top <=0:

#             self.rect.top = 0

#         if self.rect.bottom>=SCREEN_HEIGHT:

#             self.rect.bottom = SCREEN_HEIGHT

           

# class Enemy(pygame.sprite.Sprite):

#     def __init__(self):

#         super(Enemy,self).__init__()

#         self.surf = pygame.Surface((20,10))

#         self.surf.fill((0,0,255))

#         self.rect = self.surf.get_rect(

#             center = (

#                 random.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100),

#                 random.randint(0,SCREEN_HEIGHT),

               

#                 )

#             )

#         self.speed = random.randint(5,20)

#     def update(self):

#         self.rect.move_ip(-self.speed,0)

#         if self.rect.right<0:

#             self.kill()        

# enemies = pygame.sprite.Group()

# all_sprites = pygame.sprite.Group()

# player = Player()

# ADDENEMY = pygame.USEREVENT+1

# pygame.time.set_timer(ADDENEMY,250) #250 in ms

           

# running = True

# while running:

#     keys = pygame.key.get_pressed()

#     screen.fill((0,0,0))

   

#     for entity in all_sprites:

#         screen.blit(entity.surf,entity.rect)

   

#     screen.blit(player.surf,player.rect)

#     for event in pygame.event.get():

#         if event.type == QUIT:

#             running = False

#             break

#         elif event.type == ADDENEMY:

#             new_enemy = Enemy()

#             enemies.add(new_enemy)

#             all_sprites.add(new_enemy)

           

#     pygame.display.flip()

#     player.update(keys)

#     clock.tick(30)

#     enemies.update()

#     #Ensure program maintains a rate of 30 frames per second

# pygame.quit()