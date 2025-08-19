import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    tc = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable,drawable) #containers are always on class not instance
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisionwith(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collisionwith(shot):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = tc.tick(60)/1000
if __name__ == "__main__":
    main()
