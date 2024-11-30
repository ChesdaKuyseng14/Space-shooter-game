import pygame
import os
from menu import *
from log2 import *
pygame.font.init()

# Constants for the game window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Space Shooter Options")

# Load images and sounds
BG1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_1.jpg")), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_2.jpg")), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_3.jpg")), (WIDTH, HEIGHT))
music_on_img = pygame.image.load(os.path.join("assets", "music_on.png"))
music_off_img = pygame.image.load(os.path.join("assets", "music_off.png"))

# Option menu fonts
main_font = pygame.font.SysFont("comicsans", 50)
option_font = pygame.font.SysFont("comicsans", 40)

# Initialize settings
current_volume = 0.5  # Volume starts at 50%
current_bg = BG1      # Start with the default background
music_on = True       # Start with music on

# Music handling
pygame.mixer.music.load(os.path.join("sounds", "game_music.mp3"))
pygame.mixer.music.set_volume(current_volume)  # Set initial volume

def draw_options_screen():
    """Draw the options screen, allowing the player to adjust settings."""
    WIN.blit(current_bg, (0, 0))

    title_label = main_font.render("Options", 1, (255, 255, 255))
    WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 50))

    # Volume control
    volume_label = option_font.render(f"Volume: {int(current_volume * 100)}%", 1, (255, 255, 255))
    WIN.blit(volume_label, (WIDTH / 2 - volume_label.get_width() / 2, 150))

    # Background selection
    bg_label = option_font.render("Background:", 1, (255, 255, 255))
    WIN.blit(bg_label, (WIDTH / 2 - bg_label.get_width() / 2, 250))
    
    # Music on/off toggle
    music_label = option_font.render("Music:", 1, (255, 255, 255))
    WIN.blit(music_label, (WIDTH / 2 - music_label.get_width() / 2, 350))
    music_button = music_on_img if music_on else music_off_img
    WIN.blit(music_button, (WIDTH / 2 - music_button.get_width() / 2, 400))

    pygame.display.update()

def options():
    """Handle the logic for the options screen."""
    global current_volume, current_bg, music_on
    run = True
    while run:
        draw_options_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:  # Increase volume
            if current_volume < 1.0:
                current_volume += 0.05  # Smaller increments for finer control
                pygame.mixer.music.set_volume(current_volume)
        
        if keys[pygame.K_DOWN]:  # Decrease volume
            if current_volume > 0.0:
                current_volume -= 0.05  # Smaller decrements
                pygame.mixer.music.set_volume(current_volume)

        if keys[pygame.K_1]:  # Select first background
            current_bg = BG1

        if keys[pygame.K_2]:  # Select second background
            current_bg = BG2

        if keys[pygame.K_3]:  # Select third background
            current_bg = BG3

        if keys[pygame.K_m]:  # Toggle music
            music_on = not music_on
            if music_on:
                pygame.mixer.music.play(-1, 0.0)  # Play music in a loop
            else:
                pygame.mixer.music.stop()

        if keys[pygame.K_ESCAPE]:  # Press ESC to go back to the main menu
            run = False
            menu_music.play()
            menu_music_stop()  # Stop any background music from options screen
            main_menu()  # Return to the main menu

    return  # After quitting options, return to the main menu
