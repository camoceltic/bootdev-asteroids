import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20, 50)
        self.velocity = self.velocity.rotate(rand)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid_1.velocity = self.velocity * 1.2
        self.velocity = self.velocity.rotate(0 - 2 * rand)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid_2.velocity = self.velocity
