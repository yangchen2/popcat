import pygame
import os

pygame.init()
screen = pygame.display.set_mode((950//2, 1074//2))

# load images
assests_path = os.path.join(os.path.dirname(__file__), "assests" )

img_open_mouth = pygame.image.load(assests_path+"/open_mouth.png")
img_open_mouth.convert()
img_open_mouth = pygame.transform.rotozoom(img_open_mouth,0,0.5)


img_closed_mouth = pygame.image.load(assests_path+"/closed_mouth.png")
img_closed_mouth.convert()
img_closed_mouth = pygame.transform.rotozoom(img_closed_mouth,0,0.5)

screen.blit(img_closed_mouth,img_closed_mouth.get_rect())   

popSound = pygame.mixer.Sound(assests_path+"/pop.wav")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            screen.blit(img_closed_mouth,img_closed_mouth.get_rect())
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(img_open_mouth,img_open_mouth.get_rect())
            popSound.play()

                
    pygame.display.update()

pygame.quit()

