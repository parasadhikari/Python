# Python Supports two types of loop
##1. for loop
##2. while loop
'''Why loop?
Loop is used to perform a task repeatedly
Example
1. Take input of 50 students name
2. Sum of a given series of a number
7,9,4,6,8
'''
# Difference between for and while loop
# for loop is used when number of iterations are known
# while loop is used when number of iterations
# are unknown


# Print Vicky 10 times using while loop
##
##i=1
##while i<=10:
##    print("Vicky")
##    i=i+1

# Print table of any number while loop
##
##print("Enter a number")
##n=int(input())
##i=1
##while i<=10:
##    print(n*i)
##    i=i+1

# Infinite Loop
##
##while True:
##    print("Enter a number")
##    a=int(input())
##    print("Enter second number")
##    b=int(input())
##    c=a+b
##    print("Sum is ",c)
##    print("Do you want to add more Press n to stop")
##    choice=input()
##    if choice=="N" or choice=="n":
##        break

# break keyword is used to terminate the loop

# Use of break in for loop

for i in range(1,10):
    if i==6:
        break
    else:
        print(i)



# Use of break in while loop

i=51
while i<=100:
    if i%2==0 and i%10==0:
        break
    else:
        print(i)
    i=i+1
    



        
    












    

    


















