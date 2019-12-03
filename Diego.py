#!coding: utf-8
from __future__ import print_function, division

import pygame, sys
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
JAUNE = [255, 255, 0]

# DÉBUT
import random
random.randint(0+45,700-25)
R = random.randint(0,700-25)
S = random.randint(0+45,500-25)

T = random.randint(0, 700-35)
G = random.randint(0, 500+35)
sens_carre = 1

vie = 250
perso_x = 100
perso_y = 100

def collision(x1,y1,l1,h1, x2,y2,l2,h2):
    if x1+l1 > x2 and x1 < x2+l2 and y1+h1 > y2 and y1 < y2+h2:
        return True
    else:
        return False
    

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            pass # print(event.key)
        if event.type == pygame.KEYDOWN:
            ...
    # TICK
    pressed = pygame.key.get_pressed()
    vie = vie - 1
    if sens_carre == 1:
        T = T+5
    else:
        T = T-5
    if T >= 700-35:
        sens_carre = -1
    elif T <= 0:
        sens_carre = 1 
    
    if vie < 0:
        vie = 0
    if vie > 100:
        COULEUR = VERT
    #if vie == 125 or vie<125 and vie> 60:
    #if vie == 125 or (vie<125 and vie> 60):  # équivalent
    #if (vie == 125 or vie<125) and vie> 60:  # différent
    if vie <= 125 and vie> 60:
        COULEUR = JAUNE
    if vie<= 60 and vie>= 0:
        COULEUR = ROUGE
        
    if pressed[pygame.K_RIGHT]: #1073741903]:
        perso_x = perso_x + 5
    if pressed[pygame.K_LEFT]: #1073741904]:
        perso_x = perso_x- 5         
    if pressed[pygame.K_DOWN]: # 1073741905]:
        perso_y = perso_y + 5
    if pressed[pygame.K_UP]: # 1073741906]:
        perso_y = perso_y - 5
    if perso_y < 0:
        perso_y = 0   
    elif perso_x > 700-40:
        perso_x = 700-40
    if perso_y < 0:
        perso_y = 0
    elif perso_y > 500-40:
        perso_y = 500-40
    
    # COLLISIONS
    # if (b < R+25 or b == R+25) and (b > R-40 or b == R-40) :
    #if b <= R+25 and b >= R-40 and c <= S+25 and c >= S-40:
    #    a = a - 2
    if collision(perso_x, perso_y, 40, 40, R,S,25,25):
        vie = vie - 2
    if collision(perso_x, perso_y, 40, 40, T,G,35,35):
        vie = vie - 2    
        
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, COULEUR, [20,20,vie,25])
    pygame.draw.rect(ecran, BLEU, [perso_x,perso_y,40,40])
    pygame.draw.rect(ecran, ROUGE, [R,S,25,25])
    pygame.draw.rect(ecran, NOIR, [T,G,35,35])
    
    pygame.display.flip()
    
    sys.stdout.flush()
    
    clock.tick(60)
    
pygame.quit()