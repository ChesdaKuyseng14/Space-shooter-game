import pygame
import os
import sys
import time
import random
from menu import *
import menu
from log2 import *
import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 750, 750

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
HIGHLIGHT = (100, 100, 255)

# Fonts
FONT = pygame.font.Font(None, 50)
LARGE_FONT = pygame.font.Font(None, 70)

# Create a Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Menu")

# Load Background
background_image = pygame.image.load(os.path.join("assets","menu_background.jpg"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load Sound Effects
navigate_sound = pygame.mixer.Sound(os.path.join("sounds","navigate_sound.mp3"))
select_sound = pygame.mixer.Sound(os.path.join("sounds","selected_sound.mp3"))

# Menu options
menu_options = ["Start Game", "Resume Game", "Options", "Exit"]

def draw_menu(selected_index):
    # Draw Background
    screen.blit(background_image, (0, 0))
    
    for i, option in enumerate(menu_options):
        # Use larger font for the selected option
        font = LARGE_FONT if i == selected_index else FONT
        color = HIGHLIGHT if i == selected_index else WHITE
        text = font.render(option, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3 + i * 80))
    pygame.display.flip()
def menu_choice(menu_choice):
    return menu_choice
def main_menu():
    selected_index = 0
    menu_choice =''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    navigate_sound.play()
                    selected_index = (selected_index + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    navigate_sound.play()
                    selected_index = (selected_index - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    select_sound.play()
                    if selected_index == 0:  # Start Game
                        menu_choice = "start"
                        return menu_choice
                    elif selected_index == 1:  # Resume Game
                        menu_choice = "resume"
                        return menu_choice
                    elif selected_index == 2:  # Options
                        menu_choice = "Options"
                        return menu_choice
                    elif selected_index == 3:  # Exit
                        pygame.quit()
                        sys.exit()

        draw_menu(selected_index)


