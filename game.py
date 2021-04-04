import random

center=' '*75
centerhelp=' '*20
centerhof=' '*55

def playGame():
	while True:
		print("\n[1] Easy (2 points each) \n[2] Medium (3 points each) \n[3] Hard (5 points each)\n")
		names = []
		scores = []
		category = input("Enter category: ")
		if category == "1":
			scoring = 2
			filena = "easy.txt"
			categoryf(filena,scoring)
			break
		elif category == "2":
			scoring = 3
			filena = "medium.txt"
			categoryf(filena,scoring)
			break
		elif category == "3":
			scoring = 5
			filena = "hard.txt"
			categoryf(filena,scoring)
			break
		elif category == "menu":
			break
		elif category == "quit":
			exit()
		else:
			print("Invalid category!\n")
			continue

def categoryf(filena,scoring):
	score = 0
	lives = 3
	questionNum = 1
	questions = []
	answers = []
	count = 0
	fileHandle2 = open(filena,"r")		
	for line in fileHandle2:
		if count < 32:
			perLine = line[:-1].split(', ')
			questions.append(perLine[0])
			answers.append(perLine[1])
			count += 1

	while questionNum < 11:
		randNum = random.randint(0,len(questions)-1)
		print("Question #",questionNum,": ",questions[randNum])
		print("Score: ",score)
		print("Remaining lives: ",lives,"\n")
		answer = input("Answer: ")
		if answer.lower() == answers[randNum]:
			print("Correct!")
			score += scoring
			answers.pop(randNum)
			questions.pop(randNum)
			print("\n")
			questionNum += 1
		elif answer.lower() == "quit":
			exit()
		elif answer.lower() == "menu":
			break
		else:
			lives -= 1
			print("The correct answer is "+answers[randNum])
			print("\n\n")
			if lives == 0:
				print("GAME OVER")
				name = input("Enter your name: ")
				score = str(score)
				print("Final Score:", score)
				fileHandle4 = open("hallOfFame.txt", "a")
				fileHandle4.write(score + ", ")
				fileHandle4.write(name + "\n")
				fileHandle4.close()
				break
			else:
				answers.pop(randNum)
				questions.pop(randNum)
				questionNum += 1
		
		if questionNum == 11:
			name = input("Enter your name: ")
			print("You're a wizard", name,"!")
			score = str(score)
			print("Final Score:", score)
			fileHandle4 = open("hallOfFame.txt", "a")
			fileHandle4.write(score + ", ")
			fileHandle4.write(name + "\n")
			fileHandle4.close()
			break

def help():
	while True:
  		fileHandle3 = open("help.txt", "r")
  		for line in fileHandle3:
  			print(centerhelp+line[:-1])
  		fileHandle3.close() 
  		start = input("\nStart playing? (y): ").lower()
  		if start == "y":
  			playGame()
  			break
  		elif start == "quit":
  			exit()
  		elif start == "menu":
  			break
  		else:
  			print("Invalid choice!")
  			continue

def hallOfFameTitle():
	fileHandle5 = open("hoftitle.txt", "r")
	for line in fileHandle5:
		print(centerhof+line[:-1])
	print("\n\n")
	fileHandle5.close()

def hallOfFame():
	while True:
		hallOfFame = {}
		scoreKeys = []
		fileHandle4 = open("hallOfFame.txt", "r")
		for line in fileHandle4:
			perLine = line[:-1].split(", ")
			name = perLine[1]
			score = int(perLine[0])
			if score not in hallOfFame:
				hallOfFame[score] = [name]
			else:
				hallOfFame[score].insert(0,name)
	
		for e in hallOfFame.keys():
			scoreKeys.append(e)
		scoreKeys.sort(reverse = True)

		count = 0

		for k in scoreKeys:
			for n in hallOfFame[k]:
				if count < 5:
					print(center+n+"     ",k)
					count += 1
				else:
					print()
					print()
					break
		choice = input("\nGo to main menu? (y):")
		if choice.lower() == "y":
			break
		elif choice.lower() == "quit":
			exit()
		else:
			print("Invalid choice!")
			continue
		fileHandle4.close()