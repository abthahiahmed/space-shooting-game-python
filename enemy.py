import pygame
import os
import random


class Enemy:
    def __init__(self):
        self.texture = pygame.image.load(os.path.join('./assets', 'enemy.png'))
        self.texture.convert()
        self.rect = self.texture.get_rect()
        self.width, self.height = pygame.display.get_window_size()
        self.rect.x = random.randint(0, self.width - self.rect.w)
        self.life = 100
        self.shootingDelay = 0

    def isShooting(self):
        if self.shootingDelay > 140:
            self.shootingDelay = 0
            return True
        return False


    def update(self, vec):
        # if self.rect.x > vec.x:
        #     self.rect.x -= 2
        # if self.rect.x < vec.x:
        #     self.rect.x += 2
        self.rect.y += 1
        self.shootingDelay += 2

    def isDestroyed(self):
        if self.life <= 0:
            return True
        return False

    def isOut(self):
        if self.rect.y >= self.height:
            return True
        return False

    def moveFromAstroid(self, astroid):
        x = self.rect.x + 10
        y = self.rect.y + 10
        w = self.rect.w - 20
        h = self.rect.h - 20

        ax = astroid.rect.x + 10
        ay = astroid.rect.y + 10
        aw = astroid.rect.w - 20
        ah = astroid.rect.h - 20
        
        if x < ax + aw and x + w > ax and y < ay + ah and y + h > ay:
            if x < ax + aw / 2:
                self.rect.x -= 5
            else:
                self.rect.x += 5

    def draw(self, screen):
        lifeRect = pygame.rect.Rect(self.rect.x - self.life / 2 + self.rect.w / 2, self.rect.y - 30, self.life, 5)

        screen.blit(self.texture, self.rect)
        pygame.draw.rect(screen, "red", lifeRect)
    

