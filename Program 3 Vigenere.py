# Owen O'Neil
# Program 3 Vigenere
# 2/12/25

# set alphabet
alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?/>.<,\"':;|\\}]{[+=_-)(*&^%$#@!~`abcdefghijklmnopqrstuvwxyz"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# subroutine that decrypts the encrypted message
def decrypt(cypher_text, key):
    # where final text will be stored
    plain_text = ""
    # for a character in the cypher text
    i=0
    for line in cypher_text:
        # index # for key
        for char in line:
            # if the character is in the alphabet
            if char in alphabet:
                # get the key character and make sure it loops back if at the end of the key
                key_char = key[i]
                # get the index of the cyphertext character in the alphabet
                index_alpha = alphabet.index(char)
                # get the index of the key character in the alphabet
                index_key = alphabet.index(key_char)
                # get the deciphered character
                decrypted_index = (index_alpha - index_key ) % len(alphabet)
                # add the character to the plaintext string
                plain_text += alphabet[decrypted_index]
                # increment the key index by 1
                i = (i+1) % len(key)
            # if the character is not in the alphabet then add it to the plain text string
            else:
                plain_text += char
    # return the final string
    return plain_text

# get the Key
key = input("Enter your key (No Spaces): ")
# set the input file to a variable
encrypted_file = "Challenge 2 vigenere input.txt"
# open the input file
with open(encrypted_file, "r") as f:
    # read the lines of the file
    lines = f.readlines()
    # call the subroutine while passing through the line with no newline characters and also passing through the key
    plaintext = decrypt(lines, key)
    # print the output
    print(plaintext)
with open("message1.txt", "w") as f:
    f.write(plaintext)
