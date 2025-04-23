import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Projectile

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Projectile.containers = (updatable, drawable, projectiles)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                sys.exit("Game Over!")
            for projectile in projectiles:
                if projectile.isColliding(asteroid):
                    asteroid.split()
                    projectile.kill()

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()