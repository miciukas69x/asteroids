import pygame

class ScoreManager:
    def __init__(self):
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
    
    def add_points(self, points):
        self.score += points
    
    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))