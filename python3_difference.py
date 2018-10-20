'''
Sources for differences:
https://docs.python.org/3/whatsnew/3.0.html
https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
'''

import sys
print ("Python version: ", sys.version)

#Print:
print ("Hello world")
print ("Line separator", end=" ")
print ("example", end="\n\n")

#Integer Division:
print ("3/2=",3/2)
print ("3//2=",3//2)
print ("3/2.0=",3/2.0)
print ("3//2.0=",3//2.0,'\n')

#Handling Exceptions:
try:
    cause_a_name_error
except NameError as err:
    print(err, "...Our Error message")

#Input:
myInput=input("Please enter a number:")
print(type(myInput))

#Unorderable Objects:
'''print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)'''