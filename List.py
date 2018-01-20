#@Author Prathamesh More

#Python Lists
#Lists are the most versatile of Python's compound data types. A list contains items
#separated by commas and enclosed within square brackets ([]). To some extent, lists are
#similar to arrays in C. One of the differences between them is that all the items belonging
#to a list can be of different data type.

#Simple List
list = ['Prathamesh','nawaz','Santosh','Minal','Aishwarya','Shubham']

tinyList = ['Sahil']

#Print list
print(list)

#Print first element of list
print(list[0])

#Print elements from first element to third elemetn
print(list[0:3])

#Print elements from second element
print(list[2:])

#Print list two time
print(list * 2)

#Add concate two lists
print(list + tinyList)

#Reverse list
list.reverse()
print(list)

#Append new element in list
list.append("Nitin")
print(list)


#Count element from list
list.count(2)
print(list)

#Sort list
#Create new list
numbers = [9,8,7,6,5,4,3,2,1,0]
print(numbers)

#Sort List
numbers.sort()
print(numbers)

#Clear both Lists
list.clear()
numbers.clear()

print(list)
print(numbers)