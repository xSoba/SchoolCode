queue = []
queueMaxSize = 10
def isEmpty():
    if len(queue) == 0:
        print('The queue is empty')
    else:
        print('The queue is not empty')

def isFull():
    if len(queue) == queueMaxSize:
        print('The queue is full')
    else:
        print('The queue is not full')

def addElement():
    loop = int(input('How many elements do you want to add to the queue?: \n '))
    for i in range(loop):
        tempItem = input('Please enter what you would like to add to the queue: \n ')
        queue.append(tempItem)
        print(queue)

def removeElement():
    loop = int(input('How many elements would you like to remove from the queue: \n '))
    for i in range(loop):
        queue.pop()

print('Welcome to the queue manipulator 5000')
choice = int(input('What would you like to do today? \n 1.Add an Element to the queue \n 2. Remove elements from the queue \n 3. Check if the queue is full \n 4. Check if the queue is empty \n'))
if choice == 1:
    addElement()
    

elif choice == 2:
    removeElement()
    
    
   
        