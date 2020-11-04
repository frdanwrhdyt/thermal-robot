import pygame

pygame.mixer.init()
pygame.mixer.music.load("Alarm4.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue