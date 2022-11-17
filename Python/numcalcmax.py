

def initialise():
    print('This calculator finds the highest numbers of 3 sets of digits and returns the average')
    
def promptfornum():
    #simple loop to acquire three inputs
    for i in range(3):
        prompt = int(input("Please enter a number "))
        nums[n].append(prompt)
        print(nums[n])   

def findmax():
    #sorts list in numerical order from largest to smallest, then deletes the smaller elements
    nums[n].sort(reverse=True)
    del nums[n][1]
    del nums[n][1]


def processData():
    #Sets a loop to repeat processes 3 times to find the max and also maintaining that n is a global variable
    global n
    for i in range(3):
        promptfornum()
        findmax()
        n = n + 1
        print(nums)

def calcAverage():
    #adds all the highest numbers together then divides, had problems with containing it all in one assignment so it was split
    total = nums[0][0] + nums[1][0] + nums[2][0]
    total = total / 3
    print(f"Your average is {total}\n")

#nums is our 2 dimensional array with a space for each list, n is our global counter for the loop
nums = [[],[],[],]
n = 0

initialise()
processData()
calcAverage()
