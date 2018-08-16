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
    end_game(window, guess, password)


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

#   choose password
    return password_list[7]


def prompt_user(window, prompt, location):
    guess = window.input_string(prompt, location[0], location[1])
    location[1] += window.get_font_height()
    return guess

def check_warning(window, attempts_left):
    if attempts_left == 1:
        message = "*** LOCKOUT WARNING ***"
        x = window.get_width() - window.get_string_width(message)
        y = window.get_height() - window.get_font_height()
        window.draw_string(message, x, y)


def get_guesses(window, password, location, attempts_left):
#   prompt for guess
    string_high = window.get_font_height()
    prompt = "ENTER PASSWORD >"
    guess = prompt_user(window, prompt, location)
    attempts_left -= 1

    while guess != password and attempts_left > 0 :
        window.draw_string(str(attempts_left), 0, string_high)
        check_warning(window, attempts_left)
#       prompt for guess
        guess = prompt_user(window, prompt, location)
        attempts_left -= 1
    return guess


def create_outcome(window, guess, password):
    if guess == password:
        successful_outcome = ["EXITING DEBUG MODE", "", "LOGIN SUCCESSFUL - WELCOME\
 BACK", ""]
        prompt = "PRESS ENTER TO CONTINUE"
        return ([guess, ""] + successful_outcome, prompt)

    else:
        failure_outcome = ["LOGIN FAILURE - TERMINAL LOCKED", "", "PLEASE CONTACT \
AN ADMINISTRATOR", ""]
        prompt = "PRESS ENTER TO EXIT"
        return ([guess, ""] + failure_outcome, prompt)


def display_outcome(window, outcome):
    line_y = window.get_height() - 7 * window.get_font_height()
    line_y //= 2
    for line in outcome:
        line_x = window.get_width() - window.get_string_width(line)
        line_x //= 2
        display_line(window, line, [line_x, line_y])
        line_y += window.get_font_height()
    return line_y


def end_game(window, guess, password):
#   clear window
    window.clear()
    outcome = create_outcome(window, guess, password)
    line_y = display_outcome(window, outcome[0])

#   prompt for end
    line_x = window.get_width() - window.get_string_width(outcome[1])
    line_x //= 2
    window.input_string(outcome[1], line_x, line_y)

#   close window
    window.close()


main()
