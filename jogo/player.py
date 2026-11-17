import pygame
from . import settings


class Player:

    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x, y,
            settings.PLAYER_SIZE,
            settings.PLAYER_SIZE
        )

        self.velocity_y = 0

    def jump(self):
        self.velocity_y = settings.JUMP_STRENGTH

    def update(self, dt):
        self.velocity_y += settings.GRAVITY * dt
        self.rect.y += self.velocity_y * dt

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            settings.PLAYER_COLOR,
            self.rect
        )
