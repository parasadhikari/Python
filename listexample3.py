# Adding and removing data from a list

##list1=[10,20,30,40]
##print(list1)

# append function is used to add single element at the end of the list

##list1.append(50)
##print(list1)

# extends  fuction is used to add multiple elements at the end of the list
##list1.extend([60,70,80,90])
##print(list1)

# insert function is used to add an element at the specific position
# First argument is index, second argument is element

list1.insert(1,9)
print(list1)
##
list1.insert(2,90)
print(list1)

# Removing a data

# 1. pop()= Deletes last element of the  list and also returns the deleted value

##print("before pop() ", list1)
##x= list1.pop()
##print("after pop() ", list1)
##print("The deleted element is ",x)
##
##
##x= list1.pop(-3)
##print("after pop() ", list1)
##print("The deleted element is ",x)


# remove()= Remove functions removes the specified element

list1.remove(20)
print("list after remove", list1)


# del keyword= We can delete one or more elements using del
##
del list1[2]
print(list1)
####
####
del list1[ : : 3]
print(list1)


# Difference between pop and del.
# pop returns the deleted element. But we cannot get the deleted element in del


# Copying a list
# Deep copy= Changes made in a list also reflects in another copied list

##list1=[1,2,3,4]
##list2= list1
##print("before changes")
##print(list1)
##print(list2)
##
##list1[0]=100
##print("after changes")
##print(list1)
##print(list2)

# shallow copy= Changes made in a list also reflects in another copied list

##list1=[1,2,3,4]
##list2= list1.copy()
##print("before changes")
##print(list1)
##print(list2)
##
##list1[0]=100
##print("after changes")
##print(list1)
##print(list2)







































