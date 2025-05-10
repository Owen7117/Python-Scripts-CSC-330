# Owen O'Neil
# Program 1: Binary
# 2/7/2025
# This code converts the binary lines in a given input file and converts them to their corresponding ascii characters

# Initialize the plain text string
plain_text = ""
# Give the input file a variable
input = ("Challenge3.txt")
# open the input file
with open(input, 'r') as f:
    # read the input file line by line
    lines = f.readlines()
    # for a line in the file
    for line in lines:
        # delete the new lines
        line = line.strip()
        # if the line length is divisible by seven with no remainder (7-bits)
        if len(line) % 7 == 0:
            # initialize chunks variable
            chunks = []
            for i in range(0, len(line), 7):
                # Take chunks of the line by seven characters each time and add them to the array
                chunks.append(line[i:i + 7])
            # where the final words will be placed
            decoded_line = ""
            for binary in chunks:
                # join the final converted characters for every binary chunk in chunks
                decoded_line += chr(int(binary, 2))
                # print the decoded line
            print(decoded_line)

        else:
            #if the length of the line is divisible by eight with no remainder (8-bits)
            if len(line) % 8 == 0:
                # initialize chunks variable
                chunks = []
                for i in range(0, len(line), 8):
                    # Take chunks of the line by seven characters each time and add them to the array
                    chunks.append(line[i:i + 8])
                # where the final words will be placed
                decoded_line = ""
                for binary in chunks:
                    # join the final converted characters for every binary chunk in chunks
                    decoded_line += chr(int(binary, 2))
                    # print the decoded line
                print(decoded_line)


