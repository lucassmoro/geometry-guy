import pygame
from random import randint, choice

from mapa import Mapa
from menu import Menu
from player import Player
from superficie import Superficie

from sys import exit

pygame.init()

# janela e legenda
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Geometry Guy")

pygame.mixer.init()  # Inicializa o mixer de áudio
pygame.mixer.music.load("fnaf.mp3")

somMorte = pygame.mixer.Sound("dede.mp3")


# salva o recorde do player
recorde = 0
pontuacaoAtual = 0
# salva o tempo que o jogo comeca
tempoComeco = 0

# determina a velocidade das superficies
velocidadeSuperficies = 5
passoMudanca = 5

# grupos
player = pygame.sprite.GroupSingle()
player.add(Player())

# cria um grupo para as superficies
superficiesGrupo = pygame.sprite.Group() 

# variavel para ligar e desligar o jogo
jogoAtivado = False

# timer para criar as superficies
superficiesTimer = pygame.USEREVENT + 1
pygame.time.set_timer(superficiesTimer, 1250)

mapa = Mapa()
menu = Menu(screen)
# usando o sprite class podemos criar grupos e desenha-los na tela

# -------------- VARIAVEIS GLOBAIS NECESSSARIAS ACIMA --------------

# registra se houve alguma colisao
def colisao():
    if pygame.sprite.spritecollide(player.sprite, superficiesGrupo, False):
        superficiesGrupo.empty()
        somMorte.play()
        return True
    
    return False

while True:
    for event in pygame.event.get():  # neste for loop eh verificado todos os eventos
        if event.type == pygame.QUIT:  # verifica se QUIT foi acionado
            pygame.quit()
            exit()  # faz o display.update nao atualizar quando fechar o jogo
        
        if event.type == superficiesTimer:
            superficiesGrupo.add(Superficie())
    
    # pega a lista de teclas apertadas
    keys = pygame.key.get_pressed()
    
    if jogoAtivado:
        
        # pega uma lista das superficies do grupo
        listaSupperficies = superficiesGrupo.sprites()
        # esse for atualiza a velocidade
        for superficie in listaSupperficies:
            superficie.setVelocidade(velocidadeSuperficies)

        # pega a pontuacao do jogo
        pontuacaoAtual = pygame.time.get_ticks() // 1000 - tempoComeco
        
        # atualiza a velocidade das superficies com base na pontuacao (multiplos de 5)
        if pontuacaoAtual == passoMudanca and velocidadeSuperficies < 60:
            velocidadeSuperficies += 1
            passoMudanca += 5

        # desenho o mapa
        mapa.desenhar_mapa(screen, velocidadeSuperficies)

        # desenha e chama a funcao para atualizar o player
        player.draw(screen)
        player.update()

        superficiesGrupo.draw(screen)
        superficiesGrupo.update()
        
        #verifica a colisao com as superficies
        jogoAtivado = not colisao()
        
        # sai do jogo e vai para o menu
        if keys[pygame.K_ESCAPE]:
            jogoAtivado = False

        menu.mostrarTexto(f"PONTUACAO ATUAL: {pontuacaoAtual}", "white", 800, 550, 20)
    else:
        # registra se houve redorde
        if pontuacaoAtual > recorde:
            recorde = pontuacaoAtual
        
        # usa os metodos do objeto Menu para personalizar os textos do menu
        menu.corDeFundo("blue")
        menu.mostrarTexto("GEOMETRY GUY", "white", 500, 200, 60)
        menu.mostrarTexto("APERTE ENTER PARA JOGAR...", 'white', 500, 300, 20)
        menu.mostrarTexto(f"RECORDE: {recorde}", "white", 500, 340, 20)
        menu.mostrarTexto(f"PONTUACAO ATUAL: {pontuacaoAtual}", "white", 500, 360, 20)
        

        # pega o clique do espaco para comecar o jogo
        if keys[pygame.K_RETURN]:
            # pega o tempo que o jogador comeca
            tempoComeco = pygame.time.get_ticks() // 1000
            
            # zera a variavel da pontuacao atual
            pontuacaoAtual = 0

            # reinicia as variaveis
            passoMudanca = 5
            velocidadeSuperficies = 5

            # limpa os grupos
            player.empty()
            superficiesGrupo.empty()
            
            #reinicia o player para a posicao inicial
            player.add(Player())
            pygame.mixer.music.play(-1)
            
            jogoAtivado = True
            

    pygame.display.update()  # atualiza o display com as alteracoes feitas neste while
    pygame.time.Clock().tick(60)  # o while nao vai rodar mais do que 60 vezes por segundo
