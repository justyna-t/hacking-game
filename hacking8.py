# Hacking Version 8
# This is a text-based password guessing game that displays a list of potential
# computer passwords. A player who consistently guess the password with one or
# more attempts left would have the total attempts reduced from four. A player
# who doesn't win often or at all with four guesses could be given more
# attempts. When an incorrect password is entered, the game decrements the
# attempts left. The game displays a lockout warning when the player has only
# one guess attempt left. If the guess is correct the game display a success
# outcome, if the guess is incorrect and player used all guesses the game
# display a failure outcome.

# Use uagame module
# Documentation for uagame is in file 'uagame_documentation.txt'
from uagame import Window
from time import sleep
from random import randint, choice
from file import check_file, save_file


def main():
    file_name = 'savefile'
    location = [0, 0]
    previous_attempts, attempts_left = check_file(file_name, ([], 4))
    window = create_window()
    display_header(window, location, attempts_left)
    password = display_password_list(window, location)
    guess, last_attempts_left = get_guesses(window, password, location,
                                            attempts_left)
    end_game(window, guess, password)
    attempts_next_play = adjust_difficulty(previous_attempts,
                                           last_attempts_left)
    data = (previous_attempts, attempts_next_play)
    save_file(file_name, data)


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


def create_password_list():
    # Create random selection of words for password list and return this list
    all_words = ["PROVIDE", "SETTING", "CANTINA", "CUTTING", "HUNTERS",
                 "SURVIVE", "HEARING", "HUNTING", "REALIZE", "NOTHING",
                 "OVERLAP", "FINDING", "PUTTING", "CAPTURE", "VIRTUAL",
                 "NETWORK", "SUSTAIN", "THEATRE", "DIAMOND", "RUNNING",
                 "GRIZZLY", "VISIBLE", "LOGICAL", "AIRLINE", "GATEWAY",
                 "VILLAGE", "FITNESS", "TRAFFIC", "WEEKEND", "BILLION",
                 "MISSION", "WRITTEN", "VEHICLE", "ADDRESS", "WELCOME"]
    password_list = []
    while len(password_list) < 13:
        password = all_words[randint(0, len(all_words) - 1)]
        password_list.append(password)
        all_words.remove(password)
    return password_list


def display_password_list(window, location):
    # Display the game passwords, update the location for the next text and
    #   return the correct password
    # - window is the Window to display in
    # - location is a list containing the int x and y coords of where the first
    # password should be displayed and it should be updated for the next output
    password_list = create_password_list()
    size = 20
    for password in password_list:
        password = embed_password(password, size)
        display_line(window, password, location)

    # display blank line
    display_line(window, "", location)

    # choose password
    return choice(password_list)


def embed_password(password, size):
    # Return a fixed length string with the password embedded somewhere in the
    # string and padded with symbol characters
    # - password is the str to pad
    # - size is the int number of characters in the padded
    fill = '!@#$%^*()-+=~[]{}'
    embedding = ""
    password_size = len(password)
    split_index = randint(0, size - password_size)
    for index in range(split_index):
        embedding += choice(fill)
    embedding += password
    for index in range(split_index + password_size, size):
        embedding += choice(fill)
    return embedding


def get_guesses(window, password, location, attempts_left):
    # Input multiple guesses by the player and provide feedback and return the
    # player's final guess and attempts left after final guess
    # - window is the Window to display in
    # - password is the str correct password
    # - location is a list containing the int x and y coords of where the first
    # password prompt should be displayed
    # - attempts_left is the number of guesses left

    # prompt for guess
    prompt = "ENTER PASSWORD >"
    guess = prompt_user(window, prompt, location)
    attempts_left -= 1
    hint_x = window.get_width() // 2
    hint_location = [hint_x, 0]
    while guess != password and attempts_left > 0:
        # get next guess
        window.draw_string(str(attempts_left), 0, window.get_font_height())
        check_warning(window, attempts_left)
        display_hint(window, password, guess, hint_location)
        guess = prompt_user(window, prompt, location)
        attempts_left -= 1
    return guess, attempts_left


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


def display_hint(window, password, guess, location):
    # Display the game hint after an incorrect password is entered
    # - window is the Window to display in
    # - password is the str correct password
    # - guess is the player's guess str
    # - location is a tuple containing the int x and int y coords of where the
    # hint should be displayed and it should be updated to one "line" below
    # the top left corner of the displayed hint
    index = 0
    correct = 0
    for letter in guess:
        if index < len(password) and letter == password[index]:
            correct += 1
        index += 1
    hint = "%d/7 IN MATCHING POSITIONS" % correct
    display_line(window, guess + " INCORRECT", location)
    display_line(window, hint, location)


def end_game(window, guess, password):
    # End the game by displaying the outcome and prompting for an enter
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
    # the outcome
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
    # the guess equals the password or not and return the tuple containing the
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


def adjust_difficulty(previous_attempts, last_attempts_left):
    # Increase or decrease the difficulty of the game deppending on previous
    # plays and return attempts for the next play
    # - previous_attempts a list containing the last_attempts_left for the
    # maximal three previous games
    # - last_attempts_left is the number of guesses left after final guess
    if len(previous_attempts) < 2:
        previous_attempts.append(last_attempts_left)
        return 4
    elif len(previous_attempts) == 2:
        previous_attempts.append(last_attempts_left)
        return check_last_games(previous_attempts)
    else:
        previous_attempts.append(last_attempts_left)
        previous_attempts.pop(0)
        return check_last_games(previous_attempts)


def check_last_games(previous_attempts):
    # Check previous attempt and return attempts for the next play
    # - previous_attempts a list containing the last_attempts_left for the
    # maximal three previous games
    score = 0
    for attempt in previous_attempts:
        if attempt >= 1:
            score += 1
    if score == 3:
        return 2
    elif score <= 1:
        return 6
    else:
        return 4


main()
