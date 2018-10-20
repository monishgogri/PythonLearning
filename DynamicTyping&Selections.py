import sys
print("Python: ",sys.version)

#Dynamic Typing
#a):
a = 2
b = 3.1
c = 'd'
d = "a string"
e = [1,22,333]
f = (4,55,666)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f),end='\n\n')

#b):
b = 21
b = b+b
print(b) #42
b = "3"
b = b+b
print(b) #33
print(type(int(b))) #int
print(type(str(type(int(b)))),end='\n') #str
print(str(type(str(type(int(b)))))[3], "\n") #str(str)

#Selections:
myInput = 0
while True:
        myInput = input("Please Enter: ")
        if myInput == 'exit':
            break
        try:
            i = float(myInput)
        except ValueError:
            try:
                i = int(myInput)
            except ValueError:
                continue
        if i < 0 or i > 9:
            print("Invalid Number!")
        elif i >= 1 and i <= 3:
            print("A")
        elif i >= 4 and i <= 6:
            print("B")
        elif i >= 7 and i <= 9:
            print("C")