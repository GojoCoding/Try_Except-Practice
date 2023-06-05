user_dec = int(input("Type 1 for exception or 2 for no exception: "))
try:  # Something that might cause an exception, probably not but just in case
    if user_dec == 1:
        y = 10 / 0
    else:
        y = 10 / 1
except ZeroDivisionError:  # Do this if there was an exception
    print("Error: Division by zero occured")
else:  # Do this if there were no exceptions
    print("No exception within try block of code")
finally:  # Do this no matter what happens
    print("This code will run no matter if an exception was caught or not")

print()
try:
    file = open("a_file.txt")
    a_dictionary = {"Key": "value"}
    print(a_dictionary["kjsdfj"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
# More than 1 except can be used to catch multiple exceptions in try block of code
except KeyError as error_message:  # Get hold of error message and use it when exception is caught!!!!
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    # raise TypeError("This is an error that I made up")

print()
# You would want to raise errors when the code is perfectly valid but will generate wrong results
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 9:
    raise ValueError("Human height should not be over 9 feet")

bmi = weight / height ** 2
print(bmi)

