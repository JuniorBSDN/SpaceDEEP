import random

import pygame
import math
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/alien.png") #seleção da imagem
        self.image = pygame.transform.scale(self.image, [100, 80]) #tamanho do objeto
        self.rect = pygame.Rect(25, 25, 50, 50)

        self.rect.x = 1000+random.randint(1, 400)
        self.rect.y = random.randint(1, 400)
        self.speed = 1 + random.random()*2

    def update(self, *args):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
            print("kill")

