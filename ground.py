import pygame

HEIGHT = 512

class Ground:
    def __init__(self):
        self.image = pygame.image.load("Img/base.png").convert()
        self.rect = self.image.get_rect()
        self.rectTop = pygame.Rect(0, -200, self.rect.width, 5) #TODO: A revoir, pas très propre.
        self.groundScroll = 0
        self.groundSpeed = 2
        self.rect.topleft = (self.groundScroll, HEIGHT - (self.rect.height// 1.3))

    def annimationGround(self):
        self.groundScroll -= self.groundSpeed 
        if self.groundScroll <= -48:
            self.groundScroll = 0
        self.rect.topleft = (self.groundScroll, HEIGHT - (self.rect.height// 1.3))

    def stopAnimation(self):
        self.groundSpeed = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)