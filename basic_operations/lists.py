#List Comprehension = Short for loops with a function
my_list = ['a','b','c','d','e','f']
# [operación "for" variable "in" lista]
new_list = [x.upper() for x in my_list]
print(new_list)