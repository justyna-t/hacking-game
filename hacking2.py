# Hacking Version 2
# This is a text-based password guessing game that displays a list of potential
# computer passwords. The player is allowed 1 attempt to guess the password.
# The game indicates that the player failed to guess the password correctly.

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
line_y = 0
string_high = window.get_font_height()
window.draw_string("DEBUG MODE", 0, line_y)
window.update()
line_y += string_high
sleep(0.3)
window.draw_string("1 ATTEMPT(S) LEFT", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high


# display password
window.draw_string("PROVIDE", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("SETTING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("CANTINA", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("CUTTING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("HUNTERS", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("SURVIVE", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("HEARING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("HUNTING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("REALIZE", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("NOTHING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("OVERLAP", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("FINDING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("PUTTING", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
window.draw_string("", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
# prompt for guess
guess = window.input_string("ENTER PASSWORD >", 0, line_y)

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
window.draw_string("", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display failure line 2
#           compute x coordinate
string = "LOGIN FAILURE - TERMINAL LOCKED"
line_x = window_width - window.get_string_width(string)
line_x //= 2

window.draw_string(string, line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display blank line
window.draw_string("", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display failure line 3
#           compute x coordinate
string = "PLEASE CONTACT AN ADMINISTRATOR"
line_x = window_width - window.get_string_width(string)
line_x //= 2

window.draw_string(string, line_x, line_y)
window.update()
sleep(0.3)
line_y += string_high
#       display blank line
window.draw_string("", 0, line_y)
window.update()
sleep(0.3)
line_y += string_high
#   prompt for end
#           compute x coordinate
string = "PRESS ENTER TO EXIT"
line_x = window_width - window.get_string_width(string)
line_x //= 2

window.input_string(string, line_x, line_y)
#   close window
window.close()
