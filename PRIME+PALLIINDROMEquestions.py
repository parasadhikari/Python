# Write a program to check whether a number is prime or not

print("Enter a number")
n=int(input())
prime= True

for i in range(2,n):
    if n%i==0:
        prime= False
        break

if prime==False:
    print("Number is not prime")
else:
    print("Number is prime")


#  Write a program to print prime numbers between 100 to 200

for i in range(100,201):
    prime= True

    for j in range(2,i):
        if i%j==0:
            prime= False
            break

    if prime==True:
        print(i)


# while loop  print even numbers from 1 to 20

print("Even numbers")
i=1
while i<=20:
    if i%2==0:
        print(i)
    i=i+1


# Write a program to check whether a text a palindrome or not
# nitin

print("Enter a text")
s=input()
if s==s[: :-1]:
    print("Text is palindrome")
else:
    print("Text is not palindrome")























        




















    



