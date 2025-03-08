# # Test.py
# # Write a PYTHON program that asks for user's name. The program should generate a greeting message mentioning the user's name.


# name = input("What is your name? ") # Asking the user his/her name

# print("Nice to meet you, " + name + "!") # The output of what it is supposed to print


start = int(input("What number would you like to start with? "))
end = int(input("What number would you like to end with? "))
increment = int(input("What number would you like to be an increment of? "))

for i in range(start, end + 1, increment):
    print(i)