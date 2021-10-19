from typing import Text
import pygame , sys

from pygame import color

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping pong')

black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Kauan', True, white, black)
textRect = text.get_rect()
textRect.center = (screen_width/2 - 15, screen_height/2 -15)

velocidade_x = 3
velocidade_y = 3

while True:

    textRect.x += velocidade_x
    textRect.y += velocidade_y

    if textRect. top <= 0 or textRect.bottom >= screen_height:
        velocidade_y *= -1
    if textRect.left <= 0 or textRect.right >= screen_width:
        velocidade_x *= -1

    screen.fill(black)
    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)