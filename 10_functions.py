### Functions
# definition

def my_function():
    print("my functions runs")

my_function()
print(" --- " * 10)

#function with parameters
def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 15)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)
print(" --- " * 10)

# function with open parameters and return
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(sum_two_values(2,8))

my_result = sum_two_values(0.54, 3.4)
print(my_result)
print(" --- " * 10)

# args key

def print_name(name, surname):
    print(f"{name}, {surname}")

print_name(name="oscar", surname="aguirre")

def print_name_with_default(name, surname, nickname="has no nick"):
    print(f"{name} {surname}, {nickname}")


print_name_with_default("oscar", "aguirre")
print_name_with_default("will", "tara", "Cso")
print(" --- " * 10)

# functions with parameters input/arg random


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("hi", "Python", "Mou")
print_upper_texts("hi")