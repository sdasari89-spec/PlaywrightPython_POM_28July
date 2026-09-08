
# its a common method for all the testcases. json handling common for acroos all th epages and all the testcases. 
# if a particulat method is used across all the testcases then add it in util folder


import json

def jsonHandling(filepath):
    with open(filepath)as data: 
         formattedData= json.load(data)
         return formattedData