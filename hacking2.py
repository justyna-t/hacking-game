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

# display header
window.draw_string("DEBUG MODE", 0, 0)
window.update()
sleep(0.3)
window.draw_string("1 ATTEMPT(S) LEFT\n", 0, 10)
window.update()
sleep(0.3)


# display password
# print("PROVIDE\nSETTING\nCANTINA\nCUTTING\nHUNTERS\nSURVIVE")
# print("HEARING\nHUNTING\nREALIZE\nNOTHING\nOVERLAP\nFINDING\nPUTTING\n")

# prompt for guess
# raw_input("Enter password >")

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
