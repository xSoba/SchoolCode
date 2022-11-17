#Unit 2 Problem Solving Lesson 4 Worksheet question 1
#program temperature stats.py

maxTemp = int(input ("Please enter max temp, 999 to finish "))

maxArray = []
minArray = []
totalMaxTemp = 0
numDays = 0
daysAboveAverage = 0
daysNegative = 0
while maxTemp != 999:
    minTemp = int(input ("Please enter min temp "))  
    maxArray.append(maxTemp)
    minArray.append(minTemp)
    numDays = numDays + 1
    totalMaxTemp = totalMaxTemp + maxTemp
    if minTemp < 0:
        daysNegative = daysNegative + 1
    #endif
    maxTemp = int(input ("Please enter max temp, 999 to finish "))
     
#endwhile

averageMaxTemp = totalMaxTemp / numDays		

daysAboveAverage = 0
for n in range(0,numDays):
    if maxArray[n] > averageMaxTemp:
        daysAboveAverage = daysAboveAverage + 1
    #ENDIF
#ENDFOR
	
print ("Days max temp above average ",daysAboveAverage)
print ("Days min temperature below zero ", daysNegative)
