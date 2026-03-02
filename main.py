from pipe import Pipe
from bird import Bird
from ground import Ground
import score
import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60

HEIGHT = 512
WIDTH = 288

def homePage(playing):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                playing = True
    return playing

def coliderPipe(bird, pipe, ground, stopPipe ,stopMouvePipe = True):
    if bird.collition(ground.rect) or bird.collition(pipe.rect_bottom) or bird.collition(pipe.rect_top):
        stopPipe = stopMouvePipe
        ground.stopAnimation()
        bird.death(ground.rect)
    if not stopPipe:
        pipe.move()

    return stopPipe

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    score.init_score_images()
    background = pygame.image.load("Img/background-day.png").convert()
    ground = Ground()

    stopPipe = False
    running = True
    playing = False
    listPipes = []

    bird = Bird()

    while running:
        clock.tick(fps)
        screen.blit(background, (0, 0))
              
        if playing:
            bird.move()
            ground.annimationGround()

            for event in pygame.event.get():
                if event.type == QUIT:
                    print("Quit page 111")
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        bird.jump()

            if not listPipes or listPipes[-1].rect_bottom.right < WIDTH - 150 :
                print(f"Nombre de pipe:{len(listPipes)}")
                listPipes.append(Pipe())
                
            for pipe in listPipes:
                pipe.addScore(bird)

                stopPipe = coliderPipe(bird, pipe, ground, stopPipe)

                if pipe.rect_bottom.right < -250:
                    listPipes.remove(pipe)
                pipe.draw(screen)

            score.printScore(bird.score, screen)
        else:
            playing = homePage(playing)
            
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Quit page")
                print(f"Final score: {bird.score}")
                running = False
        
        bird.draw(screen)
        bird.update_animation()
        ground.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()