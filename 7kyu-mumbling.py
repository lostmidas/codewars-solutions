'''
Write a function "accum(s)" that returns the following:
accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
'''

def accum(s):
    return "-".join([str(s[i] * (i + 1)).capitalize() for i in range(len(s))])
