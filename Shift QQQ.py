#!coding: utf-8
from __future__ import print_function, division

def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT
a=100
b=100
r=5
sens=1 

QQQ = 97
SHIFT = 304

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == SHIFT:
                r = 30

        elif event.type == pygame.KEYUP:
            print("La touche relachée numero", event.key)
            if event.key == SHIFT:
                r = 5
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            print("Clic en", event.pos[0], event.pos[1])
            b = event.pos[0]       
    # TICK
    pressed = pygame.key.get_pressed()
    if pressed[QQQ]:
        b = b - r 
    if b < 20:
        b = 20
    if pressed[100]:
        b = b + r
    buttons = pygame.mouse.get_pressed() 
    if sens ==1:
        a=a+5
    else:
        a=a-5
    if a > 700:
        sens = -1
        print(sens,a)
    elif a < 0:
        sens = +1
        print(sens,a)
   
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [a,120, 20,40])
    pygame.draw.circle(ecran, BLEU, [b,200], 20)
    pygame.draw.circle(ecran, VERT, [a, 120], 10)
    pygame.draw.circle(ecran, VERT, [a, 160], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()