import pygame
import os
import math

class Background:

    def __init__(self, path, speed):
        self.speed = speed
        self.scroll = 0
        self.width, self.height = pygame.display.get_window_size()
        self.bg = pygame.image.load(path).convert_alpha()
        self.tiles = math.ceil(self.height / self.bg.get_height()) + 1
    
    def draw(self, screen):
        i = self.tiles - 1
        while i >= 0:
            screen.blit(self.bg, (0, i * self.bg.get_height() + self.scroll))
            i -= 1
        
        self.scroll += self.speed

        if self.scroll > 0:
            self.scroll = -1 * self.bg.get_height()

        