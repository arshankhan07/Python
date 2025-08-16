#list methods

#list.append() -> add one elrment at the end of the list.
#list.insert() -> add one element at the perticular index.
#list.remove() -> remove one element from the list.
#list.pop() -> remove one element from the end of the list. or from the perticular index.
#list.clear() -> remove all elements from the list.
#list.sort() -> sort the list in ascending order.
#list.(reverse=True) -> reverse the list.
#list.count() -> count the number of occurences of a element in the list.
#list.index() -> return the index of the first occurence of a element in the list.
#list.copy() -> return a shallow copy of the list.
#list.extend() -> add elements from another list to the end of the list.

list = [1,2,3,4,5]
list.append(6)
print(list)

list = [1,4,5,2,3]
list.append(6)
list.sort()
print(list)