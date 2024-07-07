import pygame
import os

import pygame.freetype
from player import Player
from enemy import Enemy
from bullet import Bullet
from explode import Explode
from astroid import Astroid
from power import Power
from background import Background
from enemy_bullet import EnemyBullet

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(10)
        pygame.font.init()
        pygame.display.set_caption("Space Shooting Game By Abthahi & Programming")
        self.screen = pygame.display.set_mode([500, 700])
        self.width, self.height = pygame.display.get_window_size()
        self.fps = pygame.time.Clock()
        self.isRunning = True
        self.dt = 0
        self.player = Player()
        self.enemies = [Enemy()]
        self.bullets = []
        self.bulletDelay = 0
        self.explosions = []
        self.enemyDelay = 0
        self.astroids = []
        self.astroidDelay = 0
        self.powers = []
        self.powerDelay = 0
        self.enemyBullets = []
        self.enemyBulletsDelay = 0
        self.sky = pygame.image.load(os.path.join('./assets', 'sky.png')).convert_alpha()
        self.skyRect = pygame.rect.Rect(0, 0, 600, 700)
        self.font = pygame.freetype.Font(os.path.join('./assets/fonts', 'KodeMono-Regular.ttf'), 20)
        self.score = 0
        self.isGaming = True
        self.background1 = Background(os.path.join('./assets', 'sky.png'), 0.1)
        self.background2 = Background(os.path.join('./assets', 'sky2.png'), 0.3)
        self.background3 = Background(os.path.join('./assets', 'sky3.png'), 0.5)

    def run(self):
        self.gameLoop()
        self.destroy()

    def gameLoop(self):
        while self.isRunning :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.isRunning = False 
            if self.isGaming == True:
                self.control()
                self.update()
            self.draw()

            

    def control(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.player.moveLeft(210 * self.dt)
        if key[pygame.K_RIGHT]:
            self.player.moveRight(210 * self.dt)
        if key[pygame.K_UP]:
            self.player.moveUp(210 * self.dt)
        if key[pygame.K_DOWN]:
            self.player.moveDown(210 * self.dt)
        if key[pygame.K_SPACE]:
            self.bulletDelay += 3
            if (self.bulletDelay >= 25):
                bulletStartFrom = pygame.Vector2(self.player.rect.x + 32, self.player.rect.y)
                self.bullets.append(Bullet(bulletStartFrom, self.player.power))
                self.bulletDelay = 0


    def update(self):
        self.dt = self.fps.tick(60) / 1000

        self.player.update(self.dt)

        for bullet in self.bullets:
            bullet.update(self.dt)
            if bullet.isOut():
                self.bullets.remove(bullet)

        for bullet in self.enemyBullets:
            bullet.update(self.dt)
            if bullet.isOut():
                self.enemyBullets.remove(bullet)
            if bullet.isImpacting(self.player):
                self.enemyBullets.remove(bullet)
        
        for astroid in self.astroids:
            astroid.update()
            if self.player.isCollidingWithAstroid(astroid):
                self.player.damage(1)

            if astroid.isDestroyed():
                self.score += 50
                self.explosions.append(Explode(pygame.Vector2(astroid.rect.x, astroid.rect.y)))
                self.astroids.remove(astroid)

            if astroid.isOut():
                self.astroids.remove(astroid)

            for bullet in self.bullets:
                if bullet.isImpacting(astroid):
                    self.bullets.remove(bullet)
        print(len(self.enemies))
        for enemy in self.enemies:
            enemy.update(self.player.rect)

            if enemy.isShooting():
                playerPos = pygame.Vector2(self.player.rect.centerx, self.player.rect.centery)
                enemyPos = pygame.Vector2(enemy.rect.centerx, enemy.rect.centery)
                self.enemyBullets.append(EnemyBullet(enemyPos, playerPos))

            for astroid in self.astroids:
                enemy.moveFromAstroid(astroid)

            if enemy.isDestroyed():
                self.score += 100
                self.explosions.append(Explode(pygame.Vector2(enemy.rect.x, enemy.rect.y)))
                self.enemies.remove(enemy)

            if enemy.isOut():
                self.enemies.remove(enemy)

            for bullet in self.bullets:
                if bullet.isImpacting(enemy):
                    self.bullets.remove(bullet)
            

        for explosion in self.explosions:
            explosion.update()
            if explosion.isEnd():
                self.explosions.remove(explosion)



        for power in self.powers:
            power.update()

            if self.player.isCollidingWithPower(power):
                self.player.getPower(10)
                self.powers.remove(power)

            if power.isOut():
                self.powers.remove(power)
            

        if self.player.isDestroyed():
            self.explosions.append(Explode(pygame.Vector2(self.player.rect.x, self.player.rect.y)))
            self.isGaming = False


        if self.enemyDelay > 400:
            self.enemies.append(Enemy())
            self.enemyDelay = 0

        if self.astroidDelay > 200:
            self.astroids.append(Astroid(0.5))
            self.astroidDelay = 0

        if self.powerDelay > 1400:
            self.powers.append(Power())
            self.powerDelay = 0

        self.astroidDelay += 1
        self.enemyDelay += 1
        self.powerDelay += 1
        self.score += 1




    def renderText(self, text, pos, center = False, size = 20):

        text, rect = self.font.render(text, "white", size = size)

        rect = text.get_rect(center = pos)
        if center:
            self.screen.blit(text, rect)
        else:
            self.screen.blit(text, pos)

    def progress(self):
        self.renderText("Score " + str(self.score), (10, 10))


    def gameOver(self):
        
        s = pygame.Surface((self.width, self.height))
        s.set_alpha(100)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0, 0))

        self.renderText("Game Over!", (80, 300), size = 60)
        self.renderText("Your Score: " + str(self.score), (self.width / 2, 400), size = 24, center = True)
        
        


    def draw(self):

        self.background1.draw(self.screen)
        self.background2.draw(self.screen)
        self.background3.draw(self.screen)

        
        
        for bullet in self.bullets:
            bullet.draw(self.screen)

        for bullet in self.enemyBullets:
            bullet.draw(self.screen)

        for astroid in self.astroids:
            astroid.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.player.draw(self.screen)

        for power in self.powers:
            power.draw(self.screen)


        for explosion in self.explosions:
            explosion.draw(self.screen)

        self.progress()

        if self.isGaming == False:
            self.gameOver()




        normalizedLife = (self.player.life / self.player.maxLife) * 100

        playerLife = pygame.rect.Rect(self.width - (normalizedLife + 10), 10, normalizedLife, 10)
        playerLifeBack = pygame.rect.Rect(self.width - 110, 10, 100, 10)


        pygame.draw.rect(self.screen, "grey", playerLifeBack)
        pygame.draw.rect(self.screen, "red", playerLife)

        pygame.display.flip()

    def destroy(self):
        pygame.quit()