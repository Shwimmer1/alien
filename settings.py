class Settings():
    """
    All settings by Alien Invasion.
    """
    def __init__(self):
        """
        init game settings.
        """
        # params screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (104, 53, 192)
        self.ship_speed_factor = 1.5
        # params bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 8
        self.bullet_height = 8
        self.bullet_color = (148, 8, 18)
        self.bullet_allowed = 3