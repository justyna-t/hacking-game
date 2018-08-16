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
    attempts_left = 4
    window = create_window()
    display_header(window, location, attempts_left)
    password = display_password_list(window, location)
    guess = get_guesses(window, password, location, attempts_left)


def create_window():
    window = Window("Hacking", 600, 500)
    window.set_font_name("couriernew")
    window.set_font_size(18)
    window.set_font_color("green")
    window.set_bg_color("black")
    return window


def display_line(window, string, location):
    string_high = window.get_font_height()
    window.draw_string(string, location[0], location[1])
    window.update()
    location[1] += string_high
    sleep(0.3)


def display_header(window, location, attempts):
    header = ["DEBUG MODE", "%d ATTEMPT(S) LEFT" % attempts, ""]
    for header_line in header:
        display_line(window, header_line, location)


def display_password_list(window, location):
    password_list = ["PROVIDE", "SETTING", "CANTINA", "CUTTING", "HUNTERS",
                     "SURVIVE", "HEARING", "HUNTING", "REALIZE", "NOTHING",
                     "OVERLAP", "FINDING", "PUTTING", ""]
    for password in password_list:
        display_line(window, password, location)

    # choose password
    return password_list[7]


def get_guesses(window, password, location, attempts_left):
    #   prompt for guess
    string_high = window.get_font_height()
    guess = window.input_string("ENTER PASSWORD >", location[0], location[1])
    location[1] += string_high
    attempts_left -= 1

    while guess != password and attempts_left > 0 :
        window.draw_string(str(attempts_left), 0, string_high)

    #       check warning
        if attempts_left == 1:
            # get window height and width
            window_height = window.get_height()
            window_width = window.get_width()
            message = "*** LOCKOUT WARNING ***"
            x = window_width - window.get_string_width(message)
            y = window_height - string_high
            window.draw_string(message, x, y)

    #       prompt for guess
        guess = window.input_string("ENTER PASSWORD >", location[0], location[1])
        location[1] += string_high
        attempts_left -= 1
    return guess


main()
