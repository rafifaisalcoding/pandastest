import pandas as pd
testdataset = {
    'column1': [1,2,3],
    "column2": [456,678,890],
    "column3": ["test","test2",3]
}
var = pd.DataFrame(testdataset)
print(var)
print(var.loc[0])
print(var.loc[[0,1]])
print("--------------------------------------------------------------------------------")
testseries = [69,3,53, "i love pandas"]
testseries_var = pd.Series(testseries)
print(testseries_var)
print(testseries[1]) # yes im aware the index starts at 0 in python programming
indexlabel = pd.Series(testseries, index = ["a","b","c","d"])
print(indexlabel)
print(indexlabel.loc["a"])
print("--------------------------------------------------------------------------------")

daytracker = {
    "day1": 1,
    "day2": 4,
    "day3": 5
}
daytrackernew = pd.Series(daytracker, index = ["day1","day2"])
print(daytrackernew)
print("--------------------------------------------------------------------------------")

testcsv = pd.read_csv('testdata.csv')
print(testcsv)
print(testcsv.to_string())
print(pd.options.display.max_rows)
pd.options.display.max_rows = 100
print("--------------------------------------------------------------------------------")

testjson = pd.read_json('testjson.json')
print(testjson)
print(testjson.to_string())

jsondata = {
    "id":{
        "entry1": 10,
        "entry2": 20,
        "entry3": 30
    },
    "identry2":{
        "entry1": 40,
        "entry2": 50,
        "entry3": 60
    }
}
jsondata_var = pd.DataFrame(jsondata)
print(jsondata_var.to_string())
print("--------------------------------------------------------------------------------")

