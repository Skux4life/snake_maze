class Settings:
    """Manage game related settings"""
    
    def __init__(self) -> None:
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Snake settings
        self.snake_speed = 3