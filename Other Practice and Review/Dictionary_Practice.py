dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1k = list(dict1.keys())
dict1v = list(dict1.values())
dict2k = list(dict2.keys())
dict2v = list(dict1.values())

for i in range(len(dict2v)):
    if dict2k[i] not in dict1:
        dict1[dict2k[i]] = dict2v[i]

print (dict1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res= {}
for i in range (len(keys)):
    res[keys[i]] = values[i]
    
print (res)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print (sampleDict["class"]["student"]["marks"]["history"])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = {}

for i in range(len(employees)):
    res[employees[i]] = defaults
    
print (res)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = {}

k = list(sample_dict.keys())
v = list(sample_dict.values())

for i in range(len(k)):
    if k[i] == keys[0] or  k[i] == keys[1]:
        new_dict[k[i]] = v[i]

print(new_dict)