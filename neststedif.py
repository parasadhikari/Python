#nested if
#write a program to find greatest among numbers
##print("enter first number")
##a=int(input())
##print("enter second number")
##b=int(input())
##print("enter third number")
##c=int(input())
##if a>b:
##    if a>c:
##        print(a,"is greatest")
##
##if b>a:
##    if b>c:
##        print(b,"is greatest")
##
##if c>b:
##    if c>a:
##        print(c,"is greatest")
##
##if a==b:
##    if b==c:
##        print("all are equal")




##a=9
##b=5
##c=6
##
##if a<b and a<c:
##    if b<c:
##        print(a,b,c)
##    else:
##        print(a,c,b)
##
##
##if b<a and b<c:
##    if a<c:
##        print(b,a,c)
##    else:
##        print(b,c,a)
##
##if c<a and c<b:
##    if b<a:
##        print(c,b,a)
##    else:
##        print(c,a,b)


#array to ascending order
##li=[78,90,2,6,7,34,65,11,5,45]
##li.sort()
##print(li)

#array to descending order
##li=[78,90,2,6,7,34,65,11,5,45]
##li.sort(reverse=True)
##print(li)


#Employee data=id,name,salary,experience
##exp=5yrs above=salary=10000 increment
##exp=3-5yrs above=salary=6000 increment
##exp=2-3yrs above=salary=3000 increment
##less than 2yrs = no increment


print("enter your id")
a=int(input())
print("enter your name")
name=input()
print("enter your experience")
exp=int(input())
print("enter your salary")
salary=float(input())
if exp>=5:
    print("old salary",salary)
    salary=salary+10000
    print("new salary is",salary)
if exp>=3 and exp<5:
    print("old salary",salary)
    salary=salary+6000
    print("new salary is",salary)
if exp>=2 and exp<3:
    print("old salary",salary)
    salary=salary+0
    print("new salary is",salary)



































