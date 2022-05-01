import pygame
import sys
from config import DIMENSOES_DA_TELA, FPS
from bird import Bird
from background import Background
from ground import Ground

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(DIMENSOES_DA_TELA)
        pygame.display.set_caption("Flappy Bird Clone")
        pygame.display.set_icon(pygame.image.load("assets/favicon.png").convert_alpha())
        self.relogio = pygame.time.Clock()

        self.objetos = pygame.sprite.Group()
        self.background = Background(self.objetos)
        self.ground = Ground(self.objetos)
        self.bird = Bird(self.objetos)

    def main(self):
        while True:
            self.processa_eventos()
            self.atualiza_mundo()
            self.renderiza_mundo()

    def processa_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def atualiza_mundo(self):
        delta = self.relogio.tick(FPS)/1000
        self.objetos.update(delta)
    
    def renderiza_mundo(self):
        self.objetos.draw(self.tela)
        pygame.display.update()

if __name__ == "__main__":
    Jogo().main()
