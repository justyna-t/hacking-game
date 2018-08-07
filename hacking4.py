# Hacking Version 4
# This is a text-based password guessing game that displays a list of potential
# computer passwords. The player is allowed 1 attempt to guess the password.
# If the guess is correct the game display a success outcome, if the guess is
# incorrect the game display a failure outcome.

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

# display header
line_x = 0
line_y = 0
string_high = window.get_font_height()
window.draw_string("DEBUG MODE", line_x, line_y)
window.update()
line_y += string_high
sleep(0.3)
window.draw_string("1 ATTEMPT(S) LEFT", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high


# display password
window.draw_string("PROVIDE", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("SETTING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("CANTINA", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("CUTTING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("HUNTERS", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("SURVIVE", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("HEARING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("HUNTING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("REALIZE", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("NOTHING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("OVERLAP", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("FINDING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("PUTTING", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
# prompt for guess
guess = window.input_string("ENTER PASSWORD >", line_x, line_y)

# end game
#   clear window
window.clear()
#   display failure outcome
#       display guess
#           compute y coordinate for every line
window_height = window.get_height()
line_y = window_height - 7 * string_high
line_y //= 2
#           compute x coordinate
window_width = window.get_width()
line_x = window_width - window.get_string_width(guess)
line_x //= 2

window.draw_string(guess, line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display blank line
window.draw_string("", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high

#       display failure line 2
if guess == "HUNTING":
    outcome_line2 = "EXITING DEBUG MODE"
    outcome_line3 = "LOGIN SUCCESSFUL - WELCOME BACK"
    outcome_line4 = "PRESS ENTER TO CONTINUE"
else:
    outcome_line2 = "LOGIN FAILURE - TERMINAL LOCKED"
    outcome_line3 = "PLEASE CONTACT AN ADMINISTRATOR"
    outcome_line4 = "PRESS ENTER TO EXIT"
#           compute x coordinate
line_x = window_width - window.get_string_width(outcome_line2)
line_x //= 2

window.draw_string(outcome_line2, line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display blank line
window.draw_string("", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display failure line 3
#           compute x coordinate
line_x = window_width - window.get_string_width(outcome_line3)
line_x //= 2

window.draw_string(outcome_line3, line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display blank line
window.draw_string("", line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#   prompt for end
#           compute x coordinate
line_x = window_width - window.get_string_width(outcome_line4)
line_x //= 2

window.input_string(outcome_line4, line_x, line_y)
#   close window
window.close()
