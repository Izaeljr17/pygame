import pygame
import os 

#inicializando o pygame
pygame.init()

#Definindo o tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela Simples")

#definindo a cor de fundo
BG_COLOR = (30, 30, 40) #cor de fundo (tom da imagem "RGB")

#carregando imagem
image_file = "pygame-main\player.png" #coloque o nome da imagem
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() #carregar imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #centralizar imagem
else:
    print("Imagem não encontrada!")

#velocidade de movimento
SPEED = 1 #pixels por movimento

#funçao para centralizar a imagem conforme o tamanho da tela 
def centralize_imagem
    global img_rect, WIDTH, HEIGHT
    img_rect.center = WIDTH

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
        last_width, last_heigth = current_width, current_height

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

    #preecher o fundo
    screen.fill(BG_COLOR)

    #desenhar a imagem na tela
    screen.blit(img, img_rect.topflet)

    #atualizando a tela
    pygame.display.flip()

#Finalizar pygame
pygame.quit()