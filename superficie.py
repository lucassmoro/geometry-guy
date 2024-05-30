import pygame
from random import randint, choice

class Superficie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # velocidade da superficie
        self.velocidade = 10

        # declarando os atributos
        altura = choice([450, 425, 400, 420, 450, 450])
        
        tamanho = choice([40, 50, 45])
        
        self.image = pygame.image.load("triangulo.png").convert_alpha()
        
        if altura != 450:
            self.image = pygame.transform.rotate(self.image, 90)
        
        self.image = pygame.transform.scale(self.image, (tamanho, tamanho))

        self.rect = self.image.get_rect(midbottom=(1000, altura))
    
    def update(self):
        # move a superficeie para esquerda
        self.rect.x -= self.velocidade
        # destroi a superficie se passsar da borda da esquerda
        if self.rect.x == -50:
            self.destruirObjeto()
    
    def setVelocidade(self, valor):
        self.velocidade = valor

    def destruirObjeto(self):
        self.kill()
    
    def getRect(self):
        return self.rect
    