### tuples 

### definition

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (20, 1.8, "liz", "Piston", "Fer")
my_other_tuple = (30, 50, 60, 20, 10)

print(my_tuple)
print(my_other_tuple)

### elements access and search

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) # indexError
#print(my_tuple[-5]) # indexError

print(my_tuple.count("liz"))
print(my_tuple.index("Piston"))
print(my_tuple.index("liz"))

#my_tuple[1] = 1.75 doesn't support item assignment

# Concatenation
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

#sub_tuples
print(my_sum_tuple[3:6])

#tuple mutable to a list

my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Ada"
my_tuple.insert(1, "Blue")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# delete

# del my_tuple[2] # object doesn't support item deletion
del my_tuple
# print(my_tuple) # is not defined