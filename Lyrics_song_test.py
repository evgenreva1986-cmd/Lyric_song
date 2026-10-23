import time
from colorama import init
init()
from colorama import Fore, Back, Style
import pygame
with open("lyrics.txt","r") as file:
    wrds = file.readlines()
def display_lyrics(words, speed):
    pygame.mixer.init()
    music_file = "falling Down.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    for line in words:
        if 16 <= words.index(line) <= 25:
            for word in line.split():
                print(Fore.CYAN +  word, flush=True, end="")
                print(end=" ")
                time.sleep(speed * 2.5)
            time.sleep(speed)
            print()
        else:
            for word in line.split():
                for char in word:
                    print(Fore.MAGENTA + char,flush=True, end="")
                    time.sleep(speed)
                print(end=" ")
                time.sleep(speed * 1.6)
            time.sleep(speed * 25.5)
            print()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()

display_lyrics(wrds,speed = 0.1)