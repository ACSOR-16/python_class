### dictionaries

# definition

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { 
    "name": "oscar", 
    "lastname": "aguirre", 
    "age": 23
}

my_dict = {
    "name": "will",
    "lastname": "Tara",
    "age": 25,
    "language": ["python", "javascript"],
    1: 17.7
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

# Search

print(my_dict[1])
print(my_dict["lastname"])

print("oscar" in my_dict)
print("language" in my_dict)

# insertion
my_dict["street"] = "Jr. Tara"
print(my_dict)

# update

my_dict["name"] = "Alexander"
print(my_dict["name"])

# elimination
del my_dict["street"]
print(my_dict)

# other operations

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["name", 1, "floor"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("name", 1, "floor"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Mou")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))