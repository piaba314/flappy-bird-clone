import pygame
from config import LARGURA_DA_TELA, ALTURA_DA_TELA

class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.images = [
                pygame.image.load("./assets/sprites/yellowbird-downflap.png"),
                pygame.image.load("./assets/sprites/yellowbird-midflap.png"),
                pygame.image.load("./assets/sprites/yellowbird-upflap.png")
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_DA_TELA//2-20, ALTURA_DA_TELA//2)
