from pipe import Pipe
from bird import Bird
from ground import Ground
from algoGenetique import AlgoGenetique
import score
import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 6000

HEIGHT = 512
WIDTH = 288

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    score.init_score_images()
    background = pygame.image.load("Img/background-day.png").convert()
    ground = Ground()

    running = True
    listPipes = []
    birds = [Bird() for _ in range(100)]
    genetiquePop = AlgoGenetique(populationSize=100, mutationRate=0.01, eliteRate=0.1)
    genetiquePop.initialiserPopulation()


    while running:
        clock.tick(fps)
        screen.blit(background, (0, 0))

        # Si au moins un oiseau est en vie, la partie continue. 
        if any(bird.alive for bird in birds):

            for bird in birds:
                bird.move()     
            ground.annimationGround()

            for event in pygame.event.get():
                if event.type == QUIT:
                    print("Quit page 111")
                    running = False

            if not listPipes or listPipes[-1].rect_bottom.right < WIDTH - 150 :
                print(f"Nombre de pipe:{len(listPipes)}")
                listPipes.append(Pipe())

            for bird,genPop in zip(birds, genetiquePop.population):
                dX, dY = bird.distanceToPipe(listPipes)
                if bird.alive:
                    genPop.fitness +=  1
                    if genPop.feedforward([dX, dY]) == 1:
                        bird.jump()
                    
            for pipe in listPipes:
                # pipe.addScore(bird)
                pipe.move()
                for bird in birds:
                    if bird.collition(pipe.rect_bottom) or bird.collition(pipe.rect_top) or bird.collition(ground.rect) or bird.collition(ground.rectTop):
                        bird.deathModel()

                    pipe.addScore(bird)
                if pipe.rect_bottom.right < -250:
                    listPipes.remove(pipe)
                pipe.draw(screen)

            score.printScore(max(bird.score for bird in birds), screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    print("Quit page")
                    print(f"Final score: {bird.score}")
                    running = False

            for bird in birds:
                if bird.alive:
                    bird.update_animation()
                    bird.draw(screen)

            ground.draw(screen)
            pygame.display.update()
        else:
            listPipes = []
            birds = [Bird() for _ in range(100)]
            genetiquePop.newGeneration()


if __name__ == "__main__":
    main()