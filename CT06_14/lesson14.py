# # # # # Order = [
# # # # # "Mushroom 🤮",
# # # # # "pepperoni😁",
# # # # # "Cheese😍"
# # # # # "Extra cheese 😍😍😍"]

# # # # # User = []
# # # # # print("The Availiable toppings are:")

# # # # # for i in range(len(Order)):
# # # # #     print(str(i+1) + ". " + Order[i])

# # # # # while True:
# # # # #     user_input = input("Please choose your pizza topping by number:")
# # # # #     if user_input == "end" :
# # # # #         break
# # # # #     else:
# # # # #         User.append(Order[int(user_input) - 1])
        
# # # # # for i in user_input:
# # # # #     print(i)






# # # # import turtle 

# # # # window = turtle.Screen()

# # # # window.setup(width=600, height=400)

# # # # t = turtle.Turtle 

# # # # t.shape("turtle")

# # # # window.mainloop()

# # # counter = 0

# # # def increment_counter ():
# # #     global counter
# # #     counter += 1

# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()
# # # increment_counter()

# # # print(counter)






# # def IsEven (num):
# #     return num % 2 == 0

# # numbers = [1,2,3,4,5,6,7,8,9]

# # for n in numbers:
# #     if IsEven(n):
# #         print(str(n) + " is even")
# #     else:
# #         print(str(n) + " is odd")








def square(num):
    return num*num

print(square((5)))

def sum_of_squares(num1, num2):
    return square(num1) + square(num2)

print(sum_of_squares)