#Tuples
#tuples are collection of heterogeneous data
#(data of different types i.e int ,string, float)
#tuples are indexed
#tuples are ordered
#tuples are immutable, cant be modified
#tuples are represented in ()
#tuples can contain duplicate values .
#tuples cant be change but list can be changed

t1=[1,3,4,5,5,4,3,2,8,9]
print(t1)
t1[0]=100
print(t1)


##t1=(1,3,4,5,5,4,3,2,8,9)
##print(t1)
##t1[0]=100
##print(t1)# 'tuple' object does not support item change neither add nor remove


#touple is used to store those data which cnt be changed like admission number,aadhar id 
t=(1,True,89.7,"abc")
print(t)
print(type(t))

### how to find datatypes of each value in Tuple
##
##t=(1,True,89.7,"abc")
##for i in t:
##    print(i,"and type is ",type(i))
##
##print("first element is ",t[0])
##
##print("last element is ",t[-1])
##
##t1=(10,3,7,12,9,5,3,7,8,2)
##x=sorted(t1)
##print(x)



##WAP to remove duplicats from tuple
t1=(1,3,4,5,5,4,3,2,8,9)
res=[]
for i in t1:
    if i not in res:
        res.append(i)

print(res)

          #OR
##WAP to remove duplicats from tuple
t1=(1,3,4,5,5,4,3,2,8,9)
print(set(t1))
#when set included repetation automatically remove



##WAP to count number of element occured in a tuple
t1=(1,1,1,2,2,3,4,4,5,4,5,6,8,7,8)
result=[(i,t1.count(i)) for i in set(t1)]
print(result)

for i in result:
    a,b=i
    print(a, "appears",b, "times")

#unpacking of touple
t=(3,4)
a,b=t
print("a is ",a)
print("b is ",b)
#paranthesis is not essential in tuple
















