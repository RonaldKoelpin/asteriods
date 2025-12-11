import pygame.draw
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        new_angle = random.uniform(20,50)
        new_velocity_1 = self.velocity.rotate(new_angle)
        new_velocity_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteriod_1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteriod_1.velocity = new_velocity_1*1.2
        new_asteriod_2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteriod_2.velocity = new_velocity_2*1.2



