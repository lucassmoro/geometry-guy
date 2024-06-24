import pygame

class Mapa():
    def __init__(self):
        self.colagens=1000
        self.velocidade = 0

        self._chao = pygame.image.load("ground.png").convert_alpha()
        self._retanguloChao = self._chao.get_rect(topleft=(0, 450))
        
        self._ceu = pygame.image.load("ceu.png").convert_alpha()
        self._retanguloCeu = self._ceu.get_rect(bottomleft=(0, 450))

    def getComprimentoChao(self):
        return self._chao.get_width()
    
    def getChao(self):
        return self._chao
    
    def desenhar_mapa(self, screen, velocidade):
        self.velocidade += velocidade
        for i in range(self.colagens):
            screen.blit(self._ceu, (self._ceu.get_width() * i - self.velocidade, 0))
        for i in range(self.colagens):
            screen.blit(self._chao, (self._chao.get_width() * i - self.velocidade, 450))

    def getRetanguloChao(self):
        return self._retanguloChao

    def getCeu(self):
        return self._ceu

    def getRetanguloCeu(self):
        return self._retanguloCeu