# # # # # # # # # # # # # Test.py
# # # # # # # # # # # # # Write a PYTHON program that asks for user's name. The program should generate a greeting message mentioning the user's name.


# # # # # # # # # # # # name = input("What is your name? ") # Asking the user his/her name

# # # # # # # # # # # # print("Nice to meet you, " + name + "!") # The output of what it is supposed to print


# # # # # # # # # # # start = int(input("What number would you like to start with? ")) # Asking the user what number would the user wants to start with.
# # # # # # # # # # # end = int(input("What number would you like to end with? ")) # Asking the user what number the user wants to end with.
# # # # # # # # # # # increment = int(input("What number would you like to be an increment of? ")) # Asking the user what number can the increment be.

# # # # # # # # # # # for i in range(start, end, increment): # counting from the start to end with the increment of the user's selected number.
# # # # # # # # # # #     print(i) # The output of what it is supposed to print 
# # # # # # # # # # age = input("What is your age")
# # # # # # # # # # futureAge = age + 2
# # # # # # # # # # print(futureAge)

# # # # # # # # # x = int(input("First number? "))
# # # # # # # # # y = int(input("Second number? "))
# # # # # # # # # results = x + y / 2
# # # # # # # # # print(results)

# # # # # # # # batman = "10"
# # # # # # # # robin = "2"
# # # # # # # # print(batman + robin)


# # # # # # # age = 11
# # # # # # # name = "John"

# # # # # # # print(age + name)
# # # # # # for count in range(100, 0, -1):
# # # # # # 	print(count)





# # # # # name = "DENNIS"
# # # # # for letter in name:
# # # # # 	print(letter)






# # # # x = '1'
# # # # b = '1'
# # # # c = x + b



# # # # name = "DENNIS"
# # # # for letter in range(len(name)):
# # # # 	print(letter)
# # # x = int(input("First number? "))
# # # y = int(input("Second number? "))
# # # results = x + y / 2
# # # print(results)


# # age = 11
# # name = "John"

# # print(age + name)
# x = '1'
# b = '1'
# c = x + b


















































































































































































#Task 1
# Print numbers from 10 to 200 using the while loop


# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here

# num = 10

# while num <= 200 :
#     print(num)
#     num += 10



###################################################

# Task 2
# Code a password checker to protect your code!

# Assign a password "superpass123" to a variable
# Ask the user to enter a password
# If the password matches, print “Access Granted”
# If the password does not match, print “Access Denied”

# Write your code here

# Task 2
# Code a password checker to protect your code!

# Assign a password "superpass123" to a variable
# Ask the user to enter a password
# If the password matches, print “Access Granted”
# If the password does not match, print “Access Denied”

# Write your code here


# parswerd = "superpass123"

# user_input = input("What is the password?")
# if user_input == parswerd:
#     print("Access granted")
# else:
#     print("Access denied")











 
# Basic List Functions
# Do the following operations to the list provided below
# Write the code below each question.

planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]

# 1. Write code below to print the 3rd item 
#    in this list using index e.g. earth

print(planets[2])
# # 2. Write code to append neptune to this list.

planets.append("neptune")
print(planets)

# 3. Elon Musk has conquered Mars. 
#    Rename Mars in the list to be "muskworld"

planets[3] = "muskworld"

# 4. Remove uranus from this list.
planets.pop(6)


# 5. Using a for loop, print all the planets 
#    from this list one by one.

for i in planets:
    print(i)
    


    word = "hello"
    word = "hello 1 "
    word = word