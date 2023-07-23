### loops

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("my condition is mayor than 10")

print("continue execute")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Execute finished")
        break
    print(my_condition)

print("continue execute")

my_list = [30, 20, 15, 10, 25, 35, 40]

for element in my_list:
    print(element)

my_tuple = ("a", "f", "c", "d", "e", "e")

for element in my_tuple:
    print(element)

my_set = {1, 5, 6, 7, 3, 4, 4}

for element in my_set:
    print(element)

my_dict = {
    "name": "Bras", 
    "lastname": "Mou", 
    "age": 35, 
    1: "Python"
}

for element in my_dict:
    print(element)
    if element == "age":
        break
    print("is runs")
else:
    print("loops finished")

print(" --- " * 10)