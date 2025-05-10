# Owen O'Neil
# CSC 330
# Program 6 V4
import string

# import scapy so that reading the cap file is possible
from scapy.all import *
from scapy.layers.inet import TCP

# Create an empty
msg = ""
# Set a variable for the file
packets = rdpcap("patsy.cap")


for pkt in packets:
    # Ensure the packet has a payload
    if pkt.haslayer(TCP):
        # Get the sequence number by extracting the sequence number
        seq_num = pkt[TCP].seq

        # if the sequence number is not 0
        if seq_num != 0:
            # Convert the sequence number to binary
            b = bin(seq_num - 1)[2:].zfill(32)
            # For the length of the sequence and jumping by 8
            for i in range(0, len(b), 8):
                # Convert the binary to an ascii number and then a character and join it to the message array
                if (chr(int(b[i:i + 8], 2)) in string.printable):
                    text = "".join(chr(int(b[i:i + 8], 2)))
                    msg += text

        # Find the start word in the message and move 4 characters ot the right so that it is not included in the message
        start = msg.find("COMB") + 4
        # Find the stop word in the message by looking for it after teh start word
        end = msg.find("COME", start)

# If the start and end word is not the last string in the array
if start != -1 and end != -1:
    # Take the text inbetween the start and stop word
    extracted_text = msg[start:end]
    # print the extracted text
    print(extracted_text)
