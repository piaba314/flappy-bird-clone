import pygame
from config import LARGURA_DA_TELA, ALTURA_DA_TELA, VELOCIDADE_DO_GROUND

class Ground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = pygame.image.load("assets/sprites/base.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = ALTURA_DA_TELA
        self.vel = pygame.Vector2(-VELOCIDADE_DO_GROUND, 0)

    def update(self, delta):
        self.rect.center += delta * self.vel
        if self.rect.right <= LARGURA_DA_TELA:
            self.rect.left = 0
