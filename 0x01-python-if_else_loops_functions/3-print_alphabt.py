#!/usr/bin/python3

# print alphabets in lower using ASCII except q & e
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
