import pygame

# ----------------
# bota sort letra pega as letra var img
# ----------------
pygame.init()

# tamanho tela
largura = 1024
altura = 646
tela = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()

# ---CORES--VARS
background = pygame.image.load("assets/fundo-2.png")
boneco_pikachu = pygame.image.load("assets/pikachu-boneco.png")
posicaoX = largura * 0.50
posicaoY = altura * 0.77
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
xA = largura * 0.45
yA = -220
velocidadeA = 3

#----------E
largura_e = 80
altura_e = 95
xE = largura * 0.05
yE = -100
velocidadeE = 3
#----------I
#----------O
#----------U


while True:
    # interação do user
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

    # ------FUNDO
    tela.blit(background, (0, 0))

    # ------IMPEDE DE PASSAR DA PAREDE
    posicaoX = posicaoX + movimentoX
    if posicaoX < 0:
        posicaoX = 0
    elif posicaoX > 880:
        posicaoX = 880

    # ------POSIÇÃO DO PIKACHU
    tela.blit(boneco_pikachu, (posicaoX, posicaoY))

    # --------------,MOVIMENTAÇÃO A
    tela.blit(letra_a, (xA, yA))
    yA = yA + velocidadeA
    if yA > altura:
        yA = -200
        velocidadeA += 2

    #----------------MOVIMENTAÇÃO E
    tela.blit(letra_e, (xE, yE))
    yE = yE + velocidadeE
    if yE > altura:
        yE = -200
        velocidadeE += 1

    #------------------movimentação i
    tela.blit(letra_i, (400, 0))
    tela.blit(letra_o, (600, 0))
    tela.blit(letra_u, (800, 0))

    # atualiza tela
    pygame.display.update()
    fps.tick(60)  # espera 60 seg e volta no while
print("Volte sempre")
