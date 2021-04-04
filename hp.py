import game

center=' '*75
centerlogo=' '*47
while True:
	fileHandle = open("logo.txt", "r")
	for line in fileHandle:
		print(centerlogo+line[:-1])
	fileHandle.close()
	print("")
	print('*'*168)
	print(center+"[1]   Start")
	print(center+"[2]   Hall of Fame")
	print(center+"[3]   Instructions")
	print(center+"[4]   Exit\n")
	print('*'*168)
	choice = input("Enter choice: ")

	if choice == "1":
		game.playGame()
	elif choice == "2":
		game.hallOfFameTitle()
		game.hallOfFame()
	elif choice == "3":
		game.help()
	elif choice == "4":
		break
	else:
		print("Invalid choice!")
		continue