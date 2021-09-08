#tenho q instalar o pygame
import pygame

pygame.init()

#criar um arquivo mp3 com esse nome na mesma pasta
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play() #tocar
pygame.event.wait() #esperar