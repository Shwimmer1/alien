import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """
        init cat and creates a starting position
        """
        # load image and get rectangle
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images\ship.png")
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # every a new cat appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.middle = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        
    def update(self):
        """
        Updates the ship's position based on the flag
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor  
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.middle -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.middle += self.ai_settings.ship_speed_factor 
        self.rect.centerx = self.center
        self.rect.bottom = self.middle
        
    def blitme(self):
        """draw a ship at current position"""
        self.screen.blit(self.image, self.rect)