def calculate_factorial(n):
    # Initialize the result to 1 (factorial of 0 is 1)
    result = 1
    
    # Calculate the factorial by multiplying the result by each integer up to n
    for i in range(1, n + 1):
        result *=  i
        
    return result
#  calculate_factorial function
print(calculate_factorial(5)) 
