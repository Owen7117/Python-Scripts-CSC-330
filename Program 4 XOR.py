# Owen O'Neil
# Program 4 XOR
# 2/17/25

# subroutine that deciphers using the XOR operator
def xor_decrypt(cipher_text, key):
    # string where the final output will go
    plain_text = bytearray()
    # for a character in the range of the cyphertext
    for i in range(len(cipher_text)):
        # add the new character using the XOR operator given the character in the cyphertext and the character in the key
        plain_text += bytearray(cipher_text[i] ^ key[i % len(key)])
    # return the final array
    return plain_text


# subroutine that allows multiple files to be opened
def open_file(input_file):
    # open the file using the input passed through and the read binary function
    with open(input_file, 'rb') as f:
        # read the lines and strip them
        return f.read().strip()

# set the key file to a variable
key = open_file("2025-05-05-10_59_14-key2")
# set the image output to a variable
image = open_file("2025-05-05-10_59_36-key4")

decrypted_data = xor_decrypt(image, key)
print(decrypted_data)
with open("fin.bmp", "w") as f:
    f.write(decrypted_data)

