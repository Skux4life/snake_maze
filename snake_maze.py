import sys
import pygame

from settings import Settings
from snake import Snake

class SnakeEater:
    """Managing game assets and behaviour"""

    def __init__(self) -> None:
        """Initialize game and its resource"""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Snake Eater')

        self.snake = Snake(self)


    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self.snake.update()

            self._update_screen()
            self.clock.tick(60)
        

    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""

        self.screen.fill(self.settings.bg_colour)

        self.snake.blitme()

        pygame.display.flip()


    def _check_events(self):
        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = pygame.mouse.get_pos()
            #     self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""

        if event.key == pygame.K_RIGHT:
            self.snake.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.snake.moving_left = True
        elif event.key == pygame.K_UP:
            self.snake.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.snake.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""

        if event.key == pygame.K_RIGHT:
            self.snake.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.snake.moving_left = False
        elif event.key == pygame.K_UP:
            self.snake.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.snake.moving_down = False


if __name__ == '__main__':
    game = SnakeEater()
    game.run_game()