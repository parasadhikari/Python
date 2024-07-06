
#ques1--->.Take values of length and breadth of a rectangle
#  from user and check if it is square or not.

##print("enter the value of length:")
##l=int(input())
##
##print("enter the value of breadth:")
##b=int(input())
##
##if l==b:
##    print("it is a square")
##
##else:
##    print("its not a square")






#ques2.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

##print("please enter your year of dervice to the company")
##year=float(input())
##
##print("please enter your year salary provided by the company")
##salary=float(input())
##
##if year>5:
##    print("salary earlier is :",salary)
##    new=salary+5*salary/100
##    print("incremented salary is:",new)
##
##else:
##    print("salary is same:",salary)



##QUES3.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
##Ask user for quantity
##Suppose, one unit will cost 100.
##Judge and print total cost for user.
##print("each quantity cost is:100")
##
##print("enter the total quantity purchased by customer")
##q=int(input())
##
##total=100*q
##print("total cost is:",total)
##                
##if q>10:
##        print("your discounted price is:",(total)-(10/100)*total)
##
##elif q<=10:
##        print("OPPS! you got no discount")




##QUES4.A school has following rules for grading system:
##a. Below 25 - F
##b. 25 to 45 - E
##c. 45 to 50 - D
##d. 50 to 60 - C
##e. 60 to 80 - B
##f. Above 80 - A
##Ask user to enter marks and print the corresponding grade.
##print("Please enter your respected marks:")
##marks=float(input())
##
##if marks<0:
##    print("Please enter valid marks")
##
##if 0<marks<=25:
##        print("F")
##
##if 25<marks<=45:
##        print("E")
##
##if 45<marks<=50:
##        print("D")
##
##if 50<marks<=60:
##        print("C")
##
##if 60<marks<=80:
##        print("B")
##
##if 80<marks<=100:
##        print("A")
##
##if marks>100:
##    print("Please enter valid marks")




####QUES5.Take input of age of 3 people by user and determine oldest and youngest among them.
##print("Please enter the respected age of yours:")
##a=int(input())
##
##print("Please enter the respected age of yours:")
##b=int(input())
##
##print("Please enter the respected age of yours:")
##c=int(input())
##
##if a>b and a>c:
##        print("oldest among 3 people is",a,":")
##
##if b>a and b>c:
##        print("oldest among 3 people is",b,":")
##
##if c>b and c>a:
##        print("oldest among 3 people is",c,":")
##
##if a<b and a<c:
##        print("youngest among 3 people is",a,":")
##
##if b<a and b<c:
##        print("youngest among 3 people is",b,":")
##
##if c<b and c<a:
##        print("youngest among 3 people is",c,":")




##QUES6.Write a program to print absolute vlaue of a number entered by user. E.g.-
##INPUT: 1        OUTPUT: 1
##INPUT: -1        OUTPUT: 1
##print("enter the random number:")
##num=int(input())
##
##
##if num>1:
##        print("absolute value is",num)
##
##elif num<1:
##        absolute=num*-1
##print("absolute value is",absolute)




##QUES7.A student will not be allowed to sit in exam if his/her attendence is less than 75%.
##Take following input from user
##Number of classes held
##Number of classes attended.
##And print percentage of class attended
##Is student is allowed to sit in exam or not.
##print("please enter the no. of total classes held :-")
##total=int(input())
##
##print("please enter the no. of total classes attend by the student :-")
##attend=int(input())
##
##percent=(attend/total)*100
##print("the percentage of class attend by student is:-",percent)
##
##
##if percent>100:
##    print("not valid as percentage is only possible upto 100")
##
##elif 0<=percent<75:
##    print("Student will not be allowed to sit in exam ")
##
##elif 75<percent<=100:
##    print("Student will be allowed to sit in exam ")




##QUES8.Modify the above question to allow student to sit if he/she has medical cause.
##Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
##print("please enter the no. of total classes held :-")
##total=int(input())
##
##print("please enter the no. of total classes attend by the student :-")
##attend=int(input())
##
##percent=(attend/total)*100
##print("the percentage of class attend by student is:-",percent)
##
##
##if percent>100:
##    print("not valid as percentage is only possible upto 100")
##
##
##elif 75<percent<=100:
##    print("Student will be allowed to sit in exam ")
##
##
##elif 0<=percent<75:
##    print("Your percentage is low,SO does you have any medical ceritficate (Y/N):-")
##    ans=input()
##
##if ans=='Y':
##    print("you can sit on the exam")
##        
##
##elif ans=='N':
##     print("You can't sit on the exam")
##
##       
##else:
##     print("Student will not be allowed to sit in exam ")





