# Referential arrays 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

list1.extend(list2)
list2[3] = 16

print(list1) #Last value is 9 still
print(list2) #Last value is 16 