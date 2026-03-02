import pygame

listImages = []

def init_score_images():
    global listImages
    listImages = [
        pygame.image.load("Img/0.png").convert_alpha(),
        pygame.image.load("Img/1.png").convert_alpha(),
        pygame.image.load("Img/2.png").convert_alpha(),
        pygame.image.load("Img/3.png").convert_alpha(),
        pygame.image.load("Img/4.png").convert_alpha(),
        pygame.image.load("Img/5.png").convert_alpha(),
        pygame.image.load("Img/6.png").convert_alpha(),
        pygame.image.load("Img/7.png").convert_alpha(),
        pygame.image.load("Img/8.png").convert_alpha(),
        pygame.image.load("Img/9.png").convert_alpha(),
    ]
def printScore(score, screen):
    if score < 10:
        image = listImages[score]
        rectUnit = image.get_rect()
        rectUnit.topleft = (132, 5)
        screen.blit(image, rectUnit)