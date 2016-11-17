'''
Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out.
Note: The function accepts an integer and returns an integer.
'''

def square_digits(num):
    num = [int(i) for i in str(num)]
    numSquare = [i ** 2 for i in num]
    numSquare = ''.join(map(str, numSquare))
    return int(numSquare)
