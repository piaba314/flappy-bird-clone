import pygame
from config import LARGURA_DA_TELA, ALTURA_DA_TELA

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = pygame.image.load("assets/sprites/background-day.png")
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_DA_TELA//2, ALTURA_DA_TELA//2)
