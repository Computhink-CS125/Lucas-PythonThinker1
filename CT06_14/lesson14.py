Order = [
"Mushroom 🤮",
"pepperoni😁",
"Cheese😍"
"Extra cheese 😍😍😍"]

User = []
print("The Availiable toppings are:")

for i in range(len(Order)):
    print(str(i+1) + ". " + Order[i])

while True:
    user_input = input("Please choose your pizza topping by number:")
    if user_input == "end" :
        break
    else:
        User.append(Order[int(user_input) - 1])
        
for order in user_input:
    print(order)






