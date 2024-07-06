#1. Write a program that prints numbers from 1 to 10 using a for loop.
##for i in range(1,11):
##    print(i)


#2. Write a program that asks the user to enter a number and prints its multiplication table using a for loop.
##print("enter a number to know it's multiplication")
##a= int(input())
##multiply=a
##for i in range(1,11):
##    multiply=a*i
##    print(multiply)
    
    
#3. Write a program that prints the sum of all even numbers between 1 and 100 using a for loop.
##print("the sum of all even no. upto 100 is:")
##sum=0
##for i in range(1,101):
##    if(i%2==0):
##        sum=sum+i
##print(sum)


#4. Write a program that prints the factorial of a given number using a for loop.
##print("enter the no. of whose you want factorial")
##n=int(input())
##temp=n
##fact=1
##for i in range(1,n+1):
##    fact=fact*i
##print("the factorial of ",temp," is:",fact)


#5. Write a program that prints the Fibonacci sequence up to a given number using a for loop.
##def fib(n):
##print("enter the no.")
##n=int(input())
##a = 0
##b = 1
##if n==1:
##    print(a)
##else:
##    print(a)
##    print(b)
##    for i in range(2,n):
##        c = a + b
##        a = b
##        b = c
##        print(c)

###6. Write a program that calculates the average of a list of numbers using a for loop.
##print("enter the no.")
##num=int(input())
##
##
##
##



#7.Write a program that prints the reverse of a given string using a for loop.
##print("enter the random number")
##num=input()
##rev=0
##for i in range(len(num),-1,-1):
##    rev=rev*10+i
##    num=num//10
##    print(rev,end="")



#8.Write a program that finds the largest number in a list using a for loop.
##
##
##
##
##
##



#9.Write a program that checks if a given number is prime using a for loop.
##print("enter the number to check whether it's prime no. or not")
##num=int(input())
##prime=True
##for i in range(2,num):
##    if num%i==0:
##        prime=False
##        break
##if prime==False:
##    print("its not a prime no.")
   
##else:
##    print("its prime no.")

     #OR

##print("enter the number")
##num=int(input())
##prime=True
##for i in range(2,(num//2)+1):
##    if num%i==0:
##        prime=False
##        break
##
##if prime==False:
##    print("not a prime number")
##
##else:
##    print("it's a prime number")
    

  #OR
##import math
##print("enter the number")
##num=int(input())
##prime=True
##x=int(math.sqrt(num))
##for i in range(2,x+1):
##    if num%i==0:
##        prime=False
##        break
##
##if prime==False:
##    print("not a prime number")
##
##else:
##    print("it's a prime number")




# 10. Write a program that calculates the sum of all numbers divisible by 3 or 5 between 1 and 100 using a for loop.
##print("sum of all 3 and 5 divisible no. between 1 and 100 is:")
##sum=0
##for i in range(1,101):
##    if (i%3 or i%5)==0:
##        sum=sum+i
##print(sum)



#12.Write a program that counts the number of vowels in a given string using a for loop.
##print("enter the any random alpahabet")
##word=input()
##count=0
##for i in range(0,len(word)):
##    if(word[i]!=' '):
##        if(word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u" or
##           word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U"):
##            count=count+1
##print("total vovels is:",count)




#13.Write a program that checks if a given string is a palindrome using a for loop.    
print("enter the random number")
num=input()
temp=num
rev=0
for i in range(len(num),-1,-1):
    last=num%10
    rev=(rev*10)+last
    if(temp==rev):
        print("its a pallindrome no.")
else:
    print("its not a pallindrome no.")






















