import os
import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, nombre, imagen_path, posicion):
        super().__init__()
        self.nombre = nombre
        self.image = pygame.image.load(imagen_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

    def mover(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy