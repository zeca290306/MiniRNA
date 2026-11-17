import pygame
import random

from . import settings
from .player import Player
from .pipe import Pipe


class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT)
        )

        pygame.display.set_caption(settings.TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.reset()

    def reset(self):
        self.player = Player(150, settings.HEIGHT // 2)

        self.pipes = []
        self.spawn_timer = 0

        self.score = 0
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.player.jump()

                elif event.key == pygame.K_r and self.game_over:
                    self.reset()

    def update(self, dt):
        if self.game_over:
            return

        self.player.update(dt)

        self.spawn_timer += dt

        if self.spawn_timer >= settings.PIPE_SPAWN_INTERVAL:
            gap_y = random.randint(150, settings.HEIGHT - 150)

            self.pipes.append(
                Pipe(settings.WIDTH, gap_y)
            )

            self.spawn_timer = 0

        for pipe in self.pipes:
            pipe.update(dt)

            if pipe.collides_with(self.player):
                self.game_over = True

            if not pipe.scored and pipe.x + settings.PIPE_WIDTH < self.player.rect.x:
                pipe.scored = True
                self.score += 1

        self.pipes = [
            pipe for pipe in self.pipes
            if not pipe.is_off_screen()
        ]

        if self.player.rect.top < 0 or self.player.rect.bottom > settings.HEIGHT:
            self.game_over = True

    def draw(self):
        self.screen.fill(settings.BACKGROUND_COLOR)

        self.player.draw(self.screen)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
