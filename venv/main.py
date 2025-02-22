# configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Da Cobrinha Python")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
# definindo variaveis que representam as cores (usando o padrão RGB) que serão usadas para tornar tudo mais organizado

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Parametros usados no jogo para definir o tamanho base da cobra e da comida e a velocidade que será rodada no jogo:

tamanho_quadrado = 10
velocidade_jogo = 10

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0

    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])

# a seguir uma função para retornar a nova movimentação da cobra a partir da tecla clicada, ou retornar None para não existir erro caso o usuario digite outra tecla
def selecionar_velocidade(tecla):
    velocidade_x = None
    velocidade_y = None

    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    # as velocidades abaixo servem como a mecanica usada para movimentar a cobra na tela baseado em um plano cartesiano.

    velocidade_x = 0 
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    # loop que roda até o jogador fazer algo que faça fim_jogo ser True.
    while not fim_jogo:
        tela.fill(preta)
        
        # realiza operações dependendo da tecla clicada
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                novas_velocidades = selecionar_velocidade(evento.key)
                if novas_velocidades[0] is not None and novas_velocidades[1]is not None:
                    velocidade_x, velocidade_y = novas_velocidades
                
        # desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posicao da cobra
        x += velocidade_x
        y += velocidade_y

        # quando houver colisão com parede teleportar a cobra para a outra extremidade
        if x >= largura:
            x = 0
        elif x < 0:
            x = largura - tamanho_quadrado
        if y >= altura:
            y = 0
        elif y < 0:
            y = altura - tamanho_quadrado
        
        # desenhar a cobra controlando seu tamanho
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # finalizar jogo se a cobra bater no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # desenhar a pontuacao do jogador
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        # atualizar a tela
        pygame.display.update()
        relogio.tick(velocidade_jogo)

        # Tela de "Game Over"
    tela.fill(preta)
    fonte = pygame.font.SysFont("Helvetica", 50)
    texto = fonte.render("Game Over", True, vermelha)
    tela.blit(texto, [largura // 2 - 100, altura // 2 - 25])
    pygame.display.update()

    # Esperar alguns segundos antes de fechar o jogo
    pygame.time.wait(3000)
# criar um loop infinito onde:

# 1 - desenha os objetos do jogo na tela:
# 1.1 - pontuação
# 1.2 - cobrinha
# 1.3 - comida

# 2 - cria a logica de terminar o jogo:
# 2.1 - quando a cobra bate na parede
# 2.2 - cobra bate em seu proprio corpo

# pega a interação com o usuario

rodar_jogo()