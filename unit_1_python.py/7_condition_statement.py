#traffic light
light = input("light color : ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("ready")
elif(light == "green"):
    print("go")
else:
    print("light is broken")


#student grade
marks = int(input("enter the marks :"))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")


#single line if statement
#<variable> = <value1> if <condition> else <value2>
food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)


#<string1>if<condition>else<string2>
food = input("food :")
print("sweet") if food == "cake" or food == "ice cream" else print("salty")


#clever if statement
#<variable> = (false_value,true_value)[<condition>]
age = int(input("age :"))
vote = ("can't vote", "can vote")[age >= 18]
print(vote)


#example
sal = float(input("salary :"))
tax = sal*(0.1, 0.2)[sal << 50000]
print(tax)