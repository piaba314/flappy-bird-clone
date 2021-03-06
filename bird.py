import pygame
import pymunk
from config import LARGURA_DA_TELA, ALTURA_DA_TELA
from anim import Animation

class Bird(pygame.sprite.Sprite):
    def __init__(self, mundo, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.init_graphics()
        self.init_physics(mundo)

    def init_graphics(self):
        self.animation = Animation(
            [
                pygame.image.load("./assets/sprites/yellowbird-downflap.png"),
                pygame.image.load("./assets/sprites/yellowbird-midflap.png"),
                pygame.image.load("./assets/sprites/yellowbird-upflap.png")
            ], 0.1)
        self.image = self.animation.image
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_DA_TELA//2-20, ALTURA_DA_TELA//2)

    def init_physics(self, mundo):
        massa = 1
        raio = 10
        inertia = pymunk.moment_for_circle(massa, 0, raio, (0, 0))
        self.body = pymunk.Body(massa, inertia)
        self.body.position = self.rect.center
        self.shape = pymunk.Circle(self.body, 10, (0, 0))
        self.shape.friction = 0.9
        self.shape.body = self.body
        mundo.add(self.shape, self.body)

    def update(self, delta):
        self.animation.update(delta)
        self.image = self.animation.image
        self.rect.center = self.body.position

    def processa_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                self.body.apply_impulse_at_local_point((0, -300), (0, 0))
