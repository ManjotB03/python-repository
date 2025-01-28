def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(divisors(12))

# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

def factor(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    return False

# Example usage
print(factor(12, 7))

def is_prime(input_value):
#     # Handle invalid inputs
      try:
          n = int(input_value)
      except ValueError:
          return "Please enter a valid integer."

#     # Check if the number is prime
      if n < 2:
          return False
#
#     # Check for divisors up to square root of n
      for i in range(2, int(n ** 0.5) + 1):
          if n % i == 0:
              return False
#
      return True