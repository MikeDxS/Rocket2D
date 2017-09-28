##Creado por Juan Fernando Arango, Michael Daniel Suarez y Johan Sebastian Diaz 
import sys, pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()
size = width, height = 1223, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Roket2D")

fps=60
clock = pygame.time.Clock()
pygame.key.set_repeat(True)

class Carro(Sprite):
    
    def __init__(self,img,x,y):
        self.car = pygame.image.load(img)
        self.carrect = self.car.get_rect()
        self.carrect.left = x
        self.carrect.top = y

    def dibujarCarro(self):
        ventana.blit(self.car,self.carrect) 
    
    def mover(self,key):
        if key=='U':
            self.carrect=self.carrect.move([0,-7])
        if key=='D':
            self.carrect=self.carrect.move([0,7])
        if key=='R':
            self.carrect=self.carrect.move([7,0])
        if key=='L':
            self.carrect=self.carrect.move([-7,0])  
    


def main():
    
    court = pygame.image.load("img/campo.png")
    court = pygame.transform.smoothscale(court, size)
    courtrect = court.get_rect()
    
    car1=Carro("img/carro1",100,100)
    car2=Carro("img/carro2",500,100)
    
    while True:
        clock.tick(fps)
                     
        for evento in pygame.event.get():
            if evento.type ==QUIT:
                pygame.quit()
                sys.exit()
            if evento.type==pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    car1.mover('U')
                if evento.key == pygame.K_DOWN:
                    car1.mover('D')
                if evento.key == pygame.K_RIGHT:
                    car1.mover('R')
                if evento.key == pygame.K_LEFT:
                    car1.mover('L')
            
                if evento.key == pygame.K_w:
                    car2.mover('U')
                if evento.key == pygame.K_s:
                    car2.mover('D')
                if evento.key == pygame.K_d:
                    car2.mover('R')
                if evento.key == pygame.K_a:
                    car2.mover('L')
                
            
        #ballrect=ballrect.move(velocidad)
        #if ballrect.top < height/3 or ballrect.bottom >height:
            #velocidad[1]=-velocidad[1]
            #print "colusiono"
        
        ventana.blit(court,courtrect)
        car1.dibujarCarro()
        car2.dibujarCarro()
        pygame.display.update()
      
main()
