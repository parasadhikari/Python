#typecasting or tyconversion
#converting one type of data to another form

#point_______________>>>>1
#conversion of non string datatype to starng datatype

##x=12
##print("before conversion x is",x,"and type is",type(x))
##
##y=str(x)
##print("after conversion x is",y,"and type is",type(y))
##  #but we cant add no. in y as its now become string and string cant add int

#********************************************************************
#float to string
##x=12.2
##print("before conversion x is",x,"and type is",type(x))
##
##y=str(x)
##print("after conversion x is",y,"and type is",type(y))
  #but we cant add no. in y as its now become string and string cant add int




#bollean to string
##x=True
##print("before conversion x is",x,"and type is",type(x))
##
##y=str(x)
##print("after conversion x is",y,"and type is",type(y))
  #after conversion thatvtrue will be normal string not bollean



#COMPLEX NUMBER
##x=56+14j
##print("before conversion x is",x,"and type is",type(x))
##
##y=str(x)
##print("after conversion x is",y,"and type is",type(y))







#point---------->>>>2
#float to int
##x=56.14
##print("before conversion x is",x,"and type is",type(x))
##
##y=int(x)
##print("after conversion x is",y,"and type is",type(y))



#bollean to integer
##false==0
##true==1

##x=False
##print("before conversion x is",x,"and type is",type(x))
##
##y=int(x)
##print("after conversion x is",y,"and type is",type(y))



#complex to integer
##x=56+14j
##print("before conversion x is",x,"and type is",type(x))
##
##y=int(x)
##print("after conversion x is",y,"and type is",type(y))

#***********throw erro bcz + sign***************
##x=56+14j
##print(x)
##print(type,(x))
##
##print("real part is",x.real)
##print("real part is",x.imag)
##
##y=int(x.real)
##print("after conversion x is",y,"and type is",type(y))
##
##y=int(x.imag)
##print("after conversion x is",y,"and type is",type(y))







#string to int---->not possible
#but no. in double quotes can be change in int

##x="345"
##print("before conversion x is",x,"and type is",type(x))
##
##y=int(x)
##print("after conversion x is",y,"and type is",type(y))




#point---------->>>>3
#conversion of non-bollean to bollean

#a.int to bool
#if no. positive or negative except "0"------>true
##if no. is "0"------>false

##x=3456
##print("before conversion x is",x,"and type is",type(x))
##
##y=bool(x)
##print("after conversion x is",y,"and type is",type(y))


##x=-3456
##print("before conversion x is",x,"and type is",type(x))
##
##y=bool(x)
##print("after conversion x is",y,"and type is",type(y))



##x=0
##print("before conversion x is",x,"and type is",type(x))
##
##y=bool(x)
##print("after conversion x is",y,"and type is",type(y))



#a.float to bool------->>>only 0.0 will give false

##x=0.0
##print("before conversion x is",x,"and type is",type(x))
##
##y=bool(x)
##print("after conversion x is",y,"and type is",type(y))



#c. string  to bool----->empty will give false only

##x=""
##print("before conversion x is",x,"and type is",type(x))
##
##y=bool(x)
##print("after conversion x is",y,"and type is",type(y))



##x="  "
##print("before conversion x is",x,"and type is",type(x))
##
##y=bool(x)
##print("after conversion x is",y,"and type is",type(y))




#complex-->bollean--->at real and img both part is "0" give false
##x=0+0j
##print("before conversion x is",x,"and type is",type(x))
##
##y=int(x)
##print("after conversion x is",y,"and type is",type(y))



##x=2+0j
##print("before conversion x is",x,"and type is",type(x))
##
##y=int(x)
##print("after conversion x is",y,"and type is",type(y))














