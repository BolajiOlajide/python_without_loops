import math
import check

# create a dictionary mapping of alphabets to their indices and vice-versa
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# use this method to get the encrypted cipher of a character
def get_cipher_text(character, step):
    # check if the character passed is capitalized
    if character.isupper():
        # return the equivalent mapping using the dictionary above
        cipher_index = (letters.find(character) + step) % 26
        return letters[cipher_index]
    else:
        # since the character is in lower case , pass the upper case
        # equivalent to the dictionary algorithm for getting the cipher
        # then convert the cipher to lowercase
        cipher_index = (letters.find(character.upper()) + step) % 26
        return letters[cipher_index].lower()


# recursive method to encrypt every character in a text
def encrypt_text(text, step, result):
    # stop the recursion when an empty string is passed
    if len(text) == 0:
        # return the result
        return result
    # get the first character in the string and assing it to a temporary variable
    temp = text[0]
    # calculate the cipher of the first character and add it to the string stored in the result
    # variable
    result += get_cipher_text(temp, step)
    # keep calling the method recursively
    return encrypt_text(text[1:], step, result)


def caesar_encrypt(text, step):
    # initialize an empty string where the cipher text will be stored
    result = ""
    # call tjhe encryption method
    return encrypt_text(text, step, result)
