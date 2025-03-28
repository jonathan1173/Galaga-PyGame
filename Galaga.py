import pygame
import sys
import time
import random

pygame.init()

ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Naves")

color_enemigo = (0, 0, 255)
color_jugador = (255, 0, 0)

balas = []

class Naves:
    def __init__(self, x, y, velocidad, vida, daño, jugador=False):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.vida = vida
        self.daño = daño
        self.jugador = jugador
        self.ultimo_disparo = 0

    def muerte(self):
        self.vida -= self.daño
        if self.vida <= 0:
            if self.jugador:
                print("Has sido destruido")
            else:
                print("La nave enemiga ha sido destruida")
            return True
        return False

    def dibujar(self, pantalla):
        color = color_jugador if self.jugador else color_enemigo
        pygame.draw.rect(pantalla, color, (self.x, self.y, 40, 40))
        pygame.draw.rect(pantalla, (255, 255, 255), (self.x - 2, self.y - 2, 44, 44), 2)

    def disparar(self, frecuencia_disparo):
        tiempo_actual = time.time()
        if tiempo_actual - self.ultimo_disparo >= frecuencia_disparo:
            if self.jugador:
                balas.append(Balas(self.x + 18, self.y, 5, 1, jugador=True))  
            else:
                balas.append(Balas(self.x + 18, self.y + 40, 5, 1, jugador=False))  
            self.ultimo_disparo = tiempo_actual

class Balas:
    def __init__(self, x, y, velocidad, daño, jugador=False):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.daño = daño
        self.jugador = jugador  

    def mover(self, pantalla):
        if self.jugador:
            self.y -= self.velocidad  
        else:
            self.y += self.velocidad 
        pygame.draw.line(pantalla, (255, 255, 255), (self.x, self.y), (self.x, self.y - 10), 2)

class Jugador(Naves):
    def __init__(self, x, y, velocidad, vida, daño):
        super().__init__(x, y, velocidad, vida, daño, jugador=True)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x < ANCHO_PANTALLA - 40:
            self.x += self.velocidad

class Enemigo(Naves):
    def __init__(self, x, y, velocidad, vida, daño):
        super().__init__(x, y, velocidad, vida, daño, jugador=False)

def formacion_enemigos_piramide():
    enemigos = []
    filas = 5
    for i in range(filas):
        for j in range(filas - i):
            pos_x = j * (30 + 20)
            pos_y = 50 + i * (30 + 20)
            margen = ANCHO_PANTALLA // 2 - (filas - i) * (30 + 20) // 2
            enemigos.append(Enemigo(pos_x + margen, pos_y, 1, 2, 1))
    return enemigos

jugador = Jugador(230, 400, 5, 3, 1)
enemigos = formacion_enemigos_piramide()

ejecutando = True
while ejecutando:
    pantalla.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    jugador.mover(teclas)
    if teclas[pygame.K_SPACE]:
        jugador.disparar(frecuencia_disparo=0.5)  
    jugador.dibujar(pantalla)
    
    for enemigo in enemigos[:]:
        enemigo.dibujar(pantalla)
        enemigo.disparar(frecuencia_disparo=2)
        
    for bala in balas[:]:
        bala.mover(pantalla)
        if bala.y < 0 or bala.y > ALTO_PANTALLA:  
            balas.remove(bala)
        else:
            if bala.jugador:  
                for enemigo in enemigos[:]:
                    if enemigo.x < bala.x < enemigo.x + 40 and enemigo.y < bala.y < enemigo.y + 40:
                        if enemigo.muerte():
                            enemigos.remove(enemigo)
                            balas.remove(bala)       
            else:
                if jugador.x < bala.x < jugador.x + 40 and jugador.y < bala.y < jugador.y + 40:
                    if jugador.muerte():
                        balas.remove(bala)
                        ejecutando = False
               
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()
