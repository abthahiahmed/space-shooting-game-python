import pygame
import os
import math

class EnemyBullet:

    def __init__(self, vec, pvec):
        self.vector = vec
        self.power = 1
        self.sfx = pygame.mixer.Sound(os.path.join('./assets/sfx', 'bullet.mp3'))
        self.sfx2 = pygame.mixer.Sound(os.path.join('./assets/sfx', 'bullet-impact.mp3'))
        self.sfx.set_volume(1)
        self.sfx2.set_volume(0.6)
        pygame.mixer.Channel(6).play(self.sfx, 0, 1000)

        self.dx = pvec.x - vec.x
        self.dy = pvec.y - vec.y

        self.d = math.sqrt(self.dx * self.dx + self.dy * self.dy)

        self.v = 10
        self.vx = self.v * (self.dx / self.d)
        self.vy = self.v * (self.dy / self.d)

    def update(self, deltaTime):
        self.vector.x += self.vx
        self.vector.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, "deepskyblue", self.vector, 3.5)
    
    def isOut(self):
        if self.vector.y < 0 or self.vector.y > 700:
            return True
        return False

    def isImpacting(self, player):
        bx = self.vector.x
        by = self.vector.y
        x = player.rect.x
        y = player.rect.y
        w = player.rect.w
        h = player.rect.h
        if bx > x and bx < x + w and by > y and by < y + h:
            player.life -= self.power
            pygame.mixer.Channel(7).play(self.sfx2, 0, 1800)
            return True    
        return False
    