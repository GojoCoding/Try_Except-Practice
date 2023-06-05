user_dec = int(input("Type 1 for exception or 2 for no exception: "))
try:
    if user_dec == 1:
        y = 10 / 0
    else:
        y = 10 / 1
except ZeroDivisionError:
    print("Error: Division by zero occured")
else:
    print("No exception within try block of code")
finally:
    print("This code will run no matter if an exception was caught or not")

# How am i gonna get this into git and github??? thats the real things i want to learn before i move forward
# Get to publish all my work for this summer into github so i got something to show that I have been coding and
# creating projects2

# Do i start with local repo i made from Odin Project?