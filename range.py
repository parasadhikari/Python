#RANGE IN PYTHON
#range() take 3 paramater
#first parameter is start(include default)=its optional i.e default star with "0"
#second parameter is end(exclude)=its mandatory
#third parameter is step(posiyive/negative)=optional
#i.e it specify the gap which we want btween loop------>>so default difference is 1



#to print 1-20 num 
##x=range(1,21)
##
##
###using loop
##for i in x:
##    print(i)



#question 2>>
##for i in range(5,10):
##    print(i*2+i*3%2)



###question 2>>
##for i in range(5,10):
##    print(i+i//2-i)



#if we want backward counting
##for i in range(10,1,-1):
##     print(i)



###question 2>>
##for i in range(20,0,-5):
##    print(i+i*2+i**3)





                        #NESTING for loop






#ques 1
##for i in range(1,4):
##    for j in range(1,3):
##        print(j)




#ques 2
##for i in range(3,5):
##    for j in range(10,14):
##        print(i)



#ques 3
##for i in range(5,10,2):
##    for j in range(0,3):
##        print(i,j)





#ques 4
##for i in range(5,10,2):
##    for j in range(0,3):
##        print(i+j-2)




#for creating in one line

##for i in range(1,5):
##    for j in range(1,5):
##        print(j, end=" ")
##    print() 





##for i in range(1,5):
##    for j in range(1,5):
##        print(j, end=",")
##    print() 




##for i in range(0,3):
##    for j in range(5,10,2):
##        print(j, end=" ")
##    print()





#to print:
#5  4  3  2  1
#5  4  3  2  1
#5  4  3  2  1
#5  4  3  2  1
#5  4  3  2  1
##for i in range(0,5):
##    for j in range(5,0,-1):
##        print(j, end=" ")
##    print()






for i in range(1,3):
    for j in range(5,0,-2):
        print(j+i//2, end=" ")
    print()









