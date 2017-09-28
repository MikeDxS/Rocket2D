##Creado por Juan Fernando Arango, Michael Daniel Suarez y Johan Sebastian Diaz 
import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 622, 400
velocidad = [0, 4]
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Roket2D")

fps=60
clock = pygame.time.Clock()

def main():
    ball = pygame.image.load("img/carro1")
    ballrect = ball.get_rect()
    ballrect.left = (width/2)-(ballrect.width/2)
    ballrect.top = (height/2)-(ballrect.height/2)

    court = pygame.image.load("img/campo.png")
    courtrect = court.get_rect()
    while True:
        clock.tick(fps)
        velocidad=[0,0]
              
        for evento in pygame.event.get():
            if evento.type ==QUIT:
                pygame.quit()
                sys.exit()
            if evento.type==pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    ballrect=ballrect.move([0,-10])
                if evento.key == pygame.K_DOWN:
                    ballrect=ballrect.move([0,10])
                if evento.key == pygame.K_RIGHT:
                    ballrect=ballrect.move([10,0])
                if evento.key == pygame.K_LEFT:
                    ballrect=ballrect.move([-10,0])
            
        #ballrect=ballrect.move(velocidad)
        #if ballrect.top < height/3 or ballrect.bottom >height:
            #velocidad[1]=-velocidad[1]
            #print "colusiono"
        
        ventana.blit(court,courtrect)
        ventana.blit(ball,ballrect)
        
        pygame.display.update()
        pygame.time.delay(10)
main()
