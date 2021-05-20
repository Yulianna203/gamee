import yulianna
import pygame
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
h = 500
w = 500
pygame.init()
sc = pygame.display.set_mode((w, h))
c1 = yulianna.Circle(w // 2, h // 2, 100, PINK)
c2 = yulianna.Circle(250, 250, 50, WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill(GREEN)
    c1.draw(sc)
    c2.draw(sc)z
    c1.move()
    c2.move()
    pygame.display.update()
    