##QUES9.Write a program to check if a year is leap year or not.
##If a year is divisible by 4 then it is leap year but
##if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
##print("please enter the year to check weather it is leap year or not")
##year=int(input())
##
##if year<=0:
##    print("please enter the valid year")#FALSE CONDITION PE BREAK KRNA HH
##
##if year%4==0 and year%100!=0:
##    print("its a leap year")
##
##if year%400==0:
##     print("its a leap year")
##
##else:
##    print("not a leap year")





##QUES10. Ask user to enter age, sex ( M or F ), marital status ( Y or N )
##and then using following rules print their place of service.
##if employee is female, then she will work only in urban areas.
##if employee is a male and age is in between 20 to 40 then he may work in anywhere
##if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
##And any other input of age should print "ERROR".
##print("Please enter your AGE")
##age=int(input())
##
##print("Please enter your Sex M or F")
##sex=input()
##
##print("Please enter your Marital Status weather married(Y) or not(N) ")
##marital=input()
##
##
##if sex=='F':
##    print("She will work only in urban areas")
##
##elif sex=='M' and 20<age<=40:
##    print("He may work in anywhere")
##
##elif sex=='M' and 40<age<=60:
##    print("He will work in urban areas only")
##
##else:
##    print("ERROR")




##QUES 11. A 4 digit number is entered through keyboard.
##Write a program to print a new number with digits reversed as of orignal one. E.g.-
##INPUT : 1234        OUTPUT : 4321
##INPUT : 5982        OUTPUT : 2895
##
##Write a python program that will check for the following conditions:
##print("enter the number to be reversed")
##num=int(input())
##
##rev=0
##while(num>0):
##    last=num%10
##    rev=rev*10+last
##    num=num//10
##
##print("reverse no. is",rev)

    


##QUES12.If the light is green – Car is allowed to go
##If the light is yellow – Car has to wait
##If the light is red – Car has to stop
##Other signal – unrecognized signal. Example black, blue, etc…
##print("enter the signal color")
##color=str(input())
##
##if color=='green':
##    print("Car is allowed to go")
##
##elif color=='yellow':
##    print("Car has to be wait")
##
##elif color=='red':
##    print("Car has to be stop")
##
##else:
##    print("unrecognized signal")




##QUES13. Write a program to trace your subject mark. Your program should fulfill the following conditions:
##1.If the subject mark is below 0 and above 100,
##print “error: mark should be between 0 and 100 only”
##
##2.Students will fail in the subject if their mark is below 50.
##
##3.Students will pass in the subject if they score 50 and above.
##a.  If subject mark is between 50 and 60, grade student as good.
##b.  If subject mark is between 60 and 80, grade student as very good.
##c.  If subject mark is between 80 and 100, grade student as outstanding.
##Make sure to print their mark in every statement to prove that the condition is fulfilled.
##print("Please enter the marks of your respective subjects")
##marks=float(input())
##
##if 0<=marks<50:
##    print("OPPS!you got fail in the respective subject")
##
##    
##elif 50<=marks<60:
##    print("GOOD")
##
##elif 60<=marks<80:
##    print("VERY GOOD")
##
##elif 80<=marks<100:
##    print("OUTSTANDING")
##
##else:
##    print("error: mark should be between 0 and 100 only")
##




##QUES14. Write a program to check whether the number is of one digited or two digited
##or three digited or more than three digited.
##print("please enter the random digit ")
##num=int(input())
##
##if 0<num<10 or -10<num<0:
##    print("Number is of one digited")
##
##elif 10<=num<100 or -100<num<9:
##    print("Number is of two digited")
##
##elif 100<=num<1000 or -1000<num<99:
##    print("Number is of three digited")
##
##else:
##    print("More than three digited")





##QUES15.Write a program to check whether the given character is an uppercase letter
##       or lowercase letter or a digit or a special character.

##print("enter a character")
##x=input()
##
##if ord(x)>=65 and ord(x)<=91:
##    print("you have entered upparcase character")
##
##elif ord(x)>=97 and ord(x)<=122:
##    print("you have entered lowercase character")
##
##elif ord(x)>=48 and ord(x)<=57:
##    print("you have entered a digit")
##
##else:
##    print("You have enter a special character")















