import pygame
import os

class Player:
    def __init__(self):
        self.texture = pygame.image.load(os.path.join('./assets', 'player.png'))
        self.texture.convert()
        self.rect = self.texture.get_rect()
        self.windowSize = pygame.display.get_window_size()
        self.rect.x = self.windowSize[0] / 2 - 32
        self.rect.y = self.windowSize[1] - 77
        self.floating = 1
        self.floatDir = 0
        self.power = 5
        self.maxLife = 100
        self.life = self.maxLife
        self.engineSfx = pygame.mixer.Sound(os.path.join('./assets/sfx', 'engine.mp3'))
        self.powerSfx = pygame.mixer.Sound(os.path.join('./assets/sfx', 'power.mp3'))
        self.crashSfx = pygame.mixer.Sound(os.path.join('./assets/sfx', 'crash.mp3'))
        self.crashSfx.set_volume(0.3)
        pygame.mixer.Channel(4).play(self.engineSfx)
        self.powerLife = 0
        self.moving = 0

    def update(self, dt):
        
        self.rect.y += self.floating
        
        self.floating += self.floatDir

        if self.floating >= 1:
            self.floatDir = -1
        elif self.floating <= -1:
            self.floatDir = 1

        if self.rect.x < 0:
            self.rect.x = 0
            
        if self.rect.x + self.rect.w > self.windowSize[0]:
            self.rect.x = self.windowSize[0] - self.rect.w

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + self.rect.h > self.windowSize[1]:
            self.rect.y = self.windowSize[1] - self.rect.h

        if (self.powerLife > 0):
            self.powerLife -= 0.1
        
        if (self.powerLife <= 0):
            self.power = 5

        

    def damage(self, damage):
        self.life -= damage

    def moveRight(self, d):
        self.rect.x += d
        self.moving = 2

    def moveLeft(self, d):
        self.rect.x -= d
        self.moving = 1

    def moveUp(self, d):
        self.rect.y -= d
        self.moving = 3

    def moveDown(self, d):
        self.rect.y += d
        self.moving = 4

    def isCollidingWithAstroid(self, astroid):
        x = self.rect.x + 10
        y = self.rect.y + 10
        w = self.rect.w - 20
        h = self.rect.h - 20

        ax = astroid.rect.x + 10
        ay = astroid.rect.y + 10
        aw = astroid.rect.w - 20
        ah = astroid.rect.h - 20
        
        if x < ax + aw and x + w > ax and y < ay + ah and y + h > ay:
            pygame.mixer.Channel(5).play(self.crashSfx)
            if x < ax + aw / 2:
                self.rect.x -= 10
            else:
                self.rect.x += 10
            
            return True
        return False

    def isCollidingWithPower(self, power):
        x = self.rect.x + 10
        y = self.rect.y + 10
        w = self.rect.w - 20
        h = self.rect.h - 20

        ax = power.rect.x + 10
        ay = power.rect.y + 10
        aw = power.rect.w - 20
        ah = power.rect.h - 20
        
        if x < ax + aw and x + w > ax and y < ay + ah and y + h > ay:
            pygame.mixer.Channel(3).play(self.powerSfx)
            return True
        return False

    def getPower(self, power):
        self.powerLife = 100
        self.power = power

    def draw(self, screen):

        if self.life > 0:
            screen.blit(self.texture, self.rect)

        powerRect = pygame.rect.Rect(self.rect.x - self.powerLife / 2 + self.rect.w / 2, self.rect.y - 10, self.powerLife, 5)
        pygame.draw.rect(screen, "yellow", powerRect)
    
    def isDestroyed(self):
        if self.life <= 0:
            return True
        return False