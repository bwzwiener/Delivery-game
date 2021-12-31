import pygame,sys
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Boxboy')
mult = 5
size = (256*mult,144*mult)
world = (256,144)
screen = pygame.display.set_mode(size)

##def load_map
##    file = open("map.txt",'r')
##    
##    file.close()
##    
##def pick_sprite
##
##def draw_world




##load_map()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ##draw_world()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
