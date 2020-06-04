import time
import pygame 

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 0, 0))


start_time = time.time()
seconds = 4



WOW123 = True
while WOW123:
    screen.fill((255, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WOW123 = False

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                print("hello")
                hello = True
                while hello:
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    print("hello")

                    if elapsed_time > seconds:
                        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
                        hello = False


    pygame.display.update()