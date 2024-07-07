import pygame
import os

class Bullet:

    def __init__(self, vec, power):
        self.vector = vec
        self.power = power
        self.sfx = pygame.mixer.Sound(os.path.join('./assets/sfx', 'bullet.mp3'))
        self.sfx2 = pygame.mixer.Sound(os.path.join('./assets/sfx', 'bullet-impact.mp3'))
        self.sfx.set_volume(1)
        self.sfx2.set_volume(0.6)
        pygame.mixer.Channel(0).play(self.sfx, 0, 1000)

    def update(self, deltaTime):
         self.vector.y -= 500 * deltaTime
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.vector, self.power / 2)
    
    def isOut(self):
        if self.vector.y < 0:
            return True
    
    def isImpacting(self, enemy):
        bx = self.vector.x
        by = self.vector.y
        x = enemy.rect.x
        y = enemy.rect.y
        w = enemy.rect.w
        h = enemy.rect.h
        if bx > x and bx < x + w and by > y and by < y + h:
            enemy.life -= self.power

            pygame.mixer.Channel(1).play(self.sfx2, 0, 1800)
            return True    
        return False
    
    def isImpacting(self, astroid):
        bx = self.vector.x
        by = self.vector.y
        x = astroid.rect.x
        y = astroid.rect.y
        w = astroid.rect.w
        h = astroid.rect.h
        if bx > x and bx < x + w and by > y and by < y + h:
            astroid.life -= self.power
            pygame.mixer.Channel(1).play(self.sfx2, 0, 1800)
            return True