import pygame
import os 


#inicializando o pygame
pygame.init()

#Definindo o tamanho da tela
WIDTH, HEGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEGHT))
pygame.display.set_caption("Janela Simples")

#definindo a cor de fundo
BG_COLOR = (30, 30, 40) #cor de fundo (tom da imagem "RGB")

#carregando imagem
image_file = "player.png" #coloque o nome da imagem
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() #carregar imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEGHT // 2)) #centralizar imagem
else:
    print("Imagem não encontrada!")

#Loop prrincipal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #preecher o fundo
    screen.fill(BG_COLOR)

    #desenhar a imagem na tela
    screen.blit(img, img_rect.topflet)

    #atualizando a tela
    pygame.display.flip()

#Finalizar pygame
pygame.quit()