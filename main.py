import time
from pygame import mixer, Rect
import pygame.freetype
import pygame
from pygame.rect import RectType
import sys
#---------------------------------------setup------------------------------------------------
pygame.init()
mixer.init()

white = (255, 255, 255)
black = (0, 0, 0)

info = pygame.display.Info()
X, Y = info.current_w, info.current_h

screen = display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption("There Is No Game")

# --------------------------------Loading the song---------------------------------------------------------
mixer.music.load("sound_effect.mp3")
pygame.mixer.music.play()

# Setting the volume
mixer.music.set_volume(1.0)
#---------------------------------loading progress--------------------------------------------------------
font = pygame.freetype.Font('Bold.ttc', 70)
# Loading progress screen
loading_font = pygame.freetype.Font('Bold.ttc', 30)
loading_message = "Loading..."
loading_text_surface, loading_text_rect = loading_font.render(loading_message, fgcolor=white, bgcolor=black)
loading_text_rect.center = (X // 2, Y // 2)

loading_progress = 0

while loading_progress < 100:
    display_surface.fill(black)
    display_surface.blit(loading_text_surface, loading_text_rect)

    # Simulate loading progress (replace this with your actual loading logic)
    # For example, loading from a file or performing initialization
    loading_progress = 0

    while loading_progress < 100:
        display_surface.fill(black)
        display_surface.blit(loading_text_surface, loading_text_rect)

        # Simulate loading progress (replace this with your actual loading logic)
        # For example, loading from a file or performing initialization
        loading_progress += 1

        # Draw a progress bar (optional)
        pygame.draw.rect(display_surface, white, (100, Y - 50, loading_progress * 2, 20))

        pygame.display.update()  # Add this line to update the display
        pygame.time.delay(15)
#-------------------------------------------------messages display----------------------------------------
# messages = ["There is NO GAME", "probably not made with python", "not a game made by Steven Su", "   ", " ", " ", " ",
#            pygame.mixer.music.play(), "hello user", "I'm sorry say,", "but there is no game here",
#            pygame.image.load(f"nail1.png", f"nail2.png")]
font = pygame.freetype.Font('Bold.ttc', 70)


messages = ["There is NO GAME", "probably not made with python", "not a game made by Steven Su", "   ", " ",
            "hello user", "I'm sorry say,", "but there is no game here","what are you looking for?"]

textRect = []

for message in messages:
    text_surface, rect = font.render(message, fgcolor=pygame.Color('white'), bgcolor=pygame.Color('black'))
    textRect.append(rect)

background_message_index = messages.index("not a game made by Steven Su") + 1
background_message_2_index = messages.index("hello user")
background_message_3_index = messages.index("I'm sorry say,")
background_message_4_index = messages.index("but there is no game here")
background_message_5_index = messages.index("what are you looking for?")
# #---------------------------------------------Square crosshair cursor-------------------------------------------------
crosshair = (
    "XXX..XXX",
    ".X.XX.X.",
    ".X.XX.X.",
    "XXX..XXX",
)

# Pad the cursor string to be divisible by 8 (multiple of 8)
cursor = pygame.cursors.compile(crosshair + (" " * 8,) * 4, "X", ".")

pygame.mouse.set_cursor((8, 8), (4, 4), *cursor)

# Initialize font with the desired size
font_size = 70
font = pygame.freetype.Font('Bold.ttc', font_size)

#----------------------------------------main loop-------------------------------------------------
fade_in = True
alpha = 0
message_index: int = 0
while message_index < len(messages):
    display_surface.fill(black)

    if fade_in:
        alpha += 5  # Increase alpha for fade in (faster)
    else:
        alpha -= 5  # Decrease alpha for fade out (faster)

    text_surface, rect = font.render(messages[message_index], fgcolor=pygame.Color('white'), bgcolor=pygame.Color('black'))
    text_surface.set_alpha(alpha)
    textRect[message_index].center = (X // 2, Y // 2)
    display_surface.blit(text_surface, textRect[message_index])

    pygame.display.update()
    time.sleep(0.01)  # Faster time delay

    if alpha >= 255:
        pygame.time.delay(750)
        fade_in = False

    if alpha <= 0:
        message_index += 1
# --------------------------------Loading the 跟读---------------------------------------------------------
        if message_index == background_message_index:
            background_music = pygame.mixer.Sound("background.wav")
            background_music.set_volume(0.1)
            background_music.play()
        if message_index == background_message_2_index:
            hello_user = pygame.mixer.Sound("hello_user.mp3")
            hello_user.play()
        if message_index == background_message_3_index:
            Im_sorry_to_say = pygame.mixer.Sound("Im_sorry_to_say.mp3")
            Im_sorry_to_say.play()
        if message_index == background_message_4_index:
            but_there_is_no_game_here = pygame.mixer.Sound("but_there_is_no_game_here.mp3")
            but_there_is_no_game_here.play()
        if message_index == background_message_5_index:
            what_are_you_looking_for = pygame.mixer.Sound("what_are_you_looking_for.mp3")
            what_are_you_looking_for.play()
        if message_index < len(messages):
            fade_in = True


# ------------------------------image display (unfinished)------------------------
#letter_paths = ["T.png", "H.png", "E.png", "R.png", "E2.png", "I.png", "S.png",
  #              "N.png", "O.png", "G.png", "A.png", "M.png", "E.png"]
#nail_paths = ["nail1.png", "nail2.png"]

#letters = [pygame.image.load(letter_path) for letter_path in letter_paths]
#nails = [pygame.image.load(nail_path) for nail_path in nail_paths]

#letter_rects = [letter.get_rect(center=(X // 2, Y // 2)) for letter in letters]

# Initialize variables
#click_count = 0
#dragging = False
#selected_letter = None

# Main loop
#running = True
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
        #    running = False
        #elif event.type == pygame.MOUSEBUTTONDOWN:
        #    if click_count < 3:
       #         click_count += 1
      #      else:
    #            # Allow dragging after 3 clicks
     #           for letter_rect in letter_rects:
   #                 if letter_rect.collidepoint(event.pos):
  #                      dragging = True
 #                       selected_letter = letter_rect
#
   #     elif event.type == pygame.MOUSEBUTTONUP:
  #          dragging = False
 #           selected_letter = None
#
   #     elif event.type == pygame.MOUSEMOTION and dragging:
  #          # Move the selected letter with the mouse
 #           selected_letter.center = event.pos
#
 #   display_surface.fill(black)
#
  #  for i in range(len(letter_paths)):
 #       display_surface.blit(letters[i], letter_rects[i])
#
    #if click_count >= 3:
   #     # After 3 clicks, display nails
  #      for nail in nails:
 #           display_surface.blit(nail, (random.randint(0, X - 50), random.randint(0, Y - 50)))
#
    #pygame.display.update()
    #pygame.time.delay(2)  # Adjust the delay between frames

#----------------------------------------loop circle------------------
while True:
    display_surface.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    time.sleep(0.01)
#-----------------------------------------------------------------
