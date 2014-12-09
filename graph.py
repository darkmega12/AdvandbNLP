import matplotlib.pyplot as plt
import numpy as np


def getGraph(data):
#this will add all elements and put in y
    x = [["kim",10,"dec 5"],["kiel",5,"jan 1"],["kiel",3,"feb 2"],["kas",4,"dec 1"],["ham",100,"jan 1"],["kim",15,"jan 5"],["kas",11,"may 5"]]
    y = [["kim",0]]
    z = 0
    check = False
    value = []
    name = []
    for i in range(len(x)):
        for j in range(len(y)):
            if (x[i][0] == y[j][0]):
                y[j][1] += x[i][1]
                check = True
        if (check == False):
            y.append([])
            y[-1].append(x[i][0])
            y[-1].append(x[i][1])
        else:
            check = False

#for printing values
    for i in range(len(y)):
        value.append(y[i][1])
        name.append(y[i][0])

    xlength = np.arange(len(y))
    width = 0.35

#This is for bar graph
    plt.figure(0)
    for i in range(len(y)):
        plt.barh(xlength, value, align = 'center', color = 'b')
    plt.yticks(xlength, name)
    plt.title('Popularity of senator')
    plt.xlabel('Value')
    plt.ylabel('Candidates')

#This is for line graph
#for i in range(len(y)):
#    tempValue = []
#    tempDate = []
#    plt.figure(i+1)
#    for j in range(len(x)):
#        if (y[i][0] == x[j][0]):
#            tempValue.append(x[j][1])
#            tempDate.append(x[j][2])
#    xlength = np.arange(len(tempValue))
#    plt.plot(xlength,tempValue)
#    plt.xticks(xlength, tempDate)
#    plt.xlabel('Date')
#    plt.ylabel('Value')

    plt.show()
