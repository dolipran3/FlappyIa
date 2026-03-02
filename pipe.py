import pygame
from random import randint

SPACE_BETWEEN_PIPES = 100
HEIGHT = 512
WIDTH = 288

class Pipe:
    def __init__(self):
        self.image = pygame.image.load("Img/pipe-green.png").convert_alpha()
        self.flipped_image = pygame.transform.flip(self.image, False, True)

        posY = randint(150, 400)

        # Bottom pipe
        self.rect_bottom = self.image.get_rect()
        self.rect_bottom.topleft = (288, posY)

        # Top pipe
        self.rect_top = self.image.get_rect()
        self.rect_top.bottomleft = (288, posY - SPACE_BETWEEN_PIPES)
        # Score zone
        self.rect_score = pygame.Rect(self.rect_top.right, self.rect_top.bottom, 10, SPACE_BETWEEN_PIPES)

        self.speed = -2

    def draw(self, screen):
        screen.blit(self.image, self.rect_bottom)
        screen.blit(self.flipped_image, self.rect_top)
        
        # pygame.draw.rect(screen, (255, 0, 0), self.rect_score)  # Draw the score zone for debugging

    def move(self):
        self.rect_bottom = self.rect_bottom.move(self.speed, 0)
        self.rect_top = self.rect_top.move(self.speed, 0)
        self.rect_score = self.rect_score.move(self.speed, 0)

    def addScore(self, bird):
        if bird.collition(self.rect_score):
            bird.score += 1
            self.rect_score.topleft = (-100, -100)  # Move the score zone out of the screen to prevent multiple scoring

    def setSpeed(self):
        self.speed = 0