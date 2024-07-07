import pygame
import os
import random


class Power:
    def __init__(self):
        self.texture = pygame.image.load(os.path.join('./assets', 'power.png'))
        self.texture.convert()
        self.rect = self.texture.get_rect()
        self.windowSize = pygame.display.get_window_size()
        self.rect.x = random.randint(0, self.windowSize[0] - self.rect.w)
        

    def update(self):
        # if self.rect.x > vec.x:
        #     self.rect.x -= 2
        # if self.rect.x < vec.x:
        #     self.rect.x += 2
        self.rect.y += 1

    def isOut(self):
        if self.windowSize[1] <= 0:
            return True
        return False



    def draw(self, screen):
        screen.blit(self.texture, self.rect)
    

