import pygame
import os 

#inicializando o pygame
pygame.init()

#Definindo o tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Janela Simples")

#definindo a cor de fundo
BG_COLOR = (30, 30, 40) #cor de fundo (tom da imagem "RGB")

#carregando imagem
image_file = "player.png" #coloque o nome da imagem
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() #carregar imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #centralizar imagem
else:
    print("Imagem não encontrada!")

#velocidade de movimento
SPEED = 2 #pixels por movimento
JUMP_STRENGTH = 20 #FORÇA DO PULO
GRAVITY = 0.3 #gravidade para fazer o personagem cair 
JUNPING = False #indica se o personagem esta no ar 
VELOCITY_Y = 0 #velocidade no eixo Y

#funçao para centralizar a imagem conforme o tamanho da tela 
def centralize_imagem():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)

#variaveis para controle de redirecionamento
last_width, last_height = WIDTH, HEIGHT

#limite de movimento para que o personagem nao saia de tela
def limit_moviment():
    global img_rect, WIDTH, HEIGHT
    #limita a posição da imagem para não sair da tela
    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH
    if img_rect.top < 0:
        img_rect.top = 0
    if img_rect.bottom > HEIGHT:
        img_rect.bottom = HEIGHT

#função para realizar o pulo
def jump():
    global VELOCITY_Y, JUNPING
    if not JUNPING:
        VELOCITY_Y = -JUMP_STRENGTH #inicia o pulo para cima
        JUNPING = True

#função para atualizar o movimento do pulo
def update_jump():
    global VELOCITY_Y, JUNPING, img_rect
    if JUNPING:
        VELOCITY_Y += GRAVITY #simula gravidade
        img_rect.y += VELOCITY_Y #atualiza a função y de personagem

        #se o personagem estiver tocando o chão novamente, para o pulo
        if img_rect.bottom >= HEIGHT:
            img_rect.bottom = HEIGHT #garanta que o personagem nã passe o chão
            JUNPING = False
            VELOCITY_Y = 0 #reseta a velocidade Y

#Loop prrincipal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #verifica se o tamanho da janela foi alterada
    current_width, current_height = screen.get_size()

    #se a janela foi redimencionada, centralizada a imagem
    if current_width != last_width or current_height != last_height:
        WIDTH, HEIGHT = current_width, current_height
        centralize_imagem() #centralize a imagem quando a janela mudar de tamanho
        last_width, last_height = current_width, current_height

    #pega as teclas precionadas
    keys = pygame.key.get_pressed()

    #movimentação da imagem
    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED #move para a esquerda
    if keys[pygame.K_RIGHT]: 
        img_rect.x += SPEED #Move para a direita
    if keys[pygame.K_UP]: 
        img_rect.y -= SPEED #move para cima
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED #move para baixo

    #pulo
    if keys[pygame.K_SPACE]:
        jump() #ativa o pulo
    
    #limite de movimento para não sair da tela
    limit_moviment()

    #atualiza a fisica do pulo
    update_jump()

    #preecher o fundo
    screen.fill(BG_COLOR)

    #desenhar a imagem na tela
    screen.blit(img, img_rect.topflet)

    #atualizando a tela
    pygame.display.flip()

#Finalizar pygame
pygame.quit()