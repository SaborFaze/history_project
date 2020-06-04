import pygame 

pygame.init()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        
        if event.type == pygame.K_a:
            print("hello from the a key")
        if event.type == pygame.K_d:
            print("hello from the d key") 