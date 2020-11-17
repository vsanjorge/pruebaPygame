# Proyecto de prueba en Pygame, en este caso siguiendo el tutorial de José Domingo Muñoz en el canal de YouTube de OpenWebinars: https://youtu.be/2Ilq_J_R9qU
import pygame
# Inicializamos pygame
pygame.init()
# Mostramos una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambiamos el título de la ventana
pygame.display.set_caption("Juego BALL")
# Inicializamos variables
width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255
# Creamos un objeto imagen y obtenemos su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
# Creamos un objeto imagen bate y obtenemos su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
# Ponemos el bate en el centro de la pantalla
baterect.move_ip(400, 260)
# Comenzamos el bucle del juego
run = True
while run:
  # Esperamos un tiempo (milisegundos) para que la pelota no vaya muy rápido
  pygame.time.delay(1)
  # Capturamos los eventos que se han producido
  for event in pygame.event.get():
    # Si el evento es salir de la ventana, terminamos
    if event.type == pygame.QUIT:
      run = False
  # Comprobamos si se ha pulsado alguna tecla
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP] and baterect.top <= 0: # Detectamos colisión del bate con el borde superior
    baterect = baterect.move(0, 0)
  elif keys[pygame.K_UP]:
    baterect = baterect.move(0, -1)
  if keys[pygame.K_DOWN] and baterect.bottom >= height: # Detectamos colisión del bate con el borde inferior
    baterect = baterect.move(0, 0)
  elif keys[pygame.K_DOWN]:
    baterect = baterect.move(0, 1)
  # Comprobamos si la pelota colisiona con el bate
  if baterect.colliderect(ballrect):
    speed[0] = -speed[0]
  # Movemos la pelota
  ballrect = ballrect.move(speed)
  # Comprobamos si la pelota llega a los límites de la ventana
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]
  # Pintamos el fondo blanco, dibujamos la pelota, el bate y actualizamos la pantalla
  screen.fill(white)
  screen.blit(ball, ballrect)
  screen.blit(bate, baterect)
  pygame.display.flip()
# Salimos de pygame
pygame.quit()