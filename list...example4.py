#copying a list
#creating shallow copy using slicing

##a=[1,2,3,4,]
##b=a.copy()
##print("a is",a)
##print("b is",b)
##
##a[0]=100
##print("a is",a)
##print("b is",b)

##

a=[1,2,3,4,]
b=a[ : ]
print("a is",a)
print("b is",b)

a[0]=200
print("a is",a)
print("b is",b)

#clear()=clear a list=empty a list
b.clear()
print("list b is",b)

#creating an empty list
list1=[]
print("empty list1 is",list1)
#or
list2=list()
print("empty list2 is",list2)


#delete a list
del list2

#print(list2)

#create a list
x=[8,9,7,6]
print(x)

y=list((6,3,2,1))
print(y)


####Sorting a list
#sort according to alphebatic order
names=["vickey","anubhav","himanshu","akash","soni","paras","vanshaj"]
names.sort()
print(names)

names.sort(reverse=True)
print(names)

s=[6,4,3,7,5,4]
s.sort()
print(s)


#index function
x=[5,7,9,3,4,7]
print("index of 7 is",x.index(7))














































