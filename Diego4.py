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

font = pygame.font.SysFont('Calibri', 25)

class Ennemi:
    pass


# DÉBUT
import random

ennemi_rouge = Ennemi()  # on crée un objet de type ennemi
ennemi_rouge.x = random.randint(0,700-25)
ennemi_rouge.y = random.randint(0+45,500-25)
ennemi_rouge.taille = 25
ennemi_rouge.couleur = ROUGE
# on peut mettre d'autres variables à l'ennemi


ennemi_noir = Ennemi()
ennemi_noir.x = random.randint(0, 700-35)
ennemi_noir.y = random.randint(0, 500-35)
ennemi_noir.taille = 35
ennemi_noir.vie = 4
ennemi_noir.sens = 1
ennemi_noir.couleur = NOIR

ennemis = [ennemi_noir, ennemi_rouge]

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
    
    epee = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 32:
                epee = 1
            
    # TICK
    pressed = pygame.key.get_pressed()
    #vie = vie - 0.2
    
    
    
    if ennemi_noir.sens == 1:
        ennemi_noir.x = ennemi_noir.x+5
    else:
        ennemi_noir.x = ennemi_noir.x-5
    if ennemi_noir.x >= 700-35:
        ennemi_noir.sens = -1
    elif ennemi_noir.x <= 0:
        ennemi_noir.sens = 1 
    
    if vie < 0:
        vie = 0
        
    if pressed[pygame.K_RIGHT]: 
        perso_x = perso_x + 5
    if pressed[pygame.K_LEFT]: 
        perso_x = perso_x- 5         
    if pressed[pygame.K_DOWN]: 
        perso_y = perso_y + 5
    if pressed[pygame.K_UP]: 
        perso_y = perso_y - 5
        
    if perso_x < 0:
        perso_x = 0   
    elif perso_x > 700-40:
        perso_x = 700-40
    if perso_y < 0:
        perso_y = 0
    elif perso_y > 500-40:
        perso_y = 500-40
    
    # COLLISIONS
    if collision(perso_x, perso_y, 40, 40, ennemi_rouge.x, ennemi_rouge.y, ennemi_rouge.taille, ennemi_rouge.taille):
        vie = vie - 2
    if collision(perso_x, perso_y, 40, 40, ennemi_noir.x, ennemi_noir.y, ennemi_noir.taille, ennemi_noir.taille):
        vie = vie - 2
       
    
    epee_x = perso_x + 40
    epee_y = perso_y - 10
    if epee == 1:
        if collision(epee_x, epee_y, 25,60, ennemi_noir.x, ennemi_noir.y, ennemi_noir.taille, ennemi_noir.taille):
            ennemi_noir.vie -= 2  # a = a + 2 -> a += 2
    
    
    if ennemi_noir.vie  <= 0:
        ennemi_noir.x = random.randint(0, 700-35)
        ennemi_noir.y = random.randint(0, 500-35)   
        vie = vie + 20
        ennemi_noir.vie  = 2
   
        
    # DESSIN
    ecran.fill(BLANC)
    
    if vie > 100:
        COULEUR = VERT
    #if vie == 125 or vie<125 and vie> 60:
    #if vie == 125 or (vie<125 and vie> 60):  # équivalent
    #if (vie == 125 or vie<125) and vie> 60:  # différent
    if vie <= 125 and vie> 60:
        COULEUR = JAUNE
    if vie<= 60 and vie>= 0:
        COULEUR = ROUGE    
    
    pygame.draw.rect(ecran, COULEUR, [20,20,vie,25])
    pygame.draw.rect(ecran, BLEU, [perso_x,perso_y,40,40])
    
    pygame.draw.rect(ecran, ennemi_rouge.couleur, [ennemi_rouge.x ,ennemi_rouge.y, ennemi_rouge.taille, ennemi_rouge.taille])
    pygame.draw.rect(ecran, ennemi_noir.couleur, [ennemi_noir.x, ennemi_noir.y, ennemi_noir.taille, ennemi_noir.taille])
    
    image_hp_enemy = font.render("HP enemy : " + str(ennemi_noir.vie), True, NOIR)  # str = string = text
    ecran.blit(image_hp_enemy, [0,0])
    
    if epee == 1:
        pygame.draw.rect(ecran, ROUGE, [epee_x, epee_y,25,60])
    
        
    pygame.display.flip()
    
    sys.stdout.flush()
    
    clock.tick(60)
    
pygame.quit()