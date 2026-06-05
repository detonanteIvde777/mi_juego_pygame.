import os
import random
import pygame

from src.personajes import Personaje
from src.comida import Personaje as Comida
from src.items import Personaje as Item
from src.obstaculos import Personaje as Obstaculo  

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mi Juego Pygame")

    # Crear grupos de sprites
    personajes = pygame.sprite.Group()
    comidas = pygame.sprite.Group()
    items = pygame.sprite.Group()
    obstaculos = pygame.sprite.Group()

    # Crear un personaje principal
    jugador = Personaje(100, 100, 50, 50, (0, 255, 0))  # Verde
    personajes.add(jugador)

    # Crear comida, items y obstáculos
    for _ in range(5):
        comida = Comida("Comida", "assets/comida.png", (random.randint(0, 750), random.randint(0, 550)))
        comidas.add(comida)

        item = Item("Item", "assets/item.png", (random.randint(0, 750), random.randint(0, 550)))
        items.add(item)

        obstaculo = Obstaculo("Obstaculo", "assets/obstaculo.png", (random.randint(0, 750), random.randint(0, 550)))
        obstaculos.add(obstaculo)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            jugador.mover(-5, 0)
        if keys[pygame.K_RIGHT]:
            jugador.mover(5, 0)
        if keys[pygame.K_UP]:
            jugador.mover(0, -5)
        if keys[pygame.K_DOWN]:
            jugador.mover(0, 5)

        screen.fill((255, 255, 255))  # Fondo blanco
        personajes.draw(screen)
        comidas.draw(screen)
        items.draw(screen)
        obstaculos.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()