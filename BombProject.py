# Write this before you press play in the terminal
# cd '/Users/leomi/OneDrive/Documents/Unity Games/HistoryProject/Assets/'

import pygame
import time
import math
from pygame import mixer

start_time = time.time()
start_time2 = time.time()

seconds = 5
JumpCount = 10


# Intialize the pygame
pygame.init()
pygame.mixer.init()
# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Background Color
screen.fill((255, 0, 0))

font = pygame.font.SysFont(None, 38)
yupie = pygame.font.SysFont(None, 60)
color = (255, 255, 255)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [100, 300])
    
def message_to_screen1(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [500, 350])

def message_to_screen2(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, 350])

def message_to_screen4(msg,color):
    screen_text = yupie.render(msg, True, color)
    screen.blit(screen_text, [200, 100])

# Title and Icon
pygame.display.set_caption("Bomb Project")
icon = pygame.image.load('bird.png')
pygame.display.set_icon(icon)

# Sound Effects 
pls_sound = pygame.mixer.Sound('PLSWORK.wav')
pls_sound.set_volume(0.8)
pls_sound.play(loops=-1)
Presnetation1 = pygame.mixer.Sound('Pres1.wav')
Presnetation2 = pygame.mixer.Sound('Pres2.wav')
Presnetation3 = pygame.mixer.Sound('Pres3.wav')
PresentGame = pygame.mixer.Sound('Who.mp3')
PresentGame2 = pygame.mixer.Sound('Who2.mp3')
Presnetation3.play(0)
if time.time() > start_time2 + 125:
    Presnetation1.play(0)


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

GrassImg2 = pygame.image.load('grass.png')
GrassX2 = 1100
GrassY2 = 1100



def Grass(x, y):
    screen.blit(GrassImg, (x, y))

def Grass2(x, y):
    screen.blit(GrassImg2, (x, y))

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


Yup = True
Player_XCord = playerY
OOpsk = True
# Game Loop
running = True
while running:

    if time.time() > start_time2 + 127 and (OOpsk):
        Presnetation1.play(0)
        print("yes")
        OOpsk = False

    if time.time() > start_time2 + 158 and (Yup):
        Presnetation2.play(1)
        print("yes")
        Yup = False

    

    

    
    Yess = False
    
    Player_XCord = playerY

    Running3 = True

    Nooi = False

    # Background Color
    screen.fill((0, 0, 0))


    for event in pygame.event.get():

        # Exit Window
        if event.type == pygame.QUIT:
            running = False

        # Player Movemnet
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:

                Running3 = True
                while Running3:

                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    print("helli")
                    if elapsed_time > seconds:
                        print("sceonds donw")
                        Running3 = False

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

                    if playerX >= 180 and playerX <= 285 and playerY == 333 and GrassX == 200:
                        Yess = True
                        playerX = 2000

                    if playerX >= 480 and playerX <= 585 and playerY == 333 and GrassX2 == 500:
                        Nooi = True
                        playerX = 50

                    if (Yess):
                        Running2 = False

                    if (Nooi):
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
                    Grass2(GrassX2, GrassY2)
                    Grass(GrassX, GrassY)
                    portal(portalX, portalY)
                    portal(portalX2, portalY2)
                    player(playerX, playerY)
                    pygame.display.update()

                    time.sleep(.001)



            if event.key == pygame.K_LEFT:
                while pygame.event.poll().type != pygame.KEYUP:
                    pygame.time.wait(35)
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

                        GrassX2 = 500
                        GrassY2 = 350

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

                        GrassX2 = 1100
                        GrassY2 = 1100
                    
                    if playerY == 357.5:
                        if playerX > 285 or playerX < 180:
                            if playerX > 585 or playerX < 480:
                                playerY = 480

                    

                    Background(BackgroundX, BackgroundY)
                    Grass2(GrassX2, GrassY2)
                    Grass(GrassX, GrassY)
                    player(playerX, playerY)
                    portal(portalX, portalY)
                    portal2(portalX2, portalY2)

                    pygame.display.update()
                    screen.fill((0, 0, 0))



            if event.key == pygame.K_RIGHT:
                while pygame.event.poll().type != pygame.KEYUP:
                    pygame.time.wait(35)
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

                        GrassX2 = 500
                        GrassY2 = 350
                    
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

                        GrassX2 = 1100
                        GrassY2 = 1100
                    
                    if playerY == 357.5:
                        if playerX > 285 or playerX < 180:
                            if playerX > 585 or playerX < 480:
                                playerY = 480


                    # Place Sprites Here
                    Background(BackgroundX, BackgroundY)
                    Grass2(GrassX2, GrassY2)
                    Grass(GrassX, GrassY)
                    player(playerX, playerY)
                    portal(portalX, portalY)
                    portal2(portalX2, portalY2)

                    pygame.display.update()  
                    screen.fill((0, 0, 0))    
    # More collision - Portal2 and Player collision  
    if playerY == 357.5:
        if playerX > 285 or playerX < 180:
            if playerX > 585 or playerX < 480:
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

    message_to_screen("Did America bomb Heroshima with the Little Boy?", color)

    if playerX == 2000 and portalX2 == 60:
        screen.fill((0, 255, 0))
        message_to_screen4("You Won", color)

    message_to_screen1("False", color)

    message_to_screen2("True", color)

    Grass(GrassX, GrassY)

    Grass2(GrassX2, GrassY2)

    portal2(portalX2, portalY2)

    portal(portalX, portalY)

    player(playerX, playerY)
    
    pygame.display.update()

    

        
