'''
Simples programa tocador de MP3
'''
import pygame
print('##### CRIE UM PGM QUE TOQUE UM MP3 #####')
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
