import pygame
import time
import random
pygame.font.init()

#Set Game Display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paddle Ball Game")

#Main Font
FONT = pygame.font.SysFont("comicsansms", 20) 

#Paddle Parameters
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_MIN_VEL = 7
PADDLE_DEF_COLOUR = "blue"

#Ball Parameters
BALL_RADIUS = 10
BALL_VEL = 5
BALL_MAX_VEL = 10
BALL_DEF_COLOUR = "red"

class Paddle(pygame.Rect):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()


class Ball(pygame.Rect):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

class Block(pygame.Rect):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def ballColl(ball, block):
        return 

def draw(player, ball, elapsedTime, stage, score):
    WIN.fill("sky blue")

    timeText = FONT.render(f"Time: {round(elapsedTime)}s", 1, "black")
    WIN.blit(timeText, (10, 10))

    stageText = FONT.render(f"Stage: {stage}", 1, "black")
    WIN.blit(stageText, (WIDTH - stageText.get_width() - 10, 10))

    scoreText = FONT.render(f"Score: {score}", 1, "black")
    WIN.blit(scoreText, (WIDTH - scoreText.get_width() - 10, stageText.get_height() + 10))

    pygame.draw.rect(WIN, PADDLE_DEF_COLOUR, player)

    pygame.draw.rect(WIN, BALL_DEF_COLOUR, ball)

    pygame.display.update()

def main():
    run = True
    
    paddle = Paddle(200, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(0, 0, BALL_RADIUS*2, BALL_RADIUS*2)

    #Time Parameters
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    lastStageTime = startTime
    stageIncrementTime = 10

    timeIncrement = 0
    stage = 1

    #Block Init
    blocks = []
    stageBlocks = 0

    #Init Score
    score = 0

    #Main Loop
    while run:
        #For Framerate set to 60
        clock.tick(60)

        elapsedTime = time.time() - startTime
        currentTime = time.time()
        
        #Increase Time Between Stages
        timeMultiplier = timeIncrement * stage
        timeIncrement = elapsedTime - timeMultiplier

    #For quitting game on pressing cross button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    draw(player=paddle, ball=ball, elapsedTime=elapsedTime, stage=stage, score=score)

if __name__ == "__main__":
    main()
