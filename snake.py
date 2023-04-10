import pygame
from pygame.sprite import Sprite

class Snake(Sprite):
    """A class to manage the snake"""

    def __init__(self, game) -> None:
        """Initialize the snake and set it's starting position"""

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the snake image and its rect
        self.image = pygame.image.load('images/snake.bmp')
        self.rect = self.image.get_rect()

        self.center_snake()

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the position of the snake based on the movement flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.snake_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.snake_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.snake_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.snake_speed

        # Update the rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    
    def blitme(self):
        """Draw the snake at its current location"""

        self.screen.blit(self.image, self.rect)

    
    def center_snake(self):
        """Center the snake on the screen"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


