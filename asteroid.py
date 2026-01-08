import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # print('draw me')
        # print(f"self.position: {self.position}")
        # print(f"self.radius {self.radius}")
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_vel = self.velocity.rotate(random_angle)
        second_vel = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_ast = Asteroid(self.position.x, self.position.y, new_radius)
        first_ast.velocity = first_vel * 1.2  # 1.2 is the magic number
        second_ast = Asteroid(self.position.x, self.position.y, new_radius)
        second_ast.velocity = second_vel * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
