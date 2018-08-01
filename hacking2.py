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
window.set_bg_color("black")
window.set_font_name("couriernew")
window.set_font_size(18)
window.set_font_color('green')

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
guess = window.input_string("Enter password >", 0, line_y)

# end game
#   clear window
#   display faulure outcome
#       display guess
#       display blank line
#       display failure line 2
#       display blank line
#       display failure line 3
#       display blank line
# print("LOGIN FAILURE - TERMINAL LOCKED\n")
# print("PLEASE CONTACT AN ADMINISTRATOR\n")
#   prompt for end
# raw_input("PRESS ENTER TO EXIT")
#   close window
