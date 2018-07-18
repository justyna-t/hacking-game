# Hacking Version 1
# This is a text-based password guessing game that displays a list of potential
# computer passwords. The player is allowed 1 attempt to guess the password.
# The game indicates that the player failed to guess the password correctly.

# display header
print("DEBUG MODE")
print("1 ATTEMPT(S) LEFT\n")

# display password
print("PROVIDE\nSETTING\nCANTINA\nCUTTING\nHUNTERS\nSURVIVE")
print("HEARING\nHUNTING\nREALIZE\nNOTHING\nOVERLAP\nFINDING\nPUTTING\n")

# prompt for guess
raw_input("Enter password >")

# end game
#   display faulure outcome
print("LOGIN FAILURE - TERMINAL LOCKED\n")
print("PLEASE CONTACT AN ADMINISTRATOR\n")
#   prompt for end
raw_input("PRESS ENTER TO EXIT")
