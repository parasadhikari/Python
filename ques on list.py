#seperate odd and even no. from given list
list1=[7,8,9,3,4,6,8,1]
even=[]
odd=[]

for i in list1:
    if i%2==0:
        even.append(i)
    else:
            odd.append(i)
print("even list is",even)
print("odd list is",odd)

#given a list,calculate square of each number of alist and store the result in seperate list
list1=[4,2,5,7]
square=[]

for i in list1:
    square.append(i*i)

print(square)
