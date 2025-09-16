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
    img_rect = img.get_rect(midbottom=(WIDTH // 2, HEIGHT // 2)) #centralizar imagem
else:
    print("Imagem não encontrada!")
    img = None
    img_rect = pygame.Rect(WIDTH // 2, HEIGHT // - 50, 50, 50) #retangular padrão para evitar erros

#carregar a imagem do personagem alvo
target_file = "bola.png"
if os.path.exists(target_file):
    target_img = pygame.image.load(target_file).convert_alpha()
    target_rect = pygame.Rect(WIDTH // 2 + 200, HEIGHT - 50, 50, 50)

background_file = "background.png" #caminho para sua imagem de fundo
if os.path.exists(background_file):
    background_orig = pygame.image.load(background_file).convert()
    background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
else:
    background_orig = None
    background = None
    print("imagem de fundo não encontrada!")

#velocidade de movimento
SPEED = 2 #pixels por movimento
JUMP_STRENGTH = 20 #FORÇA DO PULO
GRAVITY = 0.3 #gravidade para fazer o personagem cair 
JUNPING = False #indica se o personagem esta no ar 
VELOCITY_Y = 0 #velocidade no eixo Y

#variaveis para o alvo chutado
target_velocity_x = 0
target_velocity_y = 0
target_jumping = False
target_gravity = GRAVITY


#funçao para centralizar a imagem conforme o tamanho da tela 
def centralize_imagem():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)

#variaveis para controle de redirecionamento
last_width, last_heigth = WIDTH, HEIGHT


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

#atualizar o pulo / queda do alvo chutando
def update_target_physics():
    global target_velocity_x, target_velocity_y,target_jumping, target_rect, target_gravity

    if target_jumping:
        target_velocity_y += target_gravity
        target_rect.x += target_velocity_x
        target_rect.y += target_velocity_y

        if target_rect.bottom >= HEIGHT:
            target_rect.bottom = HEIGHT
            target_jumping = False
            target_velocity_x = 0
            target_velocity_y = 0
        else:
            target_velocity_x *= 0.95

#função chutar o alvo 
def kick():
    global target_velocity_x, target_velocity_y, target_jumping, target_rect, img_rect

    dist_x = target_rect.centerx - img_rect.centerx
    dist_y = target_rect.centery - img_rect.centery
    distancia = (dist_x ** 2 + dist_y ** 2) ** 0,5

    if distancia < 150:
        target_velocity_x = 20 if dist_x > 0 else -20
        target_velocity_y = -20
        target_jumping = True

#Loop prrincipal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #verifica se o tamanho da janela foi alterada
    current_width, current_height = screen.get_size()
    if current_width != last_width or current_height != last_heigth:
        WIDTH, HEIGHT = current_width, current_height

        #manter personagens no chão 
        img_rect.bottom = HEIGHT
        target_rect.bottom = HEIGHT

        if background_orig:
            background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
        last_width, last_heigth = current_width, current_height

        #parei aq

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
    if keys[pygame.K_f]:
        kick()
    
    limit_moviment(img_rect)
    limit_moviment(target_rect)

  
    update_jump()
    update_target_physics()

    if background:
        screen.blit(background, (0, 0))

    else:
        screen.fill(BG_COLOR) #caso nao tenha fundo mantem a cor de fundo

    if img:
        screen.blit(img, img_rect.topleft)
    else:
        pygame.draw.rect(screen, (255, 0, 0), img_rect)

    if target_img:
        screen.blit(target_img, target_rect.topleft)
    else:
        pygame.draw.rect(screen, (0, 255, 0), target_rect)

   #atualizando a tela
    pygame.display.flip()

#Finalizar pygame
pygame.quit()