# WITH SYNTAX

# with open("my.txt", "a") as f:
# data = f.read()

with open("my.txt", "r") as f:
    data = f.read()
    print(data)

with open("my.txt", "w") as f:
    f.write("new data")