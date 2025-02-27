print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a: print(x[:5])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b: for num in x:
#          if num % 2 == 0:  # Checks if number is even
#             print(num)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c: even_up_to_fifth = [num for num in x[:5] if num % 2 == 0]
#      print(even_up_to_fifth)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a: first_letters = [name.split()[0][0] for name in names]
#      print(first_letters)




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b: space_indices = [name.index(" ") for name in names]
#      print(space_indices)




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c: initials = [name.split()[0][0] + name.split()[1][0] for name in names]
#      print(initials)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a: no_duplicates = [list for list in list_of_lists if len(list) == len(set(list))]
#      print(no_duplicates)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a: number = 0
# # Keep asking until a number greater than 100 is entered
# while number <= 100:
#     try:
#         number = int(input("Please enter a number greater than 100: "))
#         if number <= 100:
#             print("That number is not greater than 100. Please try again.")
#     except ValueError:
#         print("That's not a valid number. Please try again.")
#
# # Print the valid number that was entered
# print(f"Thank you for entering a number greater than 100: {number}")


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b: prime = True
# if number > 1:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             prime = False
#             break
#
# else:
#     prime = False
#
# if prime:
#     print('it is a prime number')
# else:
#     print('it is not a prime number')





