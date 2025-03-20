# TODO-1: Import and print the logo from art.py when the program starts.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, encode_or_decode):
    output_result = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_result += letter
        else:
            letter_position = (alphabet.index(letter) + shift_amount) % 26
            output_result += alphabet[letter_position]
    print(f"Here is the {encode_or_decode}d result: {output_result}\n")

# TODO-3: Can you figure out a way to restart the cipher program?

go_again = True
while go_again:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart_cipher = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart_cipher == 'no':
        go_again = False
        print("Goodbye")