import numpy as np

def multiples():
    while True:
        try:
            table = int(input('Please enter the number that you would like to multiply \n'))
            startnum = int(input('Please enter the starting number \n'))
            endnum = int(input('Please enter the las number \n'))
            studentName = str(input('Please enter your name \n'))
            
            break
            
        except:
            ("Wrong Value type Try again")
    print(f'Hi {studentName} here are your values...')
    while startnum <= endnum:
        print(f'{table} x {startnum} = {table*startnum}')
        startnum = startnum + 1

def getPWord():
    while True:
        try:
            password = str(input('Please enter a password \n'))
            print(len(password))
            if 8 <= len(password) <= 16:
                while True:
                    try:
                        passwordV = input('Please re-enter the password\n')
                        if passwordV == password:
                            print("Password Authenticated")
                            break
                        else:
                            raise Exception()
                    except:
                        print('Password does not match')
                break
            else:
                raise Exception()
        except:
            print('Invalid Password')

def parkingSpace():
    grid = np.full((20,25), '', dtype=str)
    regNum = input('Please enter your vehicles registration number \n')
    rowPos = int(input('Please enter the row your vehicle is located \n'))
    columnPos = int(input('Please enter the column your vehicle is located\n '))
    if grid[rowPos - 1,columnPos - 1] == '':
        grid = np.append(grid[rowPos - 1,columnPos - 1], regNum)
    print(grid)
        
                        
parkingSpace()                    
                           
        

    
    