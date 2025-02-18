# o codigo que está no main.py é esse: # configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Da cobrinha Python")
largura, altura = 600, 400
pygame.display.set_mode((largura, altura))

# definindo variaveis que representam as cores (usando o padrão RGB) que serão usadas para tornar tudo mais organizado

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Parametros da cobra
tamanho_quadrado = 10

# criar um loop infinito onde:

# 1 - desenha os objetos do jogo na tela:
# 1.1 - pontuação
# 1.2 - cobrinha
# 1.3 - comida

# 2 - cria a logica de terminar o jogo:
# 2.1 - quando a cobra bate na parede
# 2.2 - cobra bate em seu proprio corpo

# pega a interação com o usuario