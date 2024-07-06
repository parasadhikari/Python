#LIST COMPHERINSION
#create a list of number between 1 to 10
listnum=[]
for i in range(1,11) :
    listnum.append(i)
print(listnum)

#With comprehension
newlist=[i for i in range (1,11)]
print(newlist)

#create a list of even number from 1 to 20
even=[i for i in range (1,21) if i%2==0]
print (even)

#create a list of number that are divisible by both 2 and 10
divisible=[i for i in range (1,51) if i%2==0   if i%10==0]
print(divisible)

#create a list of number that are divisible by both 2 and 10
divisible=[i for i in range (1,51) if i%2==0 and i%10==0]
print(divisible)

#create a list of number that are divisible by both 2 and 10
divisible=[i for i in range (1,51) if i%2==0 or i%10==0]
print(divisible)

#create a list of number that are not  divisible by 5
divisible=[i for i in range (1,21) if i%5!=0 ]
print(divisible)
                #or
#create a list of number that are not  divisible by 5
divisible=[i for i in range (1,21) if not i%5==0 ]
print(divisible)

#Given a list of a number print square of a no. if no. is even else print cube of a number
num=[1,2,3,4]
res=[i**2 if i%2==0 else i**3 for i in num]
print(res)

#change list in uppercase
names=["nitin","himanshu","paras"]
uppercase=[ i.upper() for i in names]
print(uppercase)

#Reverse the names using list comprehension
names=["nitin","himanshu","paras"]
reverse =[i [ : : -1] for i in names]
print(reverse)

#Reverse the names using list comprehension
#only indexing reverse 
names.reverse()
print(names)















