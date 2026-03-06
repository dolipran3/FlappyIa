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
    elif score < 100:
        imageUnit = listImages[score % 10]
        imageDiz = listImages[score // 10]
        rectUnit = imageUnit.get_rect()
        rectDiz = imageDiz.get_rect()
        rectUnit.topleft = (132, 5)
        rectDiz.topleft = (rectUnit.left - rectDiz.width, 5)
        screen.blit(imageDiz, rectDiz)
        screen.blit(imageUnit, rectUnit)
    elif score < 1000:
        imageUnit = listImages[score % 10]
        imageDiz = listImages[(score // 10) % 10]
        imageCent = listImages[score // 100]
        rectUnit = imageUnit.get_rect()
        rectDiz = imageDiz.get_rect()
        rectCent = imageCent.get_rect()
        rectUnit.topleft = (132, 5)
        rectDiz.topleft = (rectUnit.left - rectDiz.width, 5)
        rectCent.topleft = (rectDiz.left - rectCent.width, 5)
        screen.blit(imageCent, rectCent)
        screen.blit(imageDiz, rectDiz)
        screen.blit(imageUnit, rectUnit)