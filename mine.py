import pygame
from pygame.locals import *
pygame.init()

mw = pygame.display.set_mode((700,500))
sprite = pygame.image.load("rocket.png")
sprite = pygame.transform.scale(sprite, (70, 70))
mw.blit(sprite, (100, 100))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


sprite_x = 100
sprite_y = 100

pygame.mixer.music.load("mazelov.ogg")
pygame.mixer.music.play(-1)

mw = pygame.display.set_mode((700,500))

background = pygame.image.load("galaxy.png")
background = pygame.transform.scale(background, (700, 800))
pygame.display.set_caption('Genshin Shooter')

mw.blit(sprite, (sprite_x, sprite_y))
class Enemy(GameSprite):
    def update(self):
        self.rect.y - self.rect.y+ self.speed
        if self.rect.y >= 500:
            self.rect.y = 50

imageEnemy = pygame.image.load('ufo.png')

enemy = Enemy(350, 50 ,50, 50, imageEnemy,5)


# class Player(GameSprite):




clock = pygame.time.Clock()
FPS = 30

game = True
finish = False

while game:
    mw.blit(background, (0,0))
    mw.blit(sprite,(0,0))
    enemy.reset()
    enemy.update


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False


    pygame.display.update()
    clock.tick(FPS)
