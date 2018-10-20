import math
import sys
print("Python: ", sys.version)

#Functions:
#a):
def f1(n1,n2):
    return [n1+n2,n1*n2]

print(f1(10,11),"  ",type(f1(10,11)))

#b):
def f2(n1=5,n2=6):
    return n1+n2,n1*n2

print(f2(10,11),"  ",type(f2(10,11)))
print(f2())
print(f2(n2=11))
print()

#Lists:
#a):
myList = ["cheese", "milk", "water"]
print(myList)
myList.append("apple")
print(myList)
del myList[1]
print(myList)
myList.append("swiss cheese")
print(myList)
for eachValue in myList:
    print(eachValue)
print()

#b):
x = math.pi
print (((x*1000) // 10) /100)
print(x)
piList = [ (x*(10**(i+1)))//10/(10**(i)) for i in range(1,6)]
print (piList)
piList2 = [ round(x,i) for i in range(1,6)]
print (piList2)