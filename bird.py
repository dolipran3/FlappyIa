import pygame
from pygame.locals import *

class Bird:
    def __init__(self):
        self.listImages = [
            pygame.image.load("Img/redbird-upflap.png").convert_alpha(),
            pygame.image.load("Img/redbird-midflap.png").convert_alpha(),
            pygame.image.load("Img/redbird-downflap.png").convert_alpha()
        ]
        self.animationIndex = 0
        self.image = self.listImages[self.animationIndex]
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 200)
        self.speed = 0
        self.gravity = 0.19
        self.noJump = False
        self.angle = 0
        self.jumpStrength = -4.5
        self.alive = True
        self.score = 0

        self.animationCounter = 0
        self.animationSpeed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.speed += self.gravity
        self.rect.y += int(self.speed)
    
        # Calculer l'angle (limité entre -45 et 90)
        if self.alive:
            self.angle = min(max(-self.speed * 10, -45), 135)
        
        # Appliquer la rotation à l'image actuelle
        self.image = pygame.transform.rotate(self.listImages[self.animationIndex], self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update_animation(self):
        if self.alive:
            self.animationCounter += 1
            if self.animationCounter >= self.animationSpeed:
                self.animationCounter = 0
                self.animationIndex = (self.animationIndex + 1) % len(self.listImages)
                self.image = self.listImages[self.animationIndex]
            
    def jump(self):
        if not self.noJump:
            self.speed = self.jumpStrength

    def collition(self, targetRect):
        return self.rect.colliderect(targetRect)

    def death(self, ground):
        self.noJump = True
        if self.rect.colliderect(ground):
            self.alive = False
            self.gravity = 0
            self.speed = 0