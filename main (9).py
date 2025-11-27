"""
def Add_numbers(num1, num2):
  return num1 + num2 
  
a = Add_numbers(1440, 1160)
print(a)

def Sum_of_two_numbers(num1, num2):
  sum = num1 + num2
  print("Sum of the given two numbers is ", sum)
  
Sum_of_two_numbers(8146, 3146)
""" 
'''
def pass_statement(a):
  pass 

print(pass_statement(5))

def find_square(num):
  square = num * num 
  return square
  
print(find_square(252))

print(pow(165,2))



import math
sr = math.sqrt
print(sr(25))

'''

'''
def greet(name, message="Hello"):
    print(message, name)

# calling function with both arguments
greet("Alice", "Good Morning")

# calling function with only one argument
greet("Bob")


# function to sum any number of arguments
def add_all(*numbers):
    return sum(numbers)

# pass any number of arguments
print(add_all(1, 2, 3, 4, 65, 462, 645))   


def add_nums(*numbers):
  print(sum(numbers))
  
add_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  




# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")


def g_1(**words):
  for k, v in words.items():
    print(k, ':', v)
 
g_1(name = "JOhny", greeting = "Hello")  
#g_1("hello", "hi", "bye", "good bye")
'''
'''
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 5
print("The factorial of", num, "is", factorial(num))



def factorial(num):
  if num == 1:
    return num 
  else:
    return(num * factorial (num - 1))
    
print(factorial(5))
'''

print("Hi")














