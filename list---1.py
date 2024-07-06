#if we required to print 100 sudent name so we use list
names=["raj","paras","aakash","himanshu","vickey","rahul","soni"]
##print(names)
##for i in names:
##    print(i)

#python support two types of indexing
#positive indexing=start  from 0
 #negative indexing=start from-1

##print(names[0])#raj
##print(names[-1])#Himanshu



##########Positive SLICING IN LIST###############
##print(names[1:4])#paras,aakash,himanshu,vickey.....i.1-3
##print(names[1:6:2])#paras,,himanshu,rahul.....i.1--->6--leaving 1 space
##print(names[ :6])#i.e strt from 0---->as beginning is not defined default value is 0
##print(names[2:])#i.e strt from 2& end with last element as ending is not defined therefore it will run till last
##print(names[ : ])#i.e it start from 0 index and end with last index automatically




##########Negative SLICING IN LIST###############
##print(names[-7:-1])#-1 give 2nd last element 
##print(names[-7: ])# to include last element just left the space
##print(names[ : :-1])# to reverse the list


###########REVRSE THE Number/Name###########
##num='123456'
##print(num[ : :-1])


##name="vickey"
##print(name[ : :-1])


##list1=[8,7,9,1,2,4,5,6]
##print(list1[2:])
##print(list1[:5])
##print(list1[ : :2])
##print(list1[0:6:3])
##print(list1[4:0:-1])




##########ADDING and REMOVING data from a list*************************8
list1=[10,20,30,40,50]
print(list1)

###########Appended function is used to add element at the end of the list
list1.append(60)
print(list1)
##########append can add only one at atime.........therefore we use EXTENEND
list1.extend([70,77,80,90,95])
print(list1)

############insert function is used to add the element at the specific position
###1st argument is "index" 2nd is "element"
list1.insert(0,9)
print(list1)


list1.insert(4,39)
print(list1)


####removing a data
#1.pop------>>>remove last elements of list and also return deleted value
###to remove any index element we can use indexing to pop
print("before pop()",list1)
x=list1.pop()
print("after pop()",list1)
print("the deleted element is",x)



print("before pop()",list1)
x=list1.pop(5)
print("after pop()",list1)
print("the deleted element is",x)




print("before pop()",list1)
x=list1.pop(-3)
print("after pop()",list1)
print("the deleted element is",x)


####remove()=remove function removes the specified function
print("before pop()",list1)
x=list1.remove(20)
print("after remove()",list1)


#####del keyword= we can delete one or more elements using del
del list1[0]
print(list1)


del list1[2::4]
print(list1)


####DIFFERENCE between pop and del function is that we can
####see deleted value in pop but in del we cant see the deleted value



####Copyin a list
##Deep copy=changes made in a list also reflect in another copied list
list1=[1,2,3,4]
list2=list1
print("before change")
print(list1)
print(list2)

list1[0]=100
print("after changes")
print(list1)
print(list2)


###Shallow copy=changes made in a list don't reflect in another copied list
list1=[1,2,3,4]
list2=list1.copy()
print("before change")
print(list1)
print(list2)

list1[0]=100
print("after changes")
print(list1)
print(list2)


















