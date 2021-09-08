import pygame
from pygame import mixer
import sys
pygame.init()
mixer.init()
mixer.music.load("music/kaljo_no_katko.mp3")
mixer.music.set_volume(0.7)
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/1_auction_hall_with_temp1.jpg')
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("IPL Auction Game")
black = (0, 0, 0)
yellow = (237, 234, 52)
dark_red = (191, 34, 34)
red = (237, 21, 21)
light_blue = (21, 237, 219)
light_b = (21, 212, 237)
white = (255, 255, 255)
pink = (240, 22, 196)


def background_left_loop():
    dumped = False
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            mixer.music.play()

"""# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("music/kaljo_no_katko.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break"""

background_left_loop()
quit()
sys.exit()