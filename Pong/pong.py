import pygame as py
import sys
import math
from pygame.locals import *
import random

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

left_paddle_speed = 0
right_paddle_speed = 5

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
        BallRestart()
    if ball.top <= 0 or ball.bottom >= wn_height:
        ball_speed_y *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle): 
        ball_speed_x *= -1

def LeftPaddleMovement():
    left_paddle.y += left_paddle_speed
    if left_paddle.top <= 0:
        left_paddle.top = 0
    if left_paddle.bottom >= wn_height:
        left_paddle.bottom = wn_height

def RigthPaddleMovement():
    if right_paddle.top < ball.y:
        right_paddle.top += right_paddle_speed
    if right_paddle.top > ball.y:
        right_paddle.top -= right_paddle_speed

    if right_paddle.top <= 0:
        right_paddle.top = 0
    if right_paddle.bottom >= wn_height:
        right_paddle.bottom = wn_height
    

def DrawShapes():
    py.draw.rect(screen, GREEN, left_paddle)
    py.draw.rect(screen, GREEN, right_paddle)
    py.draw.ellipse(screen, GREEN, ball)
    py.draw.aaline(screen, GREEN, (wn_width / 2, 0), (wn_width / 2, wn_height))

def BallRestart():
    ball.center = (wn_width / 2, wn_height / 2)

# game loop
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                left_paddle_speed += 7
            if event.key == py.K_UP:
                left_paddle_speed -= 7
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                left_paddle_speed -= 7
            if event.key == py.K_UP:
                left_paddle_speed += 7

    screen.fill(GREY)

    DrawShapes()
    BallMovement()
    LeftPaddleMovement()
    RigthPaddleMovement()

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    py.display.update()
    clock.tick(60)