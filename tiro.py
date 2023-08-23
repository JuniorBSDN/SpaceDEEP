import random

import pygame
import math
import random

class Tiro(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/tiro.png") #seleção da imagem
        self.image = pygame.transform.scale(self.image, [30, 10]) #tamanho do objeto
        self.rect = self.image.get_rect()
        self.speed = 100

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left > 800:
            self.kill()
            print("kill")