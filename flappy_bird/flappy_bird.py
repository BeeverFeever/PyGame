import pygame as py
import sys
from pygame.locals import *


# Game methods

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (288, 512))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5


py.init()
screen = py.display.set_mode((576, 1024))
clock = py.time.Clock()

# Game variables
gravity = 0.25
bird_movement = 0

bg_surface = py.image.load('flappy_bird/assets/background-day.png')
bg_surface = py.transform.scale2x(bg_surface)

floor_surface = py.image.load('flappy_bird/assets/base.png')
floor_surface = py.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = py.image.load('flappy_bird/assets/bluebird-midflap.png')
bird_surface = py.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 512))

pipe_surface = py.image.load('flappy_bird/assests/pipe-red.png')
pipe_surface = py.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = py.USEREVENT
py.time.set_timer(SPAWNPIPE, 1200)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
                    
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                bird_movement = 0
                bird_movement -= 6

        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    
    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, (bird_rect))
    floor_x_pos -= 1
    
    draw_floor()

    if floor_x_pos <= -576:
        floor_x_pos = 0

    py.display.update()
    clock.tick(120)