"""
Write a Python function that generates a random password. The password should have a random length of between 7 and 10 characters.
Each character should be randomly selected from positions 33 to 126 in the ASCII table. Your function will not take any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main program should only run when your solution has not been imported into another file.
"""

import random

def GenerateRandomPassword():
    CHARS = [chr(i) for i in range(33,127)]
    LB, UB = (7,10)
    
    iLen = random.randint(LB, UB)
    sPassword = ""
    for ch in range(iLen+1):
        sPassword += random.choice(CHARS)
    return sPassword


"""
In this Puzzle you will write a Python function that determines whether or not a password is good.
We will define a good password to be a one that is:
- at least 8 characters long
- contains at least one uppercase letter
- at least one lowercase letter
- at least one number.
Your function should return true if the password passed to it as its only parameter is good.
Otherwise it should return false. Include a main program that reads a password from the user and reports whether or not it is good.
Ensure that your main program only runs when your solution has not been imported into another file.
"""
def IsSafe(sPassword):
    iFlags = 0 #How many criterias are met and which ones
    dBITS = { 'LEN' : 0,  'UCASE' : 1,  'LCASE' : 2, 'NUM' : 3 } #criterias for evaluating the strength of the password
    ALL =  0xFFFFFFFF & (2**len(dBITS.keys())-1) #Works for a maximum of 32 criterias

    if isinstance(sPassword, str):
        if len(sPassword) >= 8:
            iFlags |= (1 << dBITS['LEN'])
        for ch in sPassword:
            if (ord(ch) >= 65) and (ord(ch) <= 90) :
                iFlags |= (1 << dBITS['UCASE'])
            if (ord(ch) >= 97) and (ord(ch) <= 122) :
                iFlags |= (1 << dBITS['LCASE'])
            if (ord(ch) >= 48) and (ord(ch) <= 57) :
                iFlags |= (1 << dBITS['NUM'])
        return iFlags == ALL
    else:
        raise TypeError
        return False

"""
Using your solutions to Puzzle 7 & 8, write a program that generates a random good password and displays it.
Count and display the number of attempts that were needed before a good password was generated.
Structure your solution so that it imports the functions you wrote previously and then calls them from a function named main in the file that you create for this exercise.
"""
def main():
    bSafe = False
    iAttempts = 0
    sPassword = ''
    while not bSafe:
        iAttempts += 1
        sPassword = GenerateRandomPassword()
        print(sPassword, iAttempts)
        bSafe = IsSafe(sPassword)

        
        
main()                

