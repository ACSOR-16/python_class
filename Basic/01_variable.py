### variable

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

### Concatenation of variables in a print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("This is a value a:", my_bool_variable)

### some functions of the system
print(len(my_string_variable))

# variables in a only line, warning with this
name, surname, alias, age = "Oscar", "Zev", "Cso", 25
print("My name is:", name, surname, ". my age is:",
      age, ". And my nick is:", alias)

# Inputs
name = input("What is your name?")
age = input("how old are you?")
print(name)
print(age)

## Inputs
name = 35
age = "Bras"
print(name)
print(age)

### do we force the type?
address: str = "My address"
address = True
address = 5
address = 1.2
print(type(address))
