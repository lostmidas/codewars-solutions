'''
Write a function that returns both the minimum and maximum number of the given list/array.

Examples:
min_max([1,2,3,4,5])   == [1,5]
min_max([2334454,5])   == [5, 2334454]
min_max([1])           == [1, 1]
'''

def min_max(lst):
    return [min(lst), max(lst)]
