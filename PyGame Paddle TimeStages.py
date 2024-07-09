import pygame
import time
pygame.font.init()

#Set Game Display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Test")

BG = pygame.transform.scale(pygame.image.load("./Media/Grassy.jpg"), (WIDTH, HEIGHT))

#Main Font
FONT = pygame.font.SysFont("comicsansms", 20) 

#Player Parameters
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 15
PLAYER_VEL = 5

#Ball Parameters
BALL_RADIUS = 10
BALL_VEL = 5
BALL_MAX_VEL = 10

#Draw on Display
def draw(player, elapsedTime, ball, stage):
    WIN.fill("sky blue")

    timeText = FONT.render(f"Time: {round(elapsedTime)}s", 1, "black")
    WIN.blit(timeText, (10, 10))

    stageText = FONT.render(f"Stage: {stage}", 1, "black")
    WIN.blit(stageText, (WIDTH - stageText.get_width() - 10, 10))

    pygame.draw.rect(WIN, "blue", player)

    pygame.draw.rect(WIN, "red", ball)

    pygame.display.update()

#Main Game
def main():
    run = True

    #Create Player
    paddle = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(0, 0, BALL_RADIUS*2, BALL_RADIUS*2)
    ballVelocity = BALL_VEL

    #Initial Direction of Ball Movement
    ballDirX = 1
    ballDirY = 1

    #Time Parameters
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    lastStageTime = startTime
    stageIncrementTime = 20

    timeIncrement = 0
    stage = 1

    #Main Loop
    while run:
        #For Framerate set to 60
        clock.tick(60)

        elapsedTime = time.time() - startTime
        currentTime = time.time()
        
        timeMultiplier = timeIncrement * stage
        timeIncrement = elapsedTime - timeMultiplier

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        if ballVelocity < BALL_MAX_VEL and (currentTime - lastStageTime >= stageIncrementTime):
            stage += 1
            ballVelocity += 0.5
            lastStageTime = currentTime
        


        #Ball Movement
        collision = pygame.Rect.colliderect(ball, paddle)
        if ball.x + (BALL_RADIUS*2) > WIDTH or ball.x < 0:
            ballDirX *= -1
        if ball.y < 0:
            ballDirY *= -1
        if collision:
            ballDirY *= -1
        ball.y += ballVelocity * ballDirY
        ball.x += ballVelocity * ballDirX

        

        #Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.x - PLAYER_VEL >= 0:
            paddle.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and paddle.x + paddle.width + PLAYER_VEL <= WIDTH:
            paddle.x += PLAYER_VEL

        if ball.y > HEIGHT:
            lostText = FONT.render("You lost!", 1, "black")
            WIN.blit(lostText, (WIDTH/2 - lostText.get_width()/2, HEIGHT/2 - lostText.get_width()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(paddle, elapsedTime, ball, stage)

    pygame.quit()

if __name__ == "__main__":
    main()
