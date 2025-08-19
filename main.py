import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    tc = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable,drawable) #containers are always on class not instance
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = tc.tick(60)/1000
if __name__ == "__main__":
    main()
