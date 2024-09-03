import pygame
import sys

class GuitarSynthesizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Guitar Synthesizer')
        self.clock = pygame.time.Clock()
        self.sounds = {
            'A': pygame.mixer.Sound('sound_A.wav'),
            'S': pygame.mixer.Sound('sound_S.wav'),
            'D': pygame.mixer.Sound('sound_D.wav'),
            # Adicione mais sons conforme necessário
        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.sounds['A'].play()
                    elif event.key == pygame.K_s:
                        self.sounds['S'].play()
                    elif event.key == pygame.K_d:
                        self.sounds['D'].play()
                    # Adicione mais teclas conforme necessário

            self.screen.fill((0, 0, 0))  # Limpa a tela
            pygame.display.flip()  # Atualiza a tela
            self.clock.tick(60)  # Controla o FPS

if __name__ == '__main__':
    synth = GuitarSynthesizer()
    synth.run()
