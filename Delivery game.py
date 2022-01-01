import pygame,sys
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Boxboy')
mult = 5
size = (256*mult,144*mult)
world = pygame.Surface((256,144))
screen = pygame.display.set_mode(size)

##def load_map
##    file = open("map.txt",'r')
##    
##    file.close()
##    
##def pick_sprite
##
def draw_world(game_map, screen):
    world.fill((173,216,230))

    grass = pygame.image.load('grass.png')
    dirt = pygame.image.load('dirt.png')


    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] == 1:
                world.blit(grass,(x*16,y*16))
            elif game_map[y][x] == 2:
                world.blit(dirt,(x*16,y*16))

    screen.blit(pygame.transform.scale(world,(256*5,144*5)),(0,0))

game_map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,1,0,1,0,1,1,0,0,0,2],
            [2,0,1,1,0,1,2,1,2,1,2,2,1,1,1,2],
            [2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]



##load_map()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_world(game_map, screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
