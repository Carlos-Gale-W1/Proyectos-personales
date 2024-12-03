import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones de pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Asteroides - Dispara y Esquiva!")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configuraciones del juego
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad_x = 0

    def update(self):
        # Movimiento de la nave
        self.rect.x += self.velocidad_x
        
        # Limitar movimiento dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

class Dardo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidad_y = -10

    def update(self):
        self.rect.y += self.velocidad_y
        # Eliminar dardos que salen de la pantalla
        if self.rect.bottom < 0:
            self.kill()

class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidad_y = random.randint(3, 8)

    def update(self):
        self.rect.y += self.velocidad_y
        # Eliminar asteroides que salen de la pantalla
        if self.rect.top > ALTO:
            self.kill()

def juego_principal():
    # Grupos de sprites
    todos_los_sprites = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    dardos = pygame.sprite.Group()
    
    # Crear nave
    nave = Nave()
    todos_los_sprites.add(nave)
    
    # Variables de juego
    puntuacion = 0
    tiempo_juego = 0
    dificultad = 60  # Frames entre generación de asteroides
    tiempo_disparo = 0
    
    # Bucle principal del juego
    jugando = True
    while jugando:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            
            # Controles de movimiento
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    nave.velocidad_x = -5
                if evento.key == pygame.K_RIGHT:
                    nave.velocidad_x = 5
                # Disparar dardo
                if evento.key == pygame.K_SPACE:
                    # Limitar la frecuencia de disparos
                    if tiempo_juego - tiempo_disparo > 15:
                        dardo = Dardo(nave.rect.centerx, nave.rect.top)
                        todos_los_sprites.add(dardo)
                        dardos.add(dardo)
                        tiempo_disparo = tiempo_juego
            
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    nave.velocidad_x = 0
        
        # Generar asteroides
        tiempo_juego += 1
        if tiempo_juego % dificultad == 0:
            asteroide = Asteroide()
            todos_los_sprites.add(asteroide)
            asteroides.add(asteroide)
            
            # Aumentar dificultad gradualmente
            if dificultad > 20:
                dificultad -= 1
        
        # Actualizar
        todos_los_sprites.update()
        
        # Comprobar colisiones de dardos con asteroides
        for dardo in dardos:
            asteroides_impactados = pygame.sprite.spritecollide(dardo, asteroides, True)
            for asteroide in asteroides_impactados:
                dardo.kill()
                puntuacion += 10  # Más puntos por destruir asteroides
        
        # Comprobar colisiones de nave con asteroides
        colisiones = pygame.sprite.spritecollide(nave, asteroides, False)
        if colisiones:
            jugando = False
        
        # Incrementar puntuación
        puntuacion += 1
        
        # Dibujar
        pantalla.fill(NEGRO)
        todos_los_sprites.draw(pantalla)
        
        # Mostrar puntuación
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
        pantalla.blit(texto_puntuacion, (10, 10))
        
        # Actualizar pantalla
        pygame.display.flip()
        
        # Controlar FPS
        reloj.tick(60)
    
    # Pantalla de Game Over
    pantalla.fill(NEGRO)
    texto_game_over = fuente.render("Game Over", True, BLANCO)
    texto_puntuacion_final = fuente.render(f"Puntuación final: {puntuacion}", True, BLANCO)
    texto_reiniciar = fuente.render("Presiona R para reiniciar", True, BLANCO)
    
    pantalla.blit(texto_game_over, (ANCHO//2 - texto_game_over.get_width()//2, ALTO//2 - 100))
    pantalla.blit(texto_puntuacion_final, (ANCHO//2 - texto_puntuacion_final.get_width()//2, ALTO//2))
    pantalla.blit(texto_reiniciar, (ANCHO//2 - texto_reiniciar.get_width()//2, ALTO//2 + 100))
    
    pygame.display.flip()
    
    # Esperar reinicio
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
    
    return False

# Bucle principal del programa
def main():
    reiniciar = True
    while reiniciar:
        reiniciar = juego_principal()
    
    pygame.quit()
    sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    main()