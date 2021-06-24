import pygame
import random
import time

pygame.init()
colisao = pygame.mixer.Sound("assets/colisao-pymon.wav")
icone = pygame.image.load("assets/pikachu-icon.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("PyMon")

largura_tela = 1024
altura_tela = 646
tela = pygame.display.set_mode((largura_tela, altura_tela))
fps = pygame.time.Clock()

background = pygame.image.load("assets/fundo-1.png")

def texto_tela(texto, fonte):
    textSurface = fonte.render(texto, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def alert_tela(text):
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = texto_tela(text, fonte)
    TextRect.center = ((largura_tela/2), (altura_tela/2))
    tela.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    playGame()

def dead(letra):
    pygame.mixer.Sound.play(colisao)
    pygame.mixer.music.stop()
    alert_tela("A vogal " + letra + " atingiu você!!!")

def placar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, (1,1,1))
    tela.blit(texto, (0, 0))

def playGame():
    pygame.mixer.music.load('assets/trilha-sonora-pymon.mp3')
    pygame.mixer.music.play(-1)
    boneco_pikachu = pygame.image.load("assets/pikachu-boneco.png")
    posicao_x_pikachu = largura_tela * 0.50
    posicao_y_pikachu = altura_tela * 0.77
    pikachu_largura = 140
    movimentoX = 0

    letra_a = pygame.image.load("assets/vogais/a.png")
    letra_e = pygame.image.load("assets/vogais/e.png")
    letra_i = pygame.image.load("assets/vogais/i.png")
    letra_o = pygame.image.load("assets/vogais/o.png")
    letra_u = pygame.image.load("assets/vogais/u.png")

    largura_a = 57
    altura_a = 65
    xA = largura_tela * 0.45
    yA = -220
    velocidadeA = 3

    largura_e = 41
    altura_e = 68
    xE = largura_tela * 0.02
    yE = -100
    velocidadeE = 3

    largura_i = 18
    altura_i = 68
    xI = largura_tela * 0.20
    yI = -245
    velocidadeI = 3

    largura_o = 65
    altura_o = 69
    xO = largura_tela * 0.80
    yO = -80
    velocidadeO = 3

    largura_u = 51
    altura_u = 61
    xU = largura_tela * 0.65
    yU = -180
    velocidadeU = 3

    desvios = 0

    while True:
        for evento in pygame.event.get():  # evento get mostra na tela
            if evento.type == pygame.QUIT:
                pygame.quit()
                break
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    movimentoX = -8
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    movimentoX = 8
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        tela.blit(background, (0, 0))

        posicao_x_pikachu = posicao_x_pikachu + movimentoX
        if posicao_x_pikachu < 0:
            posicao_x_pikachu = 0
        elif posicao_x_pikachu > 880:
            posicao_x_pikachu = 880

        tela.blit(boneco_pikachu, (posicao_x_pikachu, posicao_y_pikachu))

        #---move
        tela.blit(letra_a, (xA, yA))
        yA = yA + velocidadeA
        if yA > altura_tela:
            yA = -200
            velocidadeA += 0.09
            xA = random.randrange(0, largura_tela)
            desvios += 1

        tela.blit(letra_e, (xE, yE))
        yE = yE + velocidadeE
        if yE > altura_tela:
            yE = -200
            velocidadeE += 0.09
            xE = random.randrange(0, largura_tela)
            desvios += 1

        tela.blit(letra_i, (xI, yI))
        yI = yI + velocidadeI
        if yI > altura_tela:
            yI = -10
            velocidadeI += 0.09
            xI = random.randrange(0, largura_tela)
            desvios += 1

        tela.blit(letra_o, (xO, yO))
        yO = yO + velocidadeO
        if yO > altura_tela:
            yO = -200
            velocidadeO += 0.09
            xO = random.randrange(0, largura_tela - 50)
            desvios += 1

        tela.blit(letra_u, (xU, yU))
        yU = yU + velocidadeU
        if yU > altura_tela:
            yU = -300
            velocidadeE += 0.09
            xU = random.randrange(0, largura_tela)
            desvios += 1

        if posicao_y_pikachu < yA + altura_a:
            if posicao_x_pikachu < xA and posicao_x_pikachu + pikachu_largura > xA or xA + largura_a > posicao_x_pikachu and xA + largura_a < posicao_x_pikachu + pikachu_largura:
                letra = "A"
                dead(letra)

        if posicao_y_pikachu < yE + altura_e:
            if posicao_x_pikachu < xE and posicao_x_pikachu + pikachu_largura > xE or xE + largura_e > posicao_x_pikachu and xE + largura_e < posicao_x_pikachu + pikachu_largura:
                letra = "E"
                dead(letra)

        if posicao_y_pikachu < yI + altura_i:
            if posicao_x_pikachu < xI and posicao_x_pikachu + pikachu_largura > xI or xI + largura_i > posicao_x_pikachu and xI + largura_i < posicao_x_pikachu + pikachu_largura:
                letra = "I"
                dead(letra)

        if posicao_y_pikachu < yO + altura_o:
            if posicao_x_pikachu < xO and posicao_x_pikachu + pikachu_largura > xO or xO + largura_o > posicao_x_pikachu and xO + largura_o < posicao_x_pikachu + pikachu_largura:
                letra = "O"
                dead(letra)

        if posicao_y_pikachu < yU + altura_u:
            if posicao_x_pikachu < xU and posicao_x_pikachu + pikachu_largura > xU or xU + largura_u > posicao_x_pikachu and xU + largura_u < posicao_x_pikachu + pikachu_largura:
                letra = "U"
                dead(letra)

        placar(desvios)
        pygame.display.update()
        fps.tick(60)

playGame()
print("Volte sempre")
