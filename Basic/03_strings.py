my_string = "my String"
my_other_string = "my other string"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "This is a string\nwhit line break"
print(my_new_line_string)

my_tab_string = "\tThis is a string with tab"
print(my_tab_string)

my_scape_string = "\tThis is a string \n with scape"
print(my_scape_string)

### format
name, nick, age = "acs", "cso", 34
print("my name is {} {} and my age is {}".format(nick,name,age))
print("My name is %s %s and my age is %d" % (name, nick, age))
print("My name is " + name + " " + nick + " and my age is " + str(age))
print(f"my name is {name} {nick} and my age is {age}")

### character unboxing
language = "python"
a,b,c,d,e,f = language
print(a)
print(e)

### division 
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

reversed_language = language[::-1]
print(reversed_language)

### functions
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))
print("Py" == "py")