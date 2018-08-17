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
    # Create a window for the game, open it and return it
    window = Window("Hacking", 600, 500)
    window.set_font_name("couriernew")
    window.set_font_size(18)
    window.set_font_color("green")
    window.set_bg_color("black")
    return window


def display_header(window, location, attempts):
    # Display the game header
    # - window is the Window to display in
    # - location is a list containing the int x and y coords of where the
    # header should be displayed and it should be updated for the next output
    # - attempts is the number of guesses allowed
    header = ["DEBUG MODE", "%d ATTEMPT(S) LEFT" % attempts, ""]
    for header_line in header:
        display_line(window, header_line, location)


def display_line(window, string, location):
    # Display a string in the window and update the location
    # - window is the Window to display in
    # - string is the str to display
    # - location is a tuple containing the int x and int y coords of where the
    # string should be displayed and it should be updated to one "line" below
    # the top left corner of the displayed string
    window.draw_string(string, location[0], location[1])
    window.update()
    location[1] += window.get_font_height()
    sleep(0.3)


def display_password_list(window, location):
    # Display the game passwords, update the location for the next text and
    #   return the correct password
    # - window is the Window to display in
    # - location is a list containing the int x and y coords of where the first
    # password should be displayed and it should be updated for the next output
    password_list = ["PROVIDE", "SETTING", "CANTINA", "CUTTING", "HUNTERS",
                     "SURVIVE", "HEARING", "HUNTING", "REALIZE", "NOTHING",
                     "OVERLAP", "FINDING", "PUTTING", ""]
    for password in password_list:
        display_line(window, password, location)

#   choose password
    return password_list[7]


def get_guesses(window, password, location, attempts_left):
    # Input multiple guesses by the player and provide feedback. Return the
    # player's final guess.
    # - window is the Window to display in
    # - password is the str correct password
    # - location is a list containing the int x and y coords of where the first
    # password prompt should be displayed
    # - attempts_left is the number of guesses left

    # prompt for guess
    prompt = "ENTER PASSWORD >"
    guess = prompt_user(window, prompt, location)
    attempts_left -= 1

    while guess != password and attempts_left > 0:
        # get next guess
        window.draw_string(str(attempts_left), 0, window.get_font_height())

        check_warning(window, attempts_left)
        guess = prompt_user(window, prompt, location)
        attempts_left -= 1
    return guess


def prompt_user(window, prompt, location):
    # Draw a prompt, input a string that the user types and return the string
    # - window is the Window to display in
    # - prompt is the str to display
    # - location is a tuple containing the int x and int y coords of where the
    # prompt should be displayed and it should be updated to one "line" below
    # the top left corner of the displayed prompt
    guess = window.input_string(prompt, location[0], location[1])
    location[1] += window.get_font_height()
    return guess


def check_warning(window, attempts_left):
    # Check whether a lockout warning should be displayed and if so, display it
    # - window is the Window to display in
    # - attempts_left is the number of guesses left
    if attempts_left == 1:
        # display warning
        message = "*** LOCKOUT WARNING ***"
        x = window.get_width() - window.get_string_width(message)
        y = window.get_height() - window.get_font_height()
        window.draw_string(message, x, y)


def end_game(window, guess, password):
    # End the game by displaying the outcome and prompting for an enter.
    # - window is the Window to display in
    # - guess is the player's guess str
    # - password is the correct password string

    # clear window
    window.clear()

    # create outcome
    outcome = create_outcome(window, guess, password)

    # display outcome
    line_y = display_outcome(window, outcome[0])

    # prompt for end
    line_x = count_line_x(window, outcome[1])
    prompt_user(window, outcome[1], [line_x, line_y])

    # close window
    window.close()


def display_outcome(window, outcome):
    # Display the outcome of the game and return the location of the line below
    # the outcome.
    # - window is the Window to display in
    # - outcome is the list of strings
    line_y = window.get_height() - 7 * window.get_font_height()
    line_y //= 2
    for line in outcome:
        line_x = count_line_x(window, line)
        display_line(window, line, [line_x, line_y])
        line_y += window.get_font_height()
    return line_y


def count_line_x(window, string):
    #  Compute x coordinate depending on string lenght and return x coordinate
    # - window is the Window to display in
    # - string is the str to compute its length
    line_x = window.get_width() - window.get_string_width(string)
    line_x //= 2
    return line_x


def create_outcome(window, guess, password):
    # Create the outcome of the game: success or failure depending on whether
    # the guess equals the password or not. Return the tuple containing the
    # list of strings and prompt string
    # - window is the Window to display in
    # - guess is the player's guess str
    # - password is the correct password string
    if guess == password:
        # create success
        successful_outcome = ["EXITING DEBUG MODE", "", "LOGIN SUCCESSFUL - \
WELCOME BACK", ""]
        prompt = "PRESS ENTER TO CONTINUE"
        return ([guess, ""] + successful_outcome, prompt)

    else:
        # create failure
        failure_outcome = ["LOGIN FAILURE - TERMINAL LOCKED", "", "PLEASE \
CONTACT AN ADMINISTRATOR", ""]
        prompt = "PRESS ENTER TO EXIT"
        return ([guess, ""] + failure_outcome, prompt)


main()
