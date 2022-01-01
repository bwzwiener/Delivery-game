import pygame,sys
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Boxboy')
mult = 5
size = (256*mult,144*mult)
world = pygame.Surface((256,144))
screen = pygame.display.set_mode(size)

class keyboard:
    def __init__(self):
        self.left = False
        self.right = False

def quit_game():
    pygame.quit()
    sys.exit()
    
def draw_world(game_map, screen, world, box, box_rect):
    world.fill((173,216,230))

    grass = pygame.image.load('grass.png')
    dirt = pygame.image.load('dirt.png')

    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] == 1:
                world.blit(grass,(x*16,y*16))
            elif game_map[y][x] == 2:
                world.blit(dirt,(x*16,y*16))

    draw_box(world, box, box_rect)

    screen.blit(pygame.transform.scale(world,(256*5,144*5)),(0,0))

def draw_box(world, box, box_rect):
    world.blit(box,box_rect)

def movement(box_rect, momentum, keys):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keys.left = True
                elif event.key == pygame.K_RIGHT:
                    keys.right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys.left = False
                elif event.key == pygame.K_RIGHT:
                    keys.right = False
        
    momentum[0] = 0
    if keys.right:
        momentum[0] = 1
    elif keys.left:
        momentum[0] = -1

    if box_rect.top < 128:
        momentum[1] = 1
    else:
        momentum[1] = 0

    box_rect.left += momentum[0]
    box_rect.top += momentum[1]

    return momentum



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
tiles = []
for y in range(len(game_map)):
    for x in range(len(game_map[0])):
        if (game_map[y][x] != 0):
            tiles.append(pygame.Rect(x*16,y*16,16,16))






box = pygame.image.load("Standing.png")
box_rect = box.get_rect()
momentum = [0,0]
keys = keyboard()

while True:  #Main Loop

    momentum = movement(box_rect, momentum, keys)
    draw_world(game_map, screen, world, box, box_rect)

    pygame.display.update()
    clock.tick(30)
