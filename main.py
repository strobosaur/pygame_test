import pygame
import os

WIDTH, HEIGHT = 480, 270
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizards of py")

FPS = 60

WHITE = (255,255,255)

SHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spr_fighter24x24_06.png"))

def draw_window(ship):
    WIN.fill(WHITE)
    WIN.blit(SHIP_IMAGE, (ship.x,ship.y))
    pygame.display.update()    

def main():
    ship = pygame.Rect(240, 128, 24, 24)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        ship.x += 1
        draw_window(ship)
                
    pygame.quit()
                
if __name__ == '__main__':
    main()