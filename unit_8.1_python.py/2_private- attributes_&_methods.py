# PRIVATE(LIKE) ATTRIBUTE & METHODS
'''conceptual implementation in python'''
'''Private attributes & methods are meant to be used only eithin the class and are not accessible from outssude the class.'''

class Person:
    __name = "anonymous"
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()

p1 = Person()