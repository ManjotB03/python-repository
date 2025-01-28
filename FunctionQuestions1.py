print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:def divisors(n):
#     return [i for i in range(1, n+1) if n % i == 0]
#
#
# print(divisors(12))  # Output: [1, 2, 3, 4, 6, 12]
# print(divisors(10))



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b: def factor(num1, num2):
#     if num1 % num2 == 0 or num2 % num1 == 0:
#         return True
#     return False
#
# # Example usage
# print(factor(12, 4))



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a: def letter_position(letter):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#
#     # Convert letter to lowercase to handle both upper and lower case inputs
#     letter = letter.lower()
#
#     # Return the position (adding 1 since list indices start at 0)
#     return alphabet.index(letter) + 1
#
# print(letter_position('A')) #should print 1



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b: def get_name_id(name):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#
#     id_number = ""
#
#     # Convert each letter to its position and add to ID
#     for letter in name.lower():
#         position = alphabet.index(letter) + 1
#         id_number += str(position)
#
#     return id_number
#
#
# # Test cases
# print(get_name_id("manjot"))



print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c: def id_to_password(id_str):
#     id_number = int(id_str)
#
#     digit_sum = sum(int(digit) for digit in id_str)
#
#     password = id_number - digit_sum
#     return password
#
# id_str = "1141"  # Example ID for "bob"
# print(id_to_password(id_str))  # Output: 1134



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a: def prime(n):
#     # numbers less than 2 (not prime)
#     if n < 2:
#         return False
#
#     # Check for divisors up to square root of n
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# # Test cases
# print(prime(13))  # Should print True
# print(prime(12))



print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b: def is_prime(input_value):
#     # Handle invalid inputs
#     try:
#         n = int(input_value)
#     except ValueError:
#         return "Please enter a valid integer."
#
#     # Check if the number is prime
#     if n < 2:
#         return False
#
#     # Check for divisors up to square root of n
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#
#     return True

#print(is_prime(7)) #should print true
#print(is_prime('djc'))#should print 'please enter a valid integer'



# -------------------------------------------------------------------------------------- #






