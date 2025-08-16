#Dictionary in python 
#dictionarys are used to store data values in "key:values" pair.
#they are unordered, mutable(changeable) &don't allow duplicate keys.
#syntax EG:
dict = {
    "name" : "Arshan",  # "key" : "value"
    "age" : 19,
    "height" : 5.10
}

info = {
    "key" : "value",
    "name" : "arshan",
    "age" : 19,
    "subject" : ["python", "c++"], #list
    "topics" : ("dictionary", "sets"),#tuple
}
print(info)
print(type(info))
print(info["name"])
print(info["age"])
print(info["subject"])
print(info["topics"])

#to assign new value 
info["name"] = "ARSHAN"
print(info)

#NESTED DICTIONARY
student = {
    "name" : "arshan",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95,
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])

#METHODS IN DICTIONARY
# myDict.key() -> return all keys
# myDict.values() -> return all values
# myDict.item() -> return all (key, val) pairs as tuples
# myDict.get("key") -> return the key according to value 
# myDict.update -> inserts the spreific item to the dictionary