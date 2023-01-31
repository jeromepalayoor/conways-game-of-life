import pygame 
import copy
import random

width,height = 1200,600
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Conway's Game of Life")

size = 15
start = False
grid = []
for x in range(width//size):
    grid.append([])
    for y in range(height//size):
        if x != 0 and x != width//size - 1 and y != 0 and y != height//size - 1:
            grid[x].append(random.choice((True,False)))
        else:
            grid[x].append(False)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start:
                    start = False
                else:
                    start = True
            if event.key == pygame.K_c:
                start = False
                grid = []
                for x in range(width//size):
                    grid.append([])
                    for y in range(height//size):
                        grid[x].append(False)

            if event.key == pygame.K_r:
                start = False
                grid = []
                for x in range(width//size):
                    grid.append([])
                    for y in range(height//size):
                        if x != 0 and x != width//size - 1 and y != 0 and y != height//size - 1:
                            grid[x].append(random.choice((True,False)))
                        else:
                            grid[x].append(False)

    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]

    if pressed:
        x = pos[0] // size
        y = pos[1] // size
        if x != 0 and x != width//size - 1 and y != 0 and y != height//size - 1:
            if not grid[x][y]:
                grid[x][y] = True
            else:
                grid[x][y] = False
    
    if start:
        grid_copy = copy.deepcopy(grid)
        for x in range(width//size):
            for y in range(height//size):
                n = 0
                if x != 0 and x != width//size - 1 and y != 0 and y != height//size - 1:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if grid_copy[x+i][y+j] and ((i,j) != (0,0)):
                                n += 1

                if grid[x][y]:
                    if n == 2 or n == 3:
                        grid[x][y] = True
                    else:
                        grid[x][y] = False
                else:
                    if n == 3:
                        grid[x][y] = True

    
    win.fill((255,255,255))

    for x in range(width//size):
        for y in range(height//size):
            if grid[x][y]:
                pygame.draw.rect(win,(0,0,100),(x*size,y*size,size,size))
            elif x == 0 or x == width//size-1 or y == 0 or y == height//size-1:
                pygame.draw.rect(win,(0,0,0),(x*size,y*size,size,size))
            else:
                pygame.draw.rect(win,(0,0,200),(x*size,y*size,size,size))

    for i in range(width//size):
        pygame.draw.line(win,(0,0,0),(i*size,0),(i*size,height))
    
    for i in range(height//size):
        pygame.draw.line(win,(0,0,0),(0,i*size),(width,i*size))

    pygame.display.update()

pygame.quit()
exit()