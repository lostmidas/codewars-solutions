'''
Create a function that returns the average of an array of numbers ("scores"),
rounded to the nearest whole number.
You are not allowed to use any loops (including for, for/in, while, and do/while loops).
'''

def average(array):
      total = sum(array) / len(array)
      return int(round(total))
