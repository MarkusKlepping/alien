import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    pygame.init()

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)



    def run_game(self):
        """Start the main loop for ghe game."""
        

        while True:
            #Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()

        
            #Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right.
                    self.ship.moving_right = True
                    #Move the ship to the left
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    


        """Respond to keypress and mouse events"""
        #Set the background color

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""

        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

if __name__ == "__main__":
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()


"""
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/codeworkspace/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
"""