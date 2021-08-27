from art import *
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def caesar(text, shift, direction):
    end_text = ''
    if direction == "decode":
        shift *= -1  # for decoding the shift is minus
    for char in text:
        if not char.isalpha():  # checks if char is not a letter. if it is it won't shift
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = (position + shift) % 26  # shifts char to new position
            new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"The {direction}d text is: '{end_text}'")
    input()


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
right_input = True
while True:
    right_input = True
    cls()
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Type the shift number, between 1 and 25:\n"))
    except ValueError:
        right_input = False
    while right_input:
        if (direction == "encode" or direction == "decode") and 0 < shift < len(alphabet):
            caesar(text, shift, direction)
            right_input = False
        else:
            print("Wrong input. Type again")
            input()
            right_input = False
