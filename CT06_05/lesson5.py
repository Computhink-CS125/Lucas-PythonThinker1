# # # # we print the for loop to printingtons the numba from 2 too 24!!! in multiples of 2!!!!!!!!!!!! hehehaha








# # # for i in range(2, 25, 2):
# # #     print(i)

# # for e in range(8, 97, 8):
# #     print(e)


# for d in range(5, 0, -1):
#     print(d)


startingtons = int(input("What integer would you like to start with? "))
endingtons = int(input("What integer would you like to end with? "))

if endingtons > startingtons:
    for i in range(startingtons, endingtons, 1):
        print(i)
else:
    for i in range(startingtons, endingtons, -1):
        print(i)