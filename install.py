from cryptography.fernet import Fernet
print('''
 /$$$$$$$  /$$$$$$$                       /$$$$$$              /$$                        
| $$__  $$| $$__  $$                     /$$__  $$            | $$                        
| $$  \ $$| $$  \ $$ /$$$$$$/$$$$       | $$  \__/  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$ 
| $$$$$$$/| $$$$$$$/| $$_  $$_  $$      |  $$$$$$  /$$__  $$|_  $$_/  | $$  | $$ /$$__  $$
| $$____/ | $$____/ | $$ \ $$ \ $$       \____  $$| $$$$$$$$  | $$    | $$  | $$| $$  \ $$
| $$      | $$      | $$ | $$ | $$       /$$  \ $$| $$_____/  | $$ /$$| $$  | $$| $$  | $$
| $$      | $$      | $$ | $$ | $$      |  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/| $$$$$$$/
|__/      |__/      |__/ |__/ |__/       \______/  \_______/   \___/   \______/ | $$____/ 
                                                                                | $$      
                                                                                | $$      
                                                                                |__/
Hello,Welcome to The PPm Setup script!
''')
answer = input("Have you set this up before(y/n)?:")
if answer == "y":
	print("Ok. If you want to generate a new key/password, please do it in the program. Thanks and goodbye.")
elif answer == "n":
	print("Alright, lets get you setup")
	dgha = Fernet.generate_key()
	ilqe = open('key.key','wb')
	ilqe.write(dgha)
	ilqe.close()
	print("Setup the first key file...")
	dghea = Fernet.generate_key()
	ilqee = open('key2.key','wb')
	ilqee.write(dghea)
	ilqee.close()
	print("Setup the second key file...")
	file = open('key2.key','rb')
	key = file.read()
	file.close()
	password = input("What would you like the password to be?: ")
	encoded = password.encode()
	f = Fernet(key)
	encrypted = f.encrypt(encoded)
	felte = open('pas.txt', 'wb')
	felte.write(encrypted)
	felte.close()
	print("Setup the password...")
	lists = open("list.txt", "w")
	lists.write("List File: ")
	lists.close()
	print("Made the password list txt...")
	print("Alright, your all setup! now all you have to do is run the PPm.py file in cmd. Have fun i guess lol.")