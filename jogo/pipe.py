import pygame
from . import settings


class Pipe:

    def __init__(self, x, gap_y):
        self.x = x
        self.gap_y = gap_y
        self.scored = False

        self.top_rect = pygame.Rect(
            x, 0,
            settings.PIPE_WIDTH,
            gap_y - settings.PIPE_GAP // 2
        )

        self.bottom_rect = pygame.Rect(
            x,
            gap_y + settings.PIPE_GAP // 2,
            settings.PIPE_WIDTH,
            settings.HEIGHT
        )

    def update(self, dt):
        self.x -= settings.PIPE_SPEED * dt

        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)

    def draw(self, screen):
        pygame.draw.rect(screen, settings.PIPE_COLOR, self.top_rect)
        pygame.draw.rect(screen, settings.PIPE_COLOR, self.bottom_rect)

    def is_off_screen(self):
        return self.x + settings.PIPE_WIDTH < 0

    def collides_with(self, player):
        return (
            self.top_rect.colliderect(player.rect)
            or self.bottom_rect.colliderect(player.rect)
        )
