import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super().__init__(*groups)

        self.image = pygame.image.load("dados/star.png")
        self.image = pygame.transform.scale(self.image, [200,30])
        self.rect = pygame.Rect(25, 25, 50, 50)

        self.speed = 0
        self.acceleration = 0.4


    def update(self, *args):
        keys = pygame.key.get_pressed()

        #logica
        if keys[pygame.K_a]:
            self.rect.x -= 4
        elif keys[pygame.K_d]:
            self.rect.x += 4

        else:
            self.speed *= 0.600

        self.rect.y += self.speed

        if keys[pygame.K_w]:
            self.rect.y -= 4
        elif keys[pygame.K_s]:
            self.rect.y += 4
"""
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 800:
            self.rect.bottom = 800
"""