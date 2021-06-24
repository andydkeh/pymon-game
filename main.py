import pygame
import random

pygame.init()
icone = pygame.image.load("assets/pikachu-icon.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("PyMon")


arrayPala = ["lala", "lele"]

# tamanho tela
largura_tela = 1024
altura_tela = 646
tela = pygame.display.set_mode((largura_tela, altura_tela))
fps = pygame.time.Clock()

background = pygame.image.load("assets/fundo-1.png")

#---MOSTRA PIKACHU
boneco_pikachu = pygame.image.load("assets/pikachu-boneco.png")
posicao_x_pikachu = largura_tela * 0.50
posicao_y_pikachu = altura_tela * 0.77
movimentoX = 0

# ------VARS ALFA
letra_a = pygame.image.load("assets/vogais/a.png")
letra_e = pygame.image.load("assets/vogais/e.png")
letra_i = pygame.image.load("assets/vogais/i.png")
letra_o = pygame.image.load("assets/vogais/o.png")
letra_u = pygame.image.load("assets/vogais/u.png")

#-------A---------
largura_a = 80
altura_a = 88
xA = largura_tela * 0.45
yA = -220
velocidadeA = 3

#----------E
largura_e = 80
altura_e = 95
xE = largura_tela * 0.05
yE = -100
velocidadeE = 3

#----------I
largura_i = 80
altura_i = 83
xI = largura_tela * 0.20
yI = -245
velocidadeI = 3

#----------O
largura_o = 80
altura_o = 86
xO = largura_tela * 0.80
yO = -80
velocidadeO = 3

#----------U
largura_u = 80
altura_u = 73
xU = largura_tela * 0.60
yU = -180
velocidadeU = 3


while True:
    for evento in pygame.event.get():  # evento get mostra na tela
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        # ------MOVIMENTO TECLAS
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                movimentoX = -8
            elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                movimentoX = 8
        # ------PAROU DE CLICAR
        if evento.type == pygame.KEYUP:
            movimentoX = 0

    #------FUNDO
    tela.blit(background, (0, 0))

    # ------IMPEDE DE PASSAR DA PAREDE
    posicao_x_pikachu = posicao_x_pikachu + movimentoX
    if posicao_x_pikachu < 0:
        posicao_x_pikachu = 0
    elif posicao_x_pikachu > 880:
        posicao_x_pikachu = 880

    # ------POSIÇÃO DO PIKACHU
    tela.blit(boneco_pikachu, (posicao_x_pikachu, posicao_y_pikachu))

    # --------------,MOVIMENTAÇÃO A
    tela.blit(letra_a, (xA, yA))
    yA = yA + velocidadeA
    if yA > altura_tela:
        yA = -200
        velocidadeA += 0.09
        xA = random.randrange(0, largura_tela)

    #----------------MOVIMENTAÇÃO E
    tela.blit(letra_e, (xE, yE))
    yE = yE + velocidadeE
    if yE > altura_tela:
        yE = -200
        velocidadeE += 0.09
        xE = random.randrange(0, largura_tela)

    #------------------movimentação I
    tela.blit(letra_i, (xI, yI))
    yI = yI + velocidadeI
    if yI > altura_tela:
        yI = -10
        velocidadeI += 0.09
        xI = random.randrange(0, largura_tela)

    #-----------------MOVIMENTAÇÃO O
    tela.blit(letra_o, (xO, yO))
    yO = yO + velocidadeO
    if yO > altura_tela:
        yO = -200
        velocidadeO += 0.09
        xO = random.randrange(0, largura_tela-50)

    #-----------------MOVIMENTAÇÃO U
    tela.blit(letra_u, (xU, yU))
    yU = yU + velocidadeU
    if yU > altura_tela:
        yU = -300
        velocidadeE += 0.09
        xU = random.randrange(0, largura_tela)

    # atualiza tela
    pygame.display.update()
    fps.tick(60)  # espera 60 seg e volta no while
print("Volte sempre")
