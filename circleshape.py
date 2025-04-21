import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass


    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other):
        position1 = self.position
        position2 = other.position
        distance = position1.distance_to(position2)
        return distance < self.radius + other.radius