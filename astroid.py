import pygame
import os
import random


class Astroid:
    def __init__(self, speed):
        self.texture = pygame.image.load(os.path.join('./assets', 'astroid.png'))
        self.texture.convert()
        self.rect = self.texture.get_rect()
        self.windowSize = pygame.display.get_window_size()
        self.rect.x = random.randint(0, self.windowSize[0] - self.rect.w)
        self.life = 200
        self.rotate = 0
        
        self.size = random.randint(30, 70)
        self.speed = speed


    def update(self):
        # if self.rect.x > vec.x:
        #     self.rect.x -= 2
        # if self.rect.x < vec.x:
        #     self.rect.x += 2
        self.rect.y += self.speed
        
        self.rotate += 1
        if self.rotate >= 360:
            self.rotate = 0

    def isOut(self):
        if self.windowSize[1] <= 0:
            return True
        return False
    
    def isDestroyed(self):
        if self.life <= 0:
            return True
        return False

    def draw(self, screen):
        image = pygame.transform.rotate(self.texture, self.rotate)
        newRect = image.get_rect(center = self.rect.center, w = self.size, h = self.size)

        screen.blit(image, newRect)
    

