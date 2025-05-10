# Owen O'Neil
# Program 2 Caesar
#2/7/2025


# Set the alphabet with a given list of characters
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#^()_+=/"
# Subroutine that decrypts the given inputs
def decrypt(ciphertext, key):
    # The final text that is returned
    plaintext = ""
    for char in ciphertext:
        # If the character in the text is in the alphabet
        if char in alphabet:
            # Get eth index of the character in the alphabet
            index = alphabet.index(char)
            # Get the new index by subtracting the index of the character by the key and then divide by the length of the alphabet to get teh remainder
            new_index = (index - int(key)) % len(alphabet)
            # That remainder will be the spot of the correct letter in the alphabet
            plaintext += alphabet[new_index]
        # If the character is not in the alphabet then just add it the plaintext string
        else:
            plaintext += char
    # Return the string
    return plaintext

### MAIN ###
# Get the input of the encryption key
key = input("Key: ")
# Set the file to a variable
encrypted_file = "challenge.txt"
# Open the file
with open(encrypted_file, "r") as f:
    lines = f.readlines()
    # For a line in the input file
    for line in lines:
        # Call the subroutine passing through the line and the key
        decrypted_text = decrypt(line, key)
        # Print the output
        print(decrypted_text)





