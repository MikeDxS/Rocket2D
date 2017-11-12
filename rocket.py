##Creado por Juan Fernando Arango, Michael Daniel Suarez y Johan Sebastian Diaz 
import threading
import sys, pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()
size = width, height = 800, 600
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
        if key=='U' and self.carrect.bottom >=self.carrect.height:
            self.carrect=self.carrect.move([0,-7])
        if key=='D' and self.carrect.bottom <=600:
            self.carrect=self.carrect.move([0,7])
        if key=='R'and self.carrect.right <=800:
            self.carrect=self.carrect.move([7,0])
        if key=='L'and self.carrect.left>=0:
            self.carrect=self.carrect.move([-7,0])


class Balon(Sprite):
    def __init__(self,img,tamFondo):
        self.tamFondo = tamFondo
        self.bal = pygame.image.load(img)
        self.balrect = self.bal.get_rect()
        self.balrect.left = (tamFondo[0] / 2) - (self.balrect.width/2)
        self.balrect.top = (tamFondo[1] / 2) - (self.balrect.height/2)
        self.velocidad = [2, 4]
    def update(self, carroIzq, carroDer):
        self.balrect=self.balrect.move(self.velocidad)
        if self.balrect.top < 0 or self.balrect.bottom >self.tamFondo[1]:
            self.velocidad[1]=-self.velocidad[1]
        if self.balrect.left==0 or self.balrect.right==self.tamFondo[0]:
            self.velocidad[0]=-self.velocidad[0]
        if self.balrect.colliderect(carroIzq):
            self.velocidad[1]=-self.velocidad[1]
            self.velocidad[0]=-self.velocidad[0]
        if self.balrect.colliderect(carroDer):
            self.velocidad[1]=-self.velocidad[1]
            self.velocidad[0]=-self.velocidad[0]

def main():
    
    court = pygame.image.load("img/campo.png")
    court = pygame.transform.smoothscale(court, size)
    courtrect = court.get_rect()
    
    car1=Carro("img/carro1",100,100)
    car2=Carro("img/carro2",500,100)
    balon=Balon("img/balon",size)
    while True:
        clock.tick(fps)
        for evento in pygame.event.get():
            if evento.type ==QUIT:
                pygame.quit()
                sys.exit()
            if evento.type==pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    car2.mover('U')
                if evento.key == pygame.K_DOWN:
                    car2.mover('D')
                if evento.key == pygame.K_RIGHT:
                    car2.mover('R')
                if evento.key == pygame.K_LEFT:
                    car2.mover('L')
                
                if evento.key == pygame.K_w:
                    car1.mover('U')
                if evento.key == pygame.K_s:
                    car1.mover('D')
                if evento.key == pygame.K_d:
                    car1.mover('R')
                if evento.key == pygame.K_a:
                    car1.mover('L')
        balon.update(car1.carrect, car2.carrect)
        ventana.blit(court,courtrect)
        car1.dibujarCarro()
        car2.dibujarCarro()
        ventana.blit(balon.bal, balon.balrect)
        pygame.display.update()
      
main()
