#Set is a collection of the unorderedd item.
#Each element in the set must be unique & immutable.
#Duplicate values are not allowed in set.

collection = {1, 2, 2, 3, 4}
print(collection)
print(type(collection))
print(len(collection))

# for empty set : 
collection = set()

# SET'S METHOD :
""" set.add() -> addscan element
set.remove() -> removes the element
set.clear() -> empties the set
set.pop() -> removes a random value
set.union() -> combines both set values and return a new set
set.intersection() -> combines common values and return a new set"""

#ADD
collection = set()
collection.add(1)
collection.add(2)

print(collection)

#REMOVE
collection = set()
collection.add(1)
collection.add(2)
collection.remove(1)
print(collection)

#CLEAR
collection = set()
collection.add(1)
collection.add(2)
collection.clear()
print(collection)

#POP
collection = set()
collection.add(1)
collection.add(2)

print(collection.pop())

#UNION
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))

#INTERSECTION
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))