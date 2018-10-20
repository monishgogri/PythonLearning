import sys
print ("Python: "+sys.version)

#a)
for x in range (10,30,3):
    print (x, end=" ")
    x = x + 2
print()
i = 10
while i < 30:
    print (i, end=' ')
    i=i+3

#b)
counter=0
while(counter<10):
    print(counter, end=" ")
    counter +=1
else:
    print("counter=" + str(counter))

for i in range(1, 10):
    if(i%5==0):
        break
    print(i, end=" ")
else:
    print("i=" + str(i))