import pygame

class Menu():
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def corDeFundo(self, cor: str):
        self.screen.fill(f'{cor}')

    def mostrarTexto(self, texto: str, cor: str, posicaoX: int, posicaoY: int, tamanho: int):
        fonte = pygame.font.Font("fonte.ttf", tamanho)
        texto = fonte.render(f'{texto}', True, f'{cor}')
        textoRetangulo = texto.get_rect(center=(posicaoX, posicaoY))
        self.screen.blit(texto, textoRetangulo)