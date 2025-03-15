# # # print("Hello from lesson 7")
# # # #  Lesson 7 - For Loop (Part 2)

# # # ## Recap 1: Debugging Average Score Program

# # # ### There is a total of 3 bugs in the following program.
# # # ### Identify and fix the bugs:

# # # score_one = 80
# # # score_two = 90
# # # score_three = 75

# # # total = score_one + score_two + score_three

# # # average_score = total / 3

# # # student_name = "Alex"

# # # print("Average score for " + student_name  + " is: " + str(average_score))

# # # print(round(average_score))







# # # Task 1
# # # for i in range(1, 11):
# # #     print(i)


# # # Task 2
# # # for i in range(2, 21, 2):
# # #     print(i)


# # # Task 3
# # # for i in range(10, 0, -1):
# # #     print(i)








# # # word = input("What word would you like to repeat?")

# # # Repetitivenumber = int(input("How many times would you like it to repeat?"))

# # # for i in range(Repetitivenumber, ):
# #     # print(word)




# # # name = input("What is your name?")
# # # TheRepeatedNumber = int(input("How many times would you like to repeat it?"))
# # # 
# # # for i in range(TheRepeatedNumber,):
# #     # print(("nice to meet you, " + name) + "!")





# # # sum = 0

# # # for n in range(1,6):
# # #     sum = sum + int(input("What is number " + str(n)))

# # # print(sum)




# # TimeTableNumbure = int(input("What number would you like to see the timetable of? "))
# # for i in range(1 , 13):
# #     print(str(TimeTableNumbure) + " x " + str(i) + "=" + str( i * TimeTableNumbure))

























































# num = int(input("Give me a number to make a number pyramid: "))

# for i in range(1, num +1):
#     print(str(i) * i)

# sum  = 0

# for i in range(1, 6):
#     sum = sum + int(input("What is the score of student #" + str(i) + "?" ))

#     average = sum / 5

# print("The average score for the five students is " +  str(average)1)







sum  = 0

numstudents = int(input("How many students do you have?"))

for i in range(1, numstudents):
    sum = sum + int(input("What is the score of student #" + str(i) + "?" ))

    average = sum / 5

print("The average score for the " + int(numstudents) + "is " +  average)