import pygame as py
import sys
import math
from pygame.locals import *

# inititalisation
py.init()

# clock
clock = py.time.Clock()

# RGB colours
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

# game variables
ball_speed_x = 7
ball_speed_y = 7

# set up window
wn_width = 1000
wn_height = 650
screen = py.display.set_mode((wn_width, wn_height))
py.display.set_caption("Pong")

# make shapes 
ball = py.Rect(wn_width / 2 - 15, wn_height / 2 - 15, 30, 30)
left_paddle = py.Rect(wn_width - 20, wn_height / 2 - 70, 10, 140)
right_paddle = py.Rect(10, wn_height / 2 - 70, 10, 140)   

# methods
def BallMovement():
    global ball_speed_x, ball_speed_y

    if ball.left <= 0 or ball.right >= wn_width:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= wn_height:
        ball_speed_y *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle): 
        ball_speed_x *= -1

def DrawShapes():
    py.draw.rect(screen, GREEN, left_paddle)
    py.draw.rect(screen, GREEN, right_paddle)
    py.draw.ellipse(screen, GREEN, ball)

# game loop
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    screen.fill(GREY)

    BallMovement()
    DrawShapes()

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    py.display.update()
    clock.tick(60)