import csv
import json
import pytest

from utils.jsonhandling import jsonHandling

@pytest.mark.dh
def test_jsonHandling():
    with open('testData\\creds.json')as data: #open and read and retrun the data and stor int he variable in data
         #convert json string file data into dictionary format
         formattedData= json.load(data)
        #  print(formattedData["email"])
        #  print(formattedData["password"])
         print(formattedData["positiveCreds"]["password"])
         print(formattedData["positiveCreds"]["email"])

@pytest.mark.dh   
def test_jsonHandling2():
    data= jsonHandling('testData\\creds.json')
    print(data)

@pytest.mark.dh 
def test_csvHandling(): 
    with open('testData\\credentials.csv')as data:
        csvData= csv.DictReader(data)
        #print(csvData) # its showing object dont print values so covert into list
        values=[]
        for i in csvData:
            values.append(i) #conert the data into list to gather the data
            print(values) #If you want to see the list growing: use print inside loop
        print(values[1]["username"]) #If you want to print the complete list only once: use print outside loop

#note: csv starts with very first row in excel we can start from headers
