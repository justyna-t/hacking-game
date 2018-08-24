# Hacking Game V8

This is a text-based password guessing game that displays a list of potential
computer passwords. A player who consistently guess the password with one or
more attempts left would have the total attempts reduced from four. A player
who doesn't win often or at all with four guesses could be given more attempts.
When an incorrect password is entered, the game decrements the attempts left.
The game displays a lockout warning when the player has only one guess attempt
left. If the guess is correct the game display a success outcome, if the guess
is incorrect and player used all guesses the game display a failure outcome.

## How to run

```
$ python3 hacking8.py
```
