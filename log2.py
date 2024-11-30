import pygame
import pandas as pd
import os
import time

from menu import *
# Initialize Pygame
pygame.init()

# Constants
EXCEL_FILE = "game_data.xlsx"
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
LIGHT_BLUE = (135, 206, 235)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

#music 
menu_music = pygame.mixer.Sound(os.path.join("sounds","menu_music.mp3"))
# Font
FONT = pygame.font.SysFont("comicsansms", 36)
SMALL_FONT = pygame.font.SysFont("comicsansms", 24)

# Sounds
#BUTTON_CLICK_SOUND = pygame.mixer.Sound('button_click.wav')

# Create the Excel file if it doesn't exist
def create_excel():
    if not os.path.exists(EXCEL_FILE):
        with pd.ExcelWriter(EXCEL_FILE) as writer:
            pd.DataFrame(columns=["UserID", "Username", "Password", "Level", "Lives", "Health"]).to_excel(writer, sheet_name="UserData", index=False)

# Load the Excel file
def load_excel():
    try:
        excel = pd.ExcelFile(EXCEL_FILE)
        if 'UserData' not in excel.sheet_names:
            create_excel()
        return excel
    except FileNotFoundError:
        create_excel()
        return pd.ExcelFile(EXCEL_FILE)

create_excel()  # Call this once to initialize the file

# Login or Signup function
def login_or_signup():
    excel = load_excel()
    user_data = pd.read_excel(excel, sheet_name="UserData")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Login or Sign Up")

    # Load background image
    background = pygame.image.load(os.path.join("assets","menu_background.jpg"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Set up buttons and input boxes
    input_box = pygame.Rect(300, 150, 200, 40)
    password_box = pygame.Rect(300, 220, 200, 40)
    button_login = pygame.Rect(300, 290, 200, 50)
    button_signup = pygame.Rect(300, 370, 200, 50)

    active_input = False
    active_password = False
    username = ""
    password = ""
    user_id = None
    running = True
    menu_music.play(-1)


    while running:
        
        screen.blit(background, (0, 0))  # Draw background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_login.collidepoint(event.pos):
                    #BUTTON_CLICK_SOUND.play()  # Play sound effect for button click
                    # Handle Log In
                    user = user_data[(user_data["Username"] == username) & (user_data["Password"] == password)]
                    if not user.empty:
                        user_id = user.iloc[0]["UserID"]
                        print("Login successful!")
                        return user_id
                    else:
                        
                        
                        print("invalid")
                        invalid = SMALL_FONT.render("Invalid credentials. Try again.", True, WHITE)
                        screen.blit(invalid, (button_login.x-50 , button_login.y +150))
                        pygame.display.update()
                        time.sleep(1)
                       
                        
                elif button_signup.collidepoint(event.pos):
                   # BUTTON_CLICK_SOUND.play()
                    # Handle Sign Up
                    if username in user_data["Username"].values:
                        print("Username already exists. Try again.")
                    else:
                        new_id = len(user_data) + 1
                        new_user = {"UserID": new_id, "Username": username, "Password": password, "Level": 0, "Lives": 5, "Health": 100}
                        user_data = user_data._append(new_user, ignore_index=True)
                        user_data.to_excel(EXCEL_FILE, sheet_name="UserData", index=False)
                        print("Sign up successful! Starting a new game.")
                        user_id = new_id
                        return user_id

            if event.type == pygame.KEYDOWN:
                if active_input:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_password:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

            if event.type == pygame.MOUSEMOTION:
                if input_box.collidepoint(event.pos):
                    active_input = True
                else:
                    active_input = False
                if password_box.collidepoint(event.pos):
                    active_password = True
                else:
                    active_password = False

        # Draw input boxes with stylish borders and active colors
        if active_input:
            pygame.draw.rect(screen, LIGHT_BLUE, input_box, 2)
        else:
            pygame.draw.rect(screen, GRAY, input_box, 2)

        if active_password:
            pygame.draw.rect(screen, LIGHT_BLUE, password_box, 2)
        else:
            pygame.draw.rect(screen, GRAY, password_box, 2)

        # Render the text
        txt_surface = FONT.render(username, True, BLACK)
        screen.blit(txt_surface, (input_box.x + 10, input_box.y -5 ))
        txt_surface = FONT.render(password, True, BLACK)
        screen.blit(txt_surface, (password_box.x + 10, password_box.y -5 ))

        # Draw buttons with hover effects
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_login.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, YELLOW, button_login)
        else:
            pygame.draw.rect(screen, BLUE, button_login)

        if button_signup.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, YELLOW, button_signup)
        else:
            pygame.draw.rect(screen, BLUE, button_signup)

        # Button text
        login_text = SMALL_FONT.render("Log In", True, WHITE)
        screen.blit(login_text, (button_login.x + 60, button_login.y +5 ))

        signup_text = SMALL_FONT.render("Sign Up", True, WHITE)
        screen.blit(signup_text, (button_signup.x + 60, button_signup.y +5 ))

        # Display title text
        title_text = FONT.render("Welcome to Space Shooter!", True, YELLOW)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
def display_invalid_message():
    button_login = pygame.Rect(300, 290, 200, 50)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    invalid = SMALL_FONT.render("Invalid credentials. Try again.", True, WHITE)
    screen.blit(invalid, (button_login.x + 60, button_login.y + 100))



        # Optionally, you can continue to draw other game elements here


# Game Progress functions (as defined earlier)
def save_progress(user_id, level, lives, health):
    excel = load_excel()
    user_data = pd.read_excel(excel, sheet_name="UserData")
    user_progress = user_data[user_data["UserID"] == user_id]
    if not user_progress.empty:
        user_data.loc[user_data["UserID"] == user_id, ["Level", "Lives", "Health"]] = [level, lives, health]
    else:
        new_progress = {"UserID": user_id, "Level": level, "Lives": lives, "Health": health}
        user_data = user_data._append(new_progress, ignore_index=True)
    user_data.to_excel(EXCEL_FILE, sheet_name="UserData", index=False)

def load_progress(user_id):
    # choice = menu.main_menu()
    # if choice == 'start':
    #     user_progress.iloc[0]["Level"] = 0 
    #     user_progress.iloc[0]["Lives"] = 5
    #     user_progress.iloc[0]["Health"] = 100
    excel = load_excel()
    user_data = pd.read_excel(excel, sheet_name="UserData")
    user_progress = user_data[user_data["UserID"] == user_id]
    if not user_progress.empty:
        return user_progress.iloc[0]["Level"]-1, user_progress.iloc[0]["Lives"], user_progress.iloc[0]["Health"]
    else:
        return 0, 5, 100
def menu_music_stop():
    menu_music.stop()
# # Main Program
# def main():
#     user_id = login_or_signup()
#     level, lives, health = load_progress(user_id)
#     print(f"Loaded progress - Level: {level}, Lives: {lives}, Health: {health}")

# if __name__ == "__main__":
#     main()
