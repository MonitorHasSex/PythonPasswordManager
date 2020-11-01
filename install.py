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
	print("Ok. If you want to generate a new key/password, please do it in the PPm script. Goodbye.")
elif answer == "n":
	print('Ok, lets set you up.')
	keygen = Fernet.generate_key()
	file3 = open('key.key','wb')
	file3.write(keygen)
	file3.close()
	file3 = open('key2.key','wb')
	file3.write(keygen)
	file3.close()
	file = open('sw.key','wb')
	file.write(keygen)
	file.close()
	file2 = open('sw2.key','wb')
	file2.write(keygen)
	file2.close()
	pas = input("Type in your desired password here: ")
	file1 = open('sw.key','rb')
	file_1 = file1.read()
	file1.close()
	encoded = pas.encode()
	f2 = Fernet(file_1)
	encrypted = f2.encrypt(encoded)
	file2 = open('sw2.key','rb')
	file_2 = file2.read()
	file2.close()
	f3 = Fernet(file_2)
	encrypted2 = f3.encrypt(encrypted)
	file4 = open('bel.txt','wb')
	file4.write(encrypted2)
	file4.close()
	lists = open("list.txt", "w")
	lists.write("List File: " + "\n")
	lists.close()
	print("Alright, your all setup. Now all you have to do is run PPm.exe. Have fun i guess lol.")