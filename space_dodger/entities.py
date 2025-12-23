import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.speed = 5
        self.color = (0, 255, 0)  # Green
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < 800 - self.width:
            self.x += self.speed
        
        # Update rect for collision and drawing
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = speed
        self.color = (255, 0, 0)  # Red
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
