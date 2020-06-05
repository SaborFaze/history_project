# Write this before you press play in the terminal
# cd '/Users/leomi/OneDrive/Documents/Unity Games/HistoryProject/Assets/'

import pygame
import time
import math
from pygame import mixer

start_time = time.time()

seconds = 2.1
JumpCount = 10


# Intialize the pygame
pygame.init()
pygame.mixer.init()
# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Background Color
screen.fill((255, 0, 0))


# Title and Icon
pygame.display.set_caption("Bomb Project")
icon = pygame.image.load('bird.png')
pygame.display.set_icon(icon)

# Sound Effects 
pls_sound = pygame.mixer.Sound('PLSWORK.wav')
pls_sound.play(loops=-1)

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


GrassImg = pygame.image.load('grass.png')
GrassX = 1100
GrassY = 1100

def Grass(x, y):
    screen.blit(GrassImg, (x, y))

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

    Yess = False
    
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


                    if playerX >= 180 and playerX <= 285 and playerY == 333 and GrassX == 200:
                        Yess = True

                    if (Yess):
                        Running2 = False

                    
                        

                    print(playerY)

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
                    Grass(GrassX, GrassY)
                    portal(portalX, portalY)
                    portal(portalX2, portalY2)
                    player(playerX, playerY)
                    pygame.display.update()

                    time.sleep(.001)



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

                        GrassX = 200
                        GrassY = 350

                    if portalX2 == 60 and playerX > 0 and playerX < 100:
                        portalX2 = 1100
                        portalY2 = 1100

                        portalX = 700
                        portalY = 480

                        playerX = 670
                        playerY = 480

                        BackgroundX = 0
                        BackgroundY = 0

                        GrassX = 1100
                        GrassY = 1100

                    if playerY == 357.5:
                        if playerX > 285 or playerX < 180:
                            playerY = 480

                    Background(BackgroundX, BackgroundY)
                    Grass(GrassX, GrassY)
                    player(playerX, playerY)
                    portal(portalX, portalY)
                    portal2(portalX2, portalY2)

                    pygame.display.update()
                    screen.fill((0, 0, 0))



            if event.key == pygame.K_RIGHT:
                while pygame.event.poll().type != pygame.KEYUP:
                    pygame.time.wait(60)
                    playerX += 5

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

                        GrassX = 200
                        GrassY = 350 
                    
                    if portalX2 == 60 and playerX > 0 and playerX < 100:
                        portalX2 = 1100
                        portalY2 = 1100

                        portalX = 700
                        portalY = 480

                        playerX = 670
                        playerY = 480

                        BackgroundX = 0
                        BackgroundY = 0

                        GrassX = 1100
                        GrassY = 1100
                    
                    if playerY == 357.5:
                        if playerX > 285 or playerX < 180:
                            playerY = 480


                    # Place Sprites Here
                    Background(BackgroundX, BackgroundY)
                    Grass(GrassX, GrassY)
                    player(playerX, playerY)
                    portal(portalX, portalY)
                    portal2(portalX2, portalY2)

                    pygame.display.update()  
                    screen.fill((0, 0, 0))    
    # More collision - Portal2 and Player collision  
    if playerY == 357.5:
        if playerX > 285 or playerX < 180:
            playerY = 480

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

    Grass(GrassX, GrassY)

    portal2(portalX2, portalY2)

    portal(portalX, portalY)

    player(playerX, playerY)
    
    pygame.display.update()
            
