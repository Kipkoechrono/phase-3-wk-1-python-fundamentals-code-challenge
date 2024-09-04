def count_vowels(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Define vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize counter for vowels
    count = 0
    
    # Iterate through each character
    for char in text:
        #  increment the count if a vowel
        if char in vowels:
            count += 1
            
    # Return the total count of vowels
    return count

# Test function with the given example input
result = count_vowels("Hello, World!")
print(result)  # Output should be 3
