# Owen O'Neil
# Program 8 GSteg
# 4/6/25

# Import the date time
from datetime import datetime

# open the file and reads into a byte array
with open("B32768-input.txt.bin", "rb") as f:
    data = bytearray(f.read())

# Finds the starting index of the hidden section using STEG
HSIG = data.find(b"STEG")
# Finds the first null byts after the STEG assuming it ends with a null byte
null = data.find(b"\x00",HSIG + 4)
# Decodes the data from the start of the hidden section until the end and converts it to ascii(this is the file name)
FNAME = data[HSIG + 4:null].decode("ascii")
# finds the L8R marker which marks the end of the header section and the start of the actual file data
HEND = data.index(b"L8R",HSIG + 4)
# Reads the length of the hidden file and is stored as a big-endian int
DLEN = int.from_bytes(data[null + 1:HEND], byteorder = "big")
# Extracts the actual hidden data from the file starting right after the L8R marker and continuing for DLEN bytes.
needle = data[HEND + 3:HEND + 3 + DLEN]
# Gets the current time formated properly
t = datetime.now().strftime("%Y%m%d-H%M%S")
# Creates a new file with the date and time as the file name and contains all decoded data
with open(f"{t}-{FNAME}", "wb") as f:
    f.write(needle)
