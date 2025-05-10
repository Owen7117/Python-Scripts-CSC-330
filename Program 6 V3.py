# Owen O'Neil
# CSC 330
# Program 6 V3

# import scapy so that reading the cap file is possible
from scapy.all import *
from scapy.layers.inet import TCP

# Create an empty
msg = ""
# Create an empty array to put all the sequences to be deciphered
sequences = []
rec = False
# Set a variable for the file
packets = rdpcap("patsy.cap")

# for a packet in the file
for pkt in packets:
    # Ensure the packet has a payload
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        # Extract the data from the packet and set it to payload
        payload = pkt[Raw].load.decode(errors="ignore")


        # If the start word is in the payload
        if ("--BEGIN--") in payload:
            # Set the recording as true to start adding words to the final message
            rec = True

        # if the end word is in the payload
        elif ("--END--") in payload:
            # Set the recording as false to stop adding words to the final message
            rec = False

        # if the recording is true
        if rec:
            # Add the sequences(numbers) to the array while subtracting by one to get the correct message
            sequences.append(pkt[TCP].seq - 1)

# For a sequence number in sequences
for seq_num in sequences:
    # if the sequence number is not 0
    if seq_num != 0:
        # Convert the sequence number to binary
        b = bin(seq_num)[2:].zfill(32)
        i = 0
        while i < len(b):
            # Convert the binary to an ascii character number
            byte = int(b[i:i+8], 2)
            # Convert the ascii to a character
            char = chr(byte)
            # if the character is printable, add the character to the message
            if char in string.printable:
                msg += char
            #inciment i by 8 so that it will go to the next sequence
            i += 8

# print the final message
print(msg)
