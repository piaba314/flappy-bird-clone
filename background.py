import pygame
from config import LARGURA_DA_TELA, ALTURA_DA_TELA, VELOCIDADE_DO_BACKGROUND

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = pygame.image.load("assets/sprites/background-day.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.vel = pygame.Vector2(-VELOCIDADE_DO_BACKGROUND, 0)

    def update(self, delta):
        self.rect.center += delta * self.vel
        if self.rect.right <= LARGURA_DA_TELA:
            self.rect.topleft = (0, 0)
