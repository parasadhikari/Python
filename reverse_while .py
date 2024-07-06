#wap to reverse a number using while loop
##print("enter a no.")
##num= int(input())
##res=0
##while num>0:
##    last=num%10
##    res= res*10+last
##    num=num//10
##
##print("reverse is",res)


#wap to print sum of digits of a number
##print("enter a no.")
##num= int(input())
##sum=0
##while num>0:
##    last=num%10
##    sum= sum+last
##    num=num//10
##
##print("sum is",sum)



#wap to check weather a number is pallendrome or not
#(having original no and reverse is same)
##print("please enter the random no.")
##num= int(input())
##temp=num
##rev=0
##while num>0:
##    last=num%10
##    rev= rev*10+last
##    num=num//10
##
##print("reverse is",rev)
##
##if temp==rev:
##    print("pallindrome no.")
##
##else:
##    print("not a pallindrome no.")





#wap to check weather a no is armstrong or not
print("enter a no.")
num= int(input())
temp=num
sum=0
while num>0:
    last=num%10
    sum= sum+last**3
    num=num//10

if temp==sum:
    print("number is armstrong")

else:
    print("number is not armstrong")




















