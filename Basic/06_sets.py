#definition

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #first dict

my_other_set = {"oscar", "aguirre", 25}
print(type(my_other_set)) #second set
print(len(my_other_set))

#insertion

my_other_set.add(1998)
print(my_other_set) # doesn't order structure
my_other_set.add(1998)
print(my_other_set) # no add repeat

#search
print("oscar" in my_other_set)
print(7 in my_other_set)

# elimination

my_other_set.remove(1998)
print(my_other_set)

my_other_set.clear() # empty set
print(len(my_other_set))

print(my_other_set)
del my_other_set # delete set

# transformation

my_set = {"will", "taz", 26}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"javascript", "python", "java"}
print(my_other_set)

# others operations

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))