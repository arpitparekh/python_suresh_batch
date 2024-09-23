list = [12,35,6,54,45,"Hello",2.34,True]

# dictionary store data in key value pairs

person = {
    "name" : "Bascom",
    "age" : 23,
    45 : "Hello",
    True:[1,2,3,54]
}

print(person)

data = {}              # empty disctionary
data[12] = "Hello"
data["hi"] = 23

print(data)

print(person[True])

print(person.get(True)[2])

# dict inside dict

mydata = {
    "data1" : {"subdata1":12},
    "data2" : {"subdata2":14}
}

print(mydata)

print(mydata["data2"]["subdata2"])

print(mydata.values())

mydata.popitem()
print(mydata)

mydata.pop("data1")
print(mydata)