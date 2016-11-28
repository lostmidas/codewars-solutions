'''
Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
returns 'Bart'
namelist([])
returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''

def namelist(names):
    if names == []:
        return ""
    if len(names) == 1:
        return names[0]["name"]
    elif len(names) > 1:
        result = []
        for i in names:
            result.append(i["name"])
        return ", ".join(result[:-1]) + " & " + "".join(result[-1])
