

import random
import pygame
from nave import Nave
from alien import Alien
from tiro import Tiro



#inicializando meu pygame
pygame.init()
display = pygame.display.set_mode([800,600]) #tamanho do display
pygame.display.set_caption("SPACEDEEP")

#VARIAVEIS DO JOGO
#Groups
objectGroup = pygame.sprite.Group()
Meteorito1Group = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()

#Background(plano de fundo)
fundo = pygame.sprite.Sprite(objectGroup)
fundo.image = pygame.image.load("dados/galax.jpg")
fundo.image = pygame.transform.scale(fundo.image,[800,640])
fundo.rect = fundo.image.get_rect()


nave = Nave(objectGroup)

#musica
pygame.mixer.music.load("dados/son/virus.wav")
pygame.mixer.music.play(-1)

#sounds - tiro
shoot = pygame.mixer.Sound("dados/son/laser.mp3")



#logica do jogo
gameLoop = True
gameover = False
timer = 0
clock = pygame.time.Clock()

if __name__=="__main__":
    while gameLoop:
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shoot.play()
                    newTiro = Tiro(objectGroup,tiroGroup)
                    newTiro.rect.center = nave.rect.center

#update LOGIC:
        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.5:
                    newMeteorito1 = Alien(objectGroup,Meteorito1Group)

            collisions = pygame.sprite.spritecollide(nave,Meteorito1Group,False,pygame.sprite.collide_mask)

            if collisions:
                print("game over")
                gameover = True

                #colocar uma cena de game over

            hits = pygame.sprite.groupcollide(tiroGroup,Meteorito1Group,True,True)



#DRAW:
        display.fill([255, 172, 100])  # cor do plano de fundo
        objectGroup.draw(display)
        pygame.display.update()