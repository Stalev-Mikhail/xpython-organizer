import pygame
import sys

class Display():
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('couriernew', 40)
        self.screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Конвертер футів")
        self.screen.fill((255, 255, 255))

    def print_display(self, text):
        text = self.font.render("Результат:" + text, True, (0, 255, 0))
        self.screen.blit(text, (50, 50))
        pygame.display.update()
