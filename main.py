import constants # TODO delte me 

import pygame
from asteroid import Asteroid
from asteroidfeild import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    message = f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}"
    print(message)
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for two_drawable in drawable:
            two_drawable.draw(screen)

        thingy = Asteroid(100, 100, 20)
        foo = thingy.position
        pygame.draw.circle(screen, "white", thingy.position, thingy.radius, constants.LINE_WIDTH)
        pygame.draw.circle(screen, "white", thingy.position, thingy.radius, 2)
        pygame.draw.circle(screen, "white", pygame.Vector2((25, 48)), thingy.radius, 2)

        screen.fill("black")
        player.draw(screen)
        # TODO put draw methods HERE
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
