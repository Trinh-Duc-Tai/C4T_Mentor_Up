#Xóa giới thiệu về Pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# Chạy nhạc
from pygame import mixer
mixer.init()
mixer.music.load('mot-dem-say.mp3')
mixer.music.play()

while True:
    input("Press any key to stop")
    break