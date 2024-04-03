import random
import pygame as pg
from klasser_og_objekter import *
from konstanter import *

# initierer pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

""" def draw_grid(): 
    for line in range(0,WIDTH // tile_size):
        pg.draw.line(surface, WHITE, (0, line* tile_size), (WIDTH, line * tile_size))
        pg.draw.line(surface, WHITE, (line * tile_size, 0), (line * tile_size, HEIGHT)) """


# Variabel som styrer om spillet skal kjøres
run = True

# Spill-løkken
while run:
    # Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)

    
    # Går gjennom hendelser (events)
    for event in pg.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False # Spillet skal avsluttes


    surface.fill(BLACK) 

    # draw_grid()

    world.draw()

    player1.update(world)
    player1.move()
    player1.draw()
        
    player2.update(world)
    player2.move()
    player2.draw()

    if player1.rect.x == tile_size * 15 and player1.rect.y == tile_size * 1.5: 
        print("Player 1 won!")
    
    

    """ if player1.rect.x == world_data[2][15]: 
        print("Player 1 wins")
    if player2.rect == world_data[2][15]: 
        print("Player 2 wins") """
    
    

    # "Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()

pg.quit()

# TO-DO 
# Startskjerm - https://www.youtube.com/watch?v=GMBqjxcKogA eller https://www.youtube.com/watch?v=deeetAQhMQU&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=8
# feller - https://www.youtube.com/watch?v=G8VsEbVS3F8&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=6
# motstandere maybe? - https://www.youtube.com/watch?v=ML2w92TIzoA&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=5
# Knapper som restart osv. https://www.youtube.com/watch?v=qNx5iuAUfes&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=7 
# Flere leveler - https://www.youtube.com/watch?v=pGC2lRAi65s&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=9 
# 

