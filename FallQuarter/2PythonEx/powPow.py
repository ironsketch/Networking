'''
    This program calculates 2^2^(user inputed data)

    I don't know if this is what you were asking for... I can change it to return an int instead? But also any power above 1048576 is too slow for my taste so I limited the user 0 - 20. 
'''
y = 2000000
MAX = 1048576

def userInput():
    x = int(input("Enter a number (0 - 20) for a good time... "))
    return x

while y > MAX:
    num = userInput()
    y = pow(2, num)

print pow(2, y)
