# Owen O'neil
# Program 5 FTP Directory Listing


# FTP Directory Listing
# Author: Dr. Jean Gourd
# Shows how to use Python to connect to an FTP server and list directory contents.
# Set the variables below as appropriate.

from ftplib import FTP

# FTP server details
IP = "10.0.222.38"
PORT = 33333
USER = "anonymous"
PASSWORD = "simple@abcdefg.com"
FOLDER = ("2025-05-05-10_57_57-key1")
key = 24
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
#files=ftp.retrlines("LIST -al")
ftp.dir(files.append)
# exit the FTP server
ftp.quit()

# sort the files by filename, ignoring case
#files = sorted(files, key=lambda x: x[56:].lower())

#with open("message (1).txt", "r") as f:
# files = f.read().splitlines()

# display the folder contents
for f in files:
	if key == 7:
		if f[:3] == "---":
			perms = f[3:10]
			perms = perms.replace("-","0")
			perms = perms.replace("r","1")
			perms = perms.replace("w","1")
			perms = perms.replace("x","1")
			print(perms, end="")

	if key == 10:
		perms = f[:10]
		perms = perms.replace("-","0")
		perms = perms.replace("r","1")
		perms = perms.replace("w","1")
		perms = perms.replace("x","1")
		perms = perms.replace("d","1")
		print(perms, end="")

