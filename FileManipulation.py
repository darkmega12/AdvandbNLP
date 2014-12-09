import csv

keyWords = ["Vote", "VOTE", "vote", "boto", "iboto", "bumoto", 
			"Halalan", "halalan", "senator", "Senator", "elect", 
			"Mayor", "mayor", "Eleksyon", "eleksyon"]

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

#nameList = getInitialNames(tweetData[0])
#print(nameList)