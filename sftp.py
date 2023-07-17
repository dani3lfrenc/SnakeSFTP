
import pysftp
import colorama
from colorama import Fore




def secondOption():

	with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
		print("Connection successfully established ... ")

		remoteFilePath = input("Paste the path to the original file: ")

		localFilePath = input("Paste the path to the destination file: ") 

		# Use the get method to download a file
		sftp.get(remoteFilePath, localFilePath)

		print(Fore.GREEN + "\nOperation performed successfully!\n")


def firstOption():


	with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
	    
	    print("Connection successfully established...")

	    localFilePath = input("Paste the path to the original file: ")


	    remoteFilePath = input("Paste the path to the destination file: ")

	    sftp.put(localFilePath, remoteFilePath)

	    print("File loaded successfully.")




print(Fore.CYAN + "==================SNAKESFTP==================\n")
print(Fore.WHITE + "\n Before you start, you need to set some parameters:\n")
Hostname = input("\nEnter the HOSTNAME: ")
Username = input("\nEnter the USERNAME: ")
Password = input("\nEnter the PASSWORD: ")
print("\n\nPerfect!")



while (True):


	choice = input(Fore.WHITE + "\n\n1) Send a file to the terminal\n2) Get a file from the terminal\n\nChoice:")
	if choice == "1":

		firstOption()

	elif choice == "2":

		secondOption()
	

	elif choice != "1" or choice != "2":
		break






