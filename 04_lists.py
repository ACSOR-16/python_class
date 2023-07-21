### lists

my_list = list()
my_other_list = []

print(len(my_list))


my_list = [35, 24, 62, 52, 60, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.75, "oscar", "Aguirre"]
print(type(my_list))
print(type(my_other_list))

### elements access and search
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
##print(my_other_list[4]) list index out of range
##print(my_other_list[-5]) list index out of range

print(my_other_list.index("oscar"))

age, height, surname, name = my_other_list
print(name, surname)
#equal
age, height, name, lastname = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]
print(age, name)

#concatenation
print(my_list + my_other_list)
##print(my_list - my_other_list)

#create, insertion, update and delete

my_other_list.append("Tara")
print(my_other_list)

my_other_list.insert(1, "Red")
print(my_other_list)
#replace
my_other_list[1] = "Black"
print(my_other_list)

my_other_list.remove("Black")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)
#pop remove and return item last or index
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

### lists operations
my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

### Sublist
print(my_new_list[1:3])

#type change
my_list = "Hello World"
print(my_list)
print(type(my_list))