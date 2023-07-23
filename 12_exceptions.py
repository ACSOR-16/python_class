### exception handling

number_one = 3
number_two = 5
number_two = "5"

try:
    print(number_one + number_two)
except:
    #runs if reproduced a exception
    print("the error has occurred")

print(" --- " * 10)
# Complete flow of an exception: try except else finally

try:
    print(number_one + number_two)
    print("an error has not occurred")
except:
    print("the error has occurred")
else:  # Optional
    # Runs if has not occurred a exception
    print("execution continues correctly Else")
finally:  # Optional
    # runs always
    print("execution continues correctly finally")

print(" --- " * 10)
# type exceptions

try:
    print(number_one + number_two)
    print("the error has no ocurred")
except ValueError:
    print("an error has ocurred ValueError")
except TypeError:
    print("an error has ocurred TypeError")

print(" --- " * 10)
# Capture the exception information

try:
    print(number_one + number_two)
    print("the error has not occurred")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)