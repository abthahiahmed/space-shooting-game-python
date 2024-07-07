import pygame
import os
import random


class Explode:
    def __init__(self, vec):
        self.texture = pygame.image.load(os.path.join('./assets', 'explode.png')).convert_alpha()
        
        # self.texture.convert_alpha()
        self.rect = self.texture.get_rect(left = 0)
        
        self.rect.x = vec.x
        self.rect.y = vec.y

        self.frame = 0

        self.sfx = pygame.mixer.Sound(os.path.join('./assets/sfx', 'enemy-explode.mp3'))
        self.sfx.set_volume(0.5)
        self.sfx.play()
        

    def update(self):
        self.frame += 1

    def isEnd(self):
        if self.frame > 21:
            return True
        return False


    def draw(self, screen):
        self.rect.width = 64
        self.rect.height = 64
        
        image = pygame.Surface((64, 64)).convert_alpha()
        image.blit(self.texture, (0, 0), (self.frame * 64, 0, 64, 64))
        image.set_colorkey((0, 0, 0), 1)
        if self.frame < 21:
            screen.blit(image, self.rect)
    

