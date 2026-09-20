import csv
import json
import os
from dotenv import load_dotenv
from openpyxl import load_workbook
import pytest

from utils.jsonhandling import jsonHandling

#@pytest.mark.dh
def test_jsonHandling():
    with open('testData\\creds.json')as data: #open and read and retrun the data and stor int he variable in data
         #convert json string file data into dictionary format
         formattedData= json.load(data)
        #  print(formattedData["email"])
        #  print(formattedData["password"])
         print(formattedData["positiveCreds"]["password"])
         print(formattedData["positiveCreds"]["email"])

#@pytest.mark.dh   
def test_jsonHandling2():
    data= jsonHandling('testData\\creds.json')
    print(data)

#@pytest.mark.dh 
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


#@pytest.mark.dh 
def test_excelhandling():
    workbook = load_workbook("testData//sampleCredentials.xlsx")
    sheet = workbook["Sheet2"]
    values=[]
    # for i in sheet[5]:
    #     print(i.values)
    #     print(i.value) #print each cell value one by one

    for i in sheet.iter_rows(min_row=2,values_only=True):
        values.append(i)
    # for i in sheet.iter_cols(min_col=1,values_only=True):
    #     values.append()
    print(sheet["A4"].value)
    print(values)


#@pytest.mark.dh 
def test_excelhandling():
    workbook = load_workbook("testData//sampleCredentials.xlsx")
    sheet = workbook["Sheet2"]
    #replace cell value to tripura
    sheet["A4"]='Tripura'
    #save the entire work book this is important and excel file should close while writing
    workbook.save("testData\\sampleCredentials.xlsx")
    # #add entire new row not replacing
    # sheet.append("new","new1")
    # workbook.save("testData\\sampleCredentials.xlsx")
    # #Delete the data
    # sheet.delete_rows(4,1)
    #  #from 4th row remove only th esingle row (4,2) meand from th e4th remove 2 rows means 4 and 5 will remove
    # workbook.save("testData\\sampleCredentials.xlsx")


@pytest.mark.dh
# execute via command line
#set usname=sushma&&set pwvalue=admin&&pytest -m dh -s
def test_cli():
    userName = os.getenv("usname")
    pwdValue = os.getenv("pwvalue")
    print(userName)
    print(pwdValue)

@pytest.mark.dh
#pip install python-dotenv
def test_cli_env():
    # now we have .env files so no need to pass from command line so w ewill read data from env and grab the data
    #load_dotenv(".env.test")
    load_dotenv(os.getenv("ENV_FILE"))
    print("ENV_FILE =", os.getenv("ENV_FILE"))
    print("Current folder =", os.getcwd())
    userName = os.getenv("usname1") #these are called keys usname and pwvalue
    pwdValue = os.getenv("pwvalue1")
    url=os.getenv("url1")
    print(userName)
    print(pwdValue)
    print(url)

    #Your test_cli() can be run while you are inside the tests folder because it doesn't depend on an .env.test file.
    #so come out tests folder and run in command line

