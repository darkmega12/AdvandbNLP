
redListedWords = ["I", "I\'ll", "YOU\'LL", "You\'ll", "ON", "Of", "OF", "And", 
					"AND", "Will", "WILL", "Or", "OR", "This", "THIS", "That",
					"THAT"]

#returns the initial names of the people
def getInitialNames(dataList):
	names = []
	rule = ['vote', 'iboto']
	tempName = ""
	for tweet in dataList:	#iterates through all tweets
		tempName = finderAlgo(rule[0], tweet[2])
		if tempName != "":
			names.append(tempName)
		else:
			tempName = finderAlgo(rule[1], tweet[2])
			if tempName != "":
				names.append(tempName)
	return names

#algorithm for finding the names
def finderAlgo(toFind, message):
	name= ""
	if message.find(toFind) != -1:  #looks 
		tokenized = message.split(' ')
		for token in tokenized:
			if token.find(toFind) != -1 and tokenized.index(token) < len(tokenized):
				index = tokenized.index(token)
				name = searchNearProper(index, tokenized, 4, 'r')
				if name == "":
					name = searchNearProper(index, tokenized, 4, 'l')
	return name

# index refers to index in list of tokens
# tokenList referst to the tweet split by spaces
# movement refers to the range in which the definition will check the tokenList
#direction determines where the index would iterate to
def searchNearProper(index, tokenList, movement, direction):  #adds gets words that starts in capital letter from the number of moves and direction from the index
	name = ""
	mover = index
	moves = movement
	numNames = 2
	found = 0 #used to count how many words are found with proper noun
	if direction == 'r':
		mover += 1
		while mover < len(tokenList) and found < numNames and moves > 0:
			if len(tokenList[mover]) > 0: #gets first letter and checks if it is capital
				firstLetter = "" + tokenList[mover][0] 
				if firstLetter.isupper() == True:
					if found > 0:
						name += " "
					name += removeSpecialCharacters(tokenList[mover]) 
					found += 1
			moves -= 1
			mover += 1
	elif direction == 'l':
		index -= 1
		while mover >= 0 and found > numNames and moves > 0:
			if len(tokenList[mover]) > 0: #gets first letter and checks if it is capital
				firstLetter = "" + tokenList[mover][0]
				if firstLetter.isupper() == True:
					if found > 0:
						name = " " + name
					name = removeSpecialCharacters(tokenList[mover])  + name
					found += 1
			moves -= 1
			mover -= 1
	return name

def removeSpecialCharacters(word):
	newWord = word
	if newWord.find(",") != -1:
		newWord= newWord.replace(",", "")
	if word.find(".") != -1:
		newWord= newWord.replace(".", "")
	if word.find("!") != -1:
		newWord= newWord.replace("!", "")
	if word.find("?") != -1:
		newWord= newWord.replace("?", "")
	return newWord