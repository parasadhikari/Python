# Multiple if-else (if-else ladder)

# Write a code to check a valid age. If age is valid,
# then display the age group

##print("Enter your age")
##age=int(input())
##if age<=0 or age>100:
##    print("Age is Invalid")
##elif age>=0 and age<=12:
##    print("You are a child")
##elif age>=13 and age<=19:
##    print("You are a teenager")
##elif age>=20:
##    print("You are an adult")



# Create a grading System.
#if marks less than 0 and marks >100 then invalid print
#marks greater than equal to 90= grade =A+
#marks between 75 to 90= grade =A
#marks between 60 to 75= grade =B
#marks between 40 to 60= grade =C
# marks below 40= grade= Fail

##print("Enter your marks")
##marks=int(input())
##if marks<0 or marks>100:
##    print("Invalid marks")
##elif marks>=90:
##    print("Your grade is A+")
##elif marks>=75 and marks<90:
##    print("Your grade is A")
##elif marks>=60 and marks<75:
##    print("Your grade is B")
##elif marks>=40 and marks<60:
##    print("Your grade is C")
##elif marks<40:
##    print("You are fail")

##
##print("Enter your marks")
##marks=int(input())
##if marks<0 or marks>100:
##    grade="NA"
##elif marks>=90:
##    grade="A+"
##elif marks>=75 and marks<90:
##    grade="A"
##elif marks>=60 and marks<75:
##    grade="B"
##elif marks>=40 and marks<60:
##    grade="C"
##elif marks<40:
##    grade="Fail"
##
##print("Your grade is ", grade)


# Shopping discount application
# Total shopping above 10000, 10% discount
# Total shopping above 7k-10k, 8% discount
# Total shopping above 4k-7k, 6% discount
# Total shopping above 2k-4k, 4% discount
# Total shopping below 2k, no discount
# Amount before discount
# Discount= Rs
# Amount after discount


print("Enter your shopping amount")
amount=int(input())
if amount>=10000:
    discount= 0.10* amount
elif amount>=7000 and amount<10000:
    discount= 0.08* amount
elif amount>=4000 and amount<7000:
    discount= 0.06* amount
elif amount>=2000 and amount<4000:
    discount= 0.04* amount
elif amount<2000:
    discount=0
    
print("Amount before discount", amount)
print("Amount of discount", discount)
print("Net payable ", amount-discount)



    






l









    
    


















