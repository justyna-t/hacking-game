# Hacking Version 5
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

# create window
window = Window("Hacking", 600, 500)
window.set_font_name("couriernew")
window.set_font_size(18)
window.set_font_color("green")
window.set_bg_color("black")

# get window height and width
window_height = window.get_height()
window_width = window.get_width()

# display header
line_x = 0
line_y = 0
string_high = window.get_font_height()
#    for header line in header
attempts = 4
header = ["DEBUG MODE", "%d ATTEMPT(S) LEFT" % attempts, ""]
for header_line in header:
    window.draw_string(header_line, line_x, line_y)
    window.update()
    line_y += string_high
    sleep(0.3)

# display password
#   for password in password list
password_list = ["PROVIDE", "SETTING", "CANTINA", "CUTTING", "HUNTERS",
                 "SURVIVE", "HEARING", "HUNTING", "REALIZE", "NOTHING",
                 "OVERLAP", "FINDING", "PUTTING", ""]
for password in password_list:
    window.draw_string(password, line_x, line_y)
    window.update()
    sleep(0.3)
    line_y += string_high

# choose password
password = password_list[7]

# get guesses
#   prompt for guess
guess = window.input_string("ENTER PASSWORD >", line_x, line_y)
line_y += string_high
attempts -= 1

#   get guess until it is not equal password and attempts left greater than 0
while guess != password and attempts > 0:
    window.draw_string(str(attempts), 0, string_high)

#       check warning
    if attempts == 1:
        message = "*** LOCKOUT WARNING ***"
        x = window_width - window.get_string_width(message)
        y = window_height - string_high
        window.draw_string(message, x, y)

#       prompt for guess
    guess = window.input_string("ENTER PASSWORD >", line_x, line_y)
    line_y += string_high
    attempts -= 1

# end game
#   clear window
window.clear()

#   display outcome
#       for outcome in outcome list
#           compute y coordinate for every line
line_y = window_height - 7 * string_high
line_y //= 2
outcome_list = [guess, ""]
if guess == password:
    successful_outcome = ["EXITING DEBUG MODE", "", "LOGIN SUCCESSFUL - WELCOME\
 BACK", ""]
    outcome_list += successful_outcome
    prompt = "PRESS ENTER TO CONTINUE"

else:
    failure_outcome = ["LOGIN FAILURE - TERMINAL LOCKED", "", "PLEASE CONTACT \
AN ADMINISTRATOR", ""]
    outcome_list += failure_outcome
    prompt = "PRESS ENTER TO EXIT"

for outcome in outcome_list:
#   compute x coordinate
    line_x = window_width - window.get_string_width(outcome)
    line_x //= 2

    window.draw_string(outcome, line_x, line_y)
    window.update()
    sleep(0.3)
    line_y += string_high

#   prompt for end
#           compute x coordinate
line_x = window_width - window.get_string_width(prompt)
line_x //= 2

window.input_string(prompt, line_x, line_y)

#   close window
window.close()
