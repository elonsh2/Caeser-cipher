from art import *
import os
from english_words import *

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

def crack(text):
    crack_list = text.split()
    for i in range(1, len(alphabet)):
        final_cracked = []
        for word in crack_list:
            end_text = ''
            for char in word:
                if not char.isalpha():  # checks if char is not a letter. if it is it won't shift
                    end_text += char
                else:
                    position = alphabet.index(char)
                    new_position = (position + i) % 26
                    new_letter = alphabet[new_position]
                    end_text += new_letter
            if end_text in wordlist:
                final_cracked.append(end_text)
        if len(crack_list)/2 <= len(final_cracked) <= len(crack_list):
            print(f"The cracked text is: '{' '.join(final_cracked)}'")
    input()




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
right_input = True
wordlist = load_words('all_words.txt')
while True:
    right_input = True
    cls()
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, "
                      "type 'crack' to crack the code:\n").lower()
    text = input("Type your message:\n").lower()
    if direction == "crack":
        crack(text)
        input()
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
