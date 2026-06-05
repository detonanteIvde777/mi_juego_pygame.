### 🐜 Hormiga Aventura: Salva a la Colonia
¡Bienvenido a Hormiga Aventura! Un emocionante juego de habilidad y reflejos desarrollado en Python con la librería Pygame. Controla a una valiente hormiga en su peligroso viaje a través del bosque, recolecta recursos, rescata a tus compañeras y asegura la supervivencia del hormiguero ante la presencia de la Reina.
### personjes

1. ![alt text](assets/images/chirrete.jpg)
2. ![alt text](assets/images/petro.jpg)
3. ![alt text](assets/images/hormiga.jpg)

### poster

![alt text](<assets/images/HORMIGA AVENTURERA.jpg>)

### 📝 Descripción del Juego
En Hormiga Aventura, asumes el rol de una pequeña pero valiente hormiga que debe cruzar un bosque lleno de peligros para ayudar a su colonia. El camino no será fácil: tendrás que esquivar obstáculos estáticos y móviles mientras cumples misiones vitales de recolección y rescate.

El juego pone a prueba tu rapidez, atención y destreza en un entorno dinámico y desafiante.

### 🚀 Características Principales
Evita los Peligros: Esquiva piedras, telarañas, ramas en el suelo y mortales ramas que caen de los árboles en tiempo real.

Mecánica de Recolección: Junta comida esparcida por el mapa para abastecer al hormiguero.

Misión de Rescate: Encuentra a tus compañeras hormigas que están heridas y llévalas contigo de regreso a salvo.

Objetivo Épico: Llega hasta la cámara de la Reina Hormiga para entregar los recursos y salvar la colonia.

### 🎮 Cómo Jugar
## Controles
° Controles por definir (Ej: Flechas de dirección / WASD) -> Mover a la hormiga.

° P -> Pausar el juego.

° Esc -> Salir.

## Objetivo
1. Avanza por el bosque esquivando los obstáculos.

2. Camina sobre la comida y las hormigas heridas para recogerlas.

3. Llega al final del nivel donde te espera la Reina Hormiga para entregar los recursos y ganar la partida.

### 🛠️ Requisitos e Instalación
Para ejecutar este juego en tu máquina local, asegúrate de tener instalado Python 3.x y la librería Pygame.

1. Clona este repositorio:

```
Bash

git clone https://github.com/tu-usuario/hormiga-aventura.git
cd hormiga-aventura

2. **Instala las dependencias:**
   ```bash
   pip install pygame

```

3. Ejecuta el juego:
```
Bash

python main.py

---

## 📂 Estructura del Proyecto

```text
├── assets/             # Sprites, imágenes y efectos de sonido
│   ├── images/         # Hormiga, obstáculos (ramas, piedras), comida
│   └── sounds/         # Música de fondo y efectos de colisión/recolección
├── src/                # Código fuente del juego
│   ├── personajes.py   # Lógica de la hormiga y los otros personajes 
│   ├── obstaculos.py   # Comportamiento de los obstaculos ramas, piedras, etc.
│   └── items.py        # Lógica de la comida y hormigas heridas
├── main.py             # Archivo principal para iniciar el juego
└── README.md           # Este archivo
```

