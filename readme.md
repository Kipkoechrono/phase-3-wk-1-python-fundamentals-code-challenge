# Readme.md file 
This repository contains solutions to various Python programming challenges, including functions, object-oriented programming, and working with data structures such as sets and dictionaries.

## Table of Contents
1.Function: Add Numbers
2.Function: Reverse String
3.Function: Count Vowels
4.Function: Calculate Factorial
5.Function: Apply Decorator
6.Sequences: Sort List of Tuples
7.Sets and Dictionaries: Merge Dictionaries
8.Object-Oriented Programming: Class Creation
## Function: Add Numbers
Description:
This function takes two numbers as inputs and returns their sum.

Function:

def add_numbers(num1, num2):
    return num1 + num2
Example Usage:

print(add_numbers(3, 5))  # Output: 8
## Function: Reverse String
Description:
This function takes a string as input and returns the reversed version of that string.

Function:

def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello, World!"))  # Output: "!dlroW ,olleH"
## Function: Count Vowels
Description:
This function takes a string as input and returns the count of vowels (a, e, i, o, u), ignoring case sensitivity.

Function:

def count_vowels(text):
    text = text.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = sum(1 for char in text if char in vowels)
    return count
Example Usage:

print(count_vowels("Hello"))  # Output: 2
## Function: Calculate Factorial
Description:
This function takes a non-negative integer n and returns its factorial.

Function:

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
Example Usage:

print(calculate_factorial(5))  # Output: 120
## Function: Apply Decorator
Description:
This function applies a decorator to another function, printing a message before executing the original function.

Function:

def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

def apply_decorator(func):
    decorated_func = decorator_func(func)
    return decorated_func

def example_function():
    print("Original function called")
Example Usage:

decorated_function = apply_decorator(example_function)
decorated_function()
# Output:
# Decorator Applied
# Original function called

## Sequences: Sort List of Tuples
Description:
This function takes a list of tuples, where each tuple contains a name and age, and sorts the list by age in ascending order.

Function:

def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])
Example Usage:

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sort_by_age(people))
# Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

## Sets and Dictionaries: Merge Dictionaries
Description:
This function takes two dictionaries and merges them. If there are common keys, their values are summed.

Function:

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
Example Usage:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
# Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5} 

## Object-Oriented Programming: Class Creation
Description:
This class represents a car with attributes for make, model, and year. It also includes a method to display the car’s information.

Class:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")
Example Usage:

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
# Output: Car Information: 2020 Toyota Corolla
License
This repository is for educational purposes and does not have any specific licensing attached.

## Contacts
For any questions or inquiries, please contact:

Email: peter.rono@student.moringaschool.com
GitHub: kprono
