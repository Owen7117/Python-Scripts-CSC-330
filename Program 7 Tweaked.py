# Owen O'Neil
# CSC 330
# Program 7 Tweaked: OTP

# Get necessary imports
import hmac
import hashlib
import time
import base64
from datetime import datetime


# Base32 shared secret
SECRET = "6R5MQOGNHBCD7CZBEHHYDEUBOJ4XWFI4HAGZJPQCFYXZQHS6BPUDTA5Y7VOKVFIIR6ZDFJ35I6UDMZBI4KLZHNJ2RLC6L7BK6KADG7I"
# Epoch time
EPOCH = "2001-11-13 13:43:20"
# OTP interval in seconds
INTERVAL = 30
# Convert secret into raw data, casefold allows lower case to be encoding
secret = base64.b32decode(SECRET, casefold=True)
# Convert the epoch into an integer, timestamp uses the seconds since 1970-01-01
epoch_time = int(datetime.strptime(EPOCH, "%Y-%m-%d %H:%M:%S").timestamp())
# Get the current counter value by dividing how many seconds have passed since the epoch by the interval
counter = (int(time.time()) - epoch_time) // INTERVAL
# Generate HMAC-SHA1 hash/20-byte raw hash output
hmac_hash = hmac.new(secret, counter.to_bytes(8, "big"), hashlib.sha1).digest()
# Extract the last byte of the hash (a value 0-15) and extract the lowest 4 bits of the byte(chat.gpt helped me understand why we do this)
offset = hmac_hash[-1] & 0xF
# Produce the 6 digit OTP by converting the bytes into a and intiger, masking with 0x7FFFFFFF and apply
# (chat.gpt also helped me understand this)
otp = (int.from_bytes(hmac_hash[offset:offset+4], "big") & 0x7FFFFFFF) % 1000000
# print the OTP
print(f"{otp:06d}")
