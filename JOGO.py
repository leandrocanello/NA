import pygame, time 
from pygame.locals import *
import sys
import os

class jogador (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagemjogador = pygame.image.load('jogador1.png').convert_alpha()
        self.rect = self.imagemjogador.get_rect()
        self.rect.centerx = HW 
        self.rect.centery = H - 70
        self.xx = W
        self.yy = H
        self.jump = 0
        self.velocidade = 1
        self.velocidadeP = 3
        self.vida = True
        self.listaDisparo = []

    def movimentacao(self):
        if self.vida == True:    
            if self.rect.left <= 0:
                self.rect.left = 0 
            elif self.rect.right > 450:
                self.rect.right = 450 

    def coloca(self, superficie):
        superficie.blit(self.imagemjogador, self.rect)

class disparo (pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagemBala = pygame.image.load('projetil.png').convert_alpha()
        self.rect = self.imagemBala.get_rect()
        self.velocidadeBala  = 10
        self.rect.right = posx
        self.rect.top = posx

    def trajetoria(self):
        self.rect.right = self.rect.right + self.velocidadeBala    

    def coloca1(self, superficie):
        superficie.blit(self.imagemBala, self.rect)
        

def main():
    player.movimentacao()
    bala.trajetoria()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    key1 = pygame.key.get_pressed()
    if key1[pygame.K_LEFT]:
        player.rect.left -= player.velocidade 
    if not key1[pygame.K_RIGHT]:
        player.rect.left -= player.velocidade
    if key1[pygame.K_RIGHT]:
        player.rect.left += player.velocidade*3        
    if key1[K_UP] and player.jump == 0:
        player.jump = 1


W, H = 450, 450
HW, HH = W/2, H/2 
AREA = W*H 

pygame.init()
tela = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")
fps = pygame.time.Clock()
#sup = pygame.Surface((1024, 450))


bkgd = pygame.image.load('fundo2.1.png').convert()
x = 0
player = jogador()
jogando  = True 
bala = disparo(HH + 130, H - 10) 

while True:
    main() 
    rel_x = x % bkgd.get_rect().width 
    tela.blit(bkgd, (rel_x - bkgd.get_rect().width , 0))
    if rel_x < W:
        tela.blit(bkgd, (rel_x, 0))
    x -= 1
    if player.rect.centery > 300 and player.jump == 1: 
        player.rect.centery -= 5
        player.rect.left += player.velocidade*3
    elif player.rect.centery == 300:
        player.jump = 2
    if player.rect.centery < 380 and player.jump == 2:
        player.rect.centery += 5 
        player.rect.left += player.velocidade*3.5
    elif player.rect.centery == 380:
        player.jump = 0    
    player.coloca(tela)
    bala.coloca1(tela)
    pygame.display.update()
    fps.tick(30)