import pygame
import sys
from config import DIMENSOES_DA_TELA
from bird import Bird
from background import Background

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(DIMENSOES_DA_TELA)
        pygame.display.set_caption("Flappy Bird Clone")
        self.relogio = pygame.time.Clock()

        self.objetos = pygame.sprite.Group()
        self.background = Background(self.objetos)
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
        pass

    
    def renderiza_mundo(self):
        self.objetos.draw(self.tela)
        pygame.display.update()

if __name__ == "__main__":
    Jogo().main()
