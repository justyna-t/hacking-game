# Hacking Version 6
# This is a text-based password guessing game that displays a list of potential
# computer passwords. The player has at most 4 guesses to guess a password.
# When an incorrect password is entered, the game decrements the attempts left.
# The game displays a lockout warning when the player has only one guess
# attempt left. If the guess is correct the game display a success outcome, if
# the guess is incorrect and player used 4 guesses the game display a failure
# outcome.

# Use uagame module
# Documentation for uagame is in file 'uagame_documentation.txt'
from uagame import Window
from time import sleep

def main():
    location = [0, 0]
    attempts = 4
    window = create_window()
    display_header(window, location, attempts)

def create_window():
    window = Window("Hacking", 600, 500)
    window.set_font_name("couriernew")
    window.set_font_size(18)
    window.set_font_color("green")
    window.set_bg_color("black")
    return window

def display_header(window, location, attempts):
    string_high = window.get_font_height()
    #    for header line in header
    header = ["DEBUG MODE", "%d ATTEMPT(S) LEFT" % attempts, ""]
    for header_line in header:
        window.draw_string(header_line, location[0], location[1])
        window.update()
        location[1] += string_high
        sleep(0.3)

main()
