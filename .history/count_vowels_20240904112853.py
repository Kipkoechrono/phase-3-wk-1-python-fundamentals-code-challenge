def count_vowels(text):
    # Convert the text to lowercase to ignore case sensitivity
    text = text.lower()
    
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate through each character in the text
    for char in text:
        # If the character is a vowel, increment the count
        if char in vowels:
            count += 1
            
    # Return the total count of vowels
    return count

result = count_vowels("Hello, World!")
print(result)  # Output: 3
