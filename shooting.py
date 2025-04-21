import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
       
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def collide(self, other):
        position1 = self.position
        position2 = other.position
        distance = position1.distance_to(position2)
        return distance < self.radius + other.radius
        
