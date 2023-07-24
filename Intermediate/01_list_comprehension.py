### LIST COMPREHENSION
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_original_list)

my_range = range(8)
print(list(my_range))

print(" --- " * 10) ### DEFINITION

my_list = [i + 1 for i in range(10)]
print(my_list)

my_list = [i * 2 for i in range(20)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(num):
    return num + 5

my_list = [sum_five(i) for i in range(10)]
print(my_list)