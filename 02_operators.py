### arithmetic operations
print(5 + 6)
print(7 - 3)
print(5 * 8)
print(5 / 2)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 //4)

### operations with string
print("Hi " + "Python" + " how are you?")
print("Hello " + str(5))

### mixed operations
print("Hi " * 5)
print("Hi " * (2 ** 3))

my_float = 2.5 * 2
print("Hi " * int(my_float))

### Comparative operators

### integer operators
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

### string operators
print("Hi" > "Python")
print("Hi" < "Python")
print("aaa" >= "aba") # ASCII
print(len("aaaa") >= len("aba"))
print("Hello" <= "Python")
print("Hello" == "Python")
print("Hello" != "Python")

### logic operators
print(3 > 4 and "Hi" > "Python")
print(3 > 4 or "Hi" > "Python")
print(3 < 4 and "Hi" < "Python")
print(3 < 4 or "Hi" > "Python")
print(3 < 4 or ("Hi" > "Python" and 4 == 4))
print(not(3 > 4))