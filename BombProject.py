# Write this before you press play in the terminal
# cd '/Users/leomi/OneDrive/Documents/Unity Games/HistoryProject/Assets/'

import pygame
import time
import math

start_time = time.time()

seconds = 2.1
JumpCount = 10


# Intialize the pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Background Color
screen.fill((255, 0, 0))


# Title and Icon
pygame.display.set_caption("Bomb Project")
icon = pygame.image.load('bird.png')
pygame.display.set_icon(icon)

# Players
playerImg = pygame.image.load('worker.png')
playerX = 370
playerY = 480


BackgroundImg = pygame.image.load('background.jpg')
BackgroundX = 0
BackgroundY = 0

PortalImg = pygame.image.load('portal.png')
portalX = 700
portalY = 480

PortalImg2 = pygame.image.load('portal2.png')
portalX2 = 10000
portalY2 = 10000



def player(x, y):
    screen.blit(playerImg, (x, y))


def Background(x, y):
    screen.blit(BackgroundImg, (x, y))


def portal(x, y):
    screen.blit(PortalImg, (x, y))


def portal2(x, y):
    screen.blit(PortalImg2, (x, y))


# Collision Unit w/ Portal and Player


def isCollision(portalX, portalY, playerX, playerY):
    distance = math.sqrt((math.pow(portalX - playerX, 2)) +
                         (math.pow(portalY - playerY, 2)))
    if distance < 32:
        return True




Player_XCord = playerY

# Game Loop
running = True
while running:

    Player_XCord = playerY

    Running3 = True

    # Background Color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        # Exit Window
        if event.type == pygame.QUIT:
            running = False

        # Player Movemnet
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_time = time.time()

                Running2 = True
                move = None

                while Running2:

                    event_while_jump = pygame.event.poll()
                    if event_while_jump.type == pygame.KEYDOWN:
                        if event_while_jump.key == pygame.K_LEFT:
                            move = "left"
                        if event_while_jump.key == pygame.K_RIGHT:
                            move = "right"
                    if event_while_jump.type == pygame.KEYUP:
                        move = None

                    current_time = time.time()
                    elapsed_time = current_time - start_time

                    print(elapsed_time)
                    print(Player_XCord)

                    if JumpCount >= -10:
                        neg = 1
                        if JumpCount < 0:
                            neg = -1
                        playerY -= (JumpCount ** 2) * 0.5 * neg
                        JumpCount -= 1
                        # Is player moving left or right?
                        if move:
                            if move == "left":
                                playerX -= 5
                            if move == "right":
                                playerX += 5
                        time.sleep(0.065)
                        
                    if JumpCount == -11:
                        JumpCount = 10
                        playerY = Player_XCord
                        Running2 = False
                    


                    screen.fill((0, 0, 0))  
                    Background(BackgroundX, BackgroundY)
                    portal(portalX, portalY)
                    player(playerX, playerY)
                    pygame.display.update()

                    time.sleep(.001)

                    if elapsed_time > seconds:
                        print("Jump Loop Done")
                        playerY = Player_XCord
                        Running2 = False



            if event.key == pygame.K_LEFT:
                while pygame.event.poll().type != pygame.KEYUP:
                    pygame.time.wait(60)
                    playerX -= 5
                    

                    # Place Everything Here in the While Loop

                    collision = isCollision(portalX, portalY, playerX, playerY)
                    if collision:
                        playerX = 100
                        playerY = 480 

                        BackgroundX = 1100
                        BackgroundY = 1100

                        portalX = 1100
                        portalY = 1100

                        portalX2 = 60
                        portalY2 = 480

                    if portalX2 == 60 and playerX > 0 and playerX < 100:
                        portalX2 = 1100
                        portalY2 = 1100

                        portalX = 700
                        portalY = 480

                        playerX = 670
                        playerY = 480

                        BackgroundX = 0
                        BackgroundY = 0

                    Background(BackgroundX, BackgroundY)
                    player(playerX, playerY)
                    portal(portalX, portalY)
                    portal2(portalX2, portalY2)

                    pygame.display.update()
                    screen.fill((0, 0, 0))



            if event.key == pygame.K_RIGHT:
                while pygame.event.poll().type != pygame.KEYUP:
                    pygame.time.wait(60)
                    playerX += 5
                    Right_Running = True

                    # Place Everything Here in the While Loop

                    collision = isCollision(portalX, portalY, playerX, playerY)
                    if collision:
                        playerX = 100
                        playerY = 480 

                        BackgroundX = 1100
                        BackgroundY = 1100

                        portalX = 1100
                        portalY = 1100

                        portalX2 = 60
                        portalY2 = 480
                    
                    if portalX2 == 60 and playerX > 0 and playerX < 100:
                        portalX2 = 1100
                        portalY2 = 1100

                        portalX = 700
                        portalY = 480

                        playerX = 670
                        playerY = 480

                        BackgroundX = 0
                        BackgroundY = 0

                    else:
                        Right_Running = False


                    # Place Sprites Here
                    Background(BackgroundX, BackgroundY)
                    player(playerX, playerY)
                    portal(portalX, portalY)
                    portal2(portalX2, portalY2)

                    pygame.display.update()  
                    screen.fill((0, 0, 0))    
    # More collision - Portal2 and Player collision  
    if portalX2 == 60 and playerX > 0 and playerX < 100:
        portalX2 = 1100
        portalY2 = 1100

        portalX = 700
        portalY = 480

        playerX = 670
        playerY = 480

        BackgroundX = 0
        BackgroundY = 0
        
    # Collision - Portal and Player collision
    collision = isCollision(portalX, portalY, playerX, playerY)
    if collision:
        playerX = 100
        playerY = 480 

        BackgroundX = 1100
        BackgroundY = 1100

        portalX = 1100
        portalY = 1100

        portalX2 = 60
        portalY2 = 480
    
    # Place Sprites Here
    Background(BackgroundX, BackgroundY)

    portal2(portalX2, portalY2)

    portal(portalX, portalY)

    player(playerX, playerY)
    
    pygame.display.update()
            
