import pygame
import time
pygame.font.init()

#Set Game Display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

#Main Font
FONT = pygame.font.SysFont("comicsansms", 15) 

#Player Parameters
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 10
PLAYER_VEL = 5

import pygame
import time
pygame.font.init()

#Set Game Display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Test")

#Main Font
FONT = pygame.font.SysFont("comicsansms", 20) 

#Player Parameters
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 15
PLAYER_VEL = 5

#Ball Parameters
BALL_RADIUS = 10
BALL_VEL = 5

#Draw on Display
def draw(player, elapsedTime, ball):
    WIN.fill("sky blue")

    timeText = FONT.render(f"Time: {round(elapsedTime)}s", 1, "black")
    WIN.blit(timeText, (10, 10))

    pygame.draw.rect(WIN, "blue", player)

    pygame.draw.rect(WIN, "red", ball)

    pygame.display.update()

#Main Game
def main():
    run = True

    
    #Create Player
    paddle = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(0, 0, BALL_RADIUS*2, BALL_RADIUS*2)

    #Initial Direction of Ball Movement
    ballDirX = 1
    ballDirY = 1

    #Time Parameters
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0

    #Main Loop
    while run:
        #For Framerate set to 60
        clock.tick(60)

        elapsedTime = time.time() - startTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        #Ball Movement
        collision = pygame.Rect.colliderect(ball, paddle)
        if ball.x + (BALL_RADIUS*2) > WIDTH or ball.x < 0:
            ballDirX *= -1
        if ball.y < 0:
            ballDirY *= -1
        if collision:
            ballDirY *= -1
        ball.y += BALL_VEL * ballDirY
        ball.x += BALL_VEL * ballDirX

        

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

        draw(paddle, elapsedTime, ball)

    pygame.quit()

if __name__ == "__main__":
    main()
