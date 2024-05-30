import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.gravidade = 0

        # cria o corpo e pega o retangulo
        self.image = pygame.image.load('gg.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(midbottom=(200, 450))

        pygame.mixer.init()  # Inicializa o mixer de áudio
        self.somPulo = pygame.mixer.Sound("pulo.mp3")

    # permite o player pular apenas se estiver em cima de uma superficie
    def pulo(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.rect.bottom >= 450:
            self.gravidade = -18
            self.somPulo.play()
    
    def aplicarGravidade(self):
        self.gravidade += 1
        self.rect.y += self.gravidade
        if self.rect.bottom >= 450:
            self.rect.bottom = 450
    
    # sobrescrita de uma funcao do pygame
    def update(self):
        self.pulo()
        self.aplicarGravidade()