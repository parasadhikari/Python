##########set operation##############
#1.union
#2.intersection
#3.difference
#4.symmetric_difference

s1={10,15,17,18}
s2={5,6,20,18}
##x=s1.union(s2)
x=s1|s2
print("union of s1 and s2 is:",x)


s1={10,15,17,18}
s2={5,6,20,18}
s1.update(s2)
print("update of s1 and s2 is:",s1)##i.e s1 ki value change ho gyi ab yani union is stored in s1


##......................................................................................................................................................................................

s1={10,15,17,18}
s2={5,6,20,18}
##x=s1.intersection(s2)
x=s1&s2
print("intersection of s1 and s2 is:",x)



s1={10,15,17,18}
s2={5,6,20,18}
s1.intersection_update(s2)
print("intersection update of s1 and s2 is:",s1)

##......................................................................................................................................................................................
s1={10,15,17,18}
s2={5,6,20,18}
##x=s2.difference(s1)
x=s2-s1
print("difference of s1 and s2 is:",x)



s1={10,15,17,18}
s2={5,6,20,18}
s2.difference_update(s1)
print("difference_update of s1 and s2 is:",s2)

##......................................................................................................................................................................................

s1={10,15,17,18}
s2={5,6,20,18}
##x=s2.symmetric_difference(s1)
x=s2^s1
print("symmetric_difference of s1 and s2 is:",x)



s1={10,15,17,18}
s2={5,6,20,18}
s2.symmetric_difference_update(s1)
print("symmetric_difference_update of s1 and s2 is:",s2)

##......................................................................................................................................................................................

s1={10,15,17}
s2={5,6,20}

print(s1.isdisjoint(s2))

