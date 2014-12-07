import csv


keyWords = ["Vote", "VOTE", "vote", "boto", "iboto", "bumoto", 
			"Halalan", "halalan", "senator", "Senator", "elect", 
			"Mayor", "mayor", "Eleksyon", "eleksyon"]



filename = 'C:\\Users\\Kiel\\Dropbox\\3RD YEAR\\2ND TERM\\ADVANDB\\filtered-may1-onwards.csv'

def getDataFromCSV(filename):
	CSVfile = open(filename, 'rt', encoding = 'utf8')   #opens the csv file and encodes to utf8
	reader = csv.reader(CSVfile, dialect = 'excel', delimiter = ',') #reads the file
	filteredData = []
	tempData = []
	first = True
	day = 1 #used in finding the date of tweet; for getting the first index in the csv file per day
	for row in reader:
		if first == True: #is done so that first row, which is the headers, is not added to tempData
			first = False
			continue
		#following code gets the first index of the dates and adds each consecutively in startDates
		if day < 10:
			if row[3].find('May 0' + str(day)) == -1:
				day += 1
				filteredData.append(tempData)
				tempData = []
		else:
			if row[3].find('May ' + str(day)) == -1:
				day += 1
				filteredData.append(tempData)
				tempData = []
		#looks for all keywords in the tweet. Adds the tweet if it has done so
		for word in keyWords:
			if row[2].find(word) != -1:
				tempData.append(row)
				break

	return filteredData
	
    
#returns the initial names of the people
def getInitialNames(dataList):
	names = []
	rule = ['vote', 'iboto']
	tempName = ""
	for tweet in dataList:	#iterates through all tweets
		tempName = finderAlgo(rule[0], tweet[2])
		if (tempName != ""):
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
					name += tokenList[mover] 
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
					name = tokenList[mover] + name
					found += 1
			moves -= 1
			mover -= 1
	return name

tweetData = []
tweetData = getDataFromCSV(filename)
#nameList = getInitialNames(tweetData[0])
#print(nameList)

day = 1
for chunk in tweetData:
	print("\n\n----------- May " + str(day) + " ----------\n")
	for row in chunk:
		print(row[2])
	day += 1