# write a python program to translate a message into secret code language.
# Use the rules below to translate normal english into secret code language

# Coding:
# if word contains at least 3 characters, remove the first letter and append it at the end.
# now append three random characters at the starting and the end
# else:
#   simply reverse the string


# Decoding:
# if the word contains less than 3 characters then just reverse it.
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

#  your program should ask whether you want to code or decode

import random
import string


def generate_random_chars():
    """
    Generate three random characters
    """
    # Choose 3 random alphanumeric characters
    three_Char = random.choices(string.ascii_letters + string.digits, k=3)
    return ''.join(three_Char)  # Join the list into a string and return


def encoded_message(message):
    """
    Encode the message into the secret code language.
    """
    words = message.split()  # Split the message into words
    encoded_words = []  # Initialize a list to store encoded words

    for word in words:
        if len(word) >= 3:  # For words with 3 or more characters
            # Remove the first character, append it to the end, and add random chars at start and end
            encoded_word = word[1:] + word[0]
            encoded_word = generate_random_chars() + encoded_word + generate_random_chars()
        else:  # For words with less than 3 characters, reverse the word
            encoded_word = word[::-1]
        encoded_words.append(encoded_word + ' ')  # Add a space after each encoded word

    return ''.join(encoded_words)  # Join all encoded words into a single string


def decoded_message(message):
    """
    Decode the secret code language back into the original message.
    """
    words = message.split()  # Split the encoded message into words
    decoded_words = []  # Initialize a list to store decoded words

    for word in words:
        if len(word) < 3:  # For words with less than 3 characters, reverse the word
            decoded_word = word[::-1]
        else:  # For words with 3 or more characters
            # Remove 3 characters from start and end, then move the last letter to the beginning
            core_word = word[3:-3]
            decoded_word = core_word[-1] + core_word[:-1]
        decoded_words.append(decoded_word + ' ')  # Add a space after each decoded word

    return ''.join(decoded_words)  # Join all decoded words into a single string


# Main program loop
while True:
    print("\nWelcome to the 'Secret Code Translator!'")
    # Ask the user if they want to code, decode, or quit
    choice = input("Do you want to 'code' or 'decode' a message or press 'q' to quit? : ").strip().lower()

    if choice == 'q':  # Exit the program if the user chooses to quit
        print("\nThank you for using the Secret Code Translator! Goodbye!")
        break

    if choice == 'code':  # If the user wants to encode a message
        message = input("Enter the message to encode: ").strip()
        print("Encoded Message: ", encoded_message(message))
    elif choice == 'decode':  # If the user wants to decode a message
        message = input("Enter the message to decode: ").strip()
        print("Decoded Message: ", decoded_message(message))
    else:  # If the input is invalid
        print("Invalid choice. Please choose 'code', 'decode', or 'q'.")