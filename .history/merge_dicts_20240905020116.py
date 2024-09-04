def merge_dicts(dict1, dict2):
    # Create a new dictionary that will hold the merged results
    merged_dict = dict1.copy()
    
    # Iterate through the second dictionary
    for key, value in dict2.items():
        # If the key exists in the merged dictionary, sum the values
        if key in merged_dict:
            merged_dict[key] += value
        else:
            # Otherwise, add the key-value pair to the merged dictionary
            merged_dict[key] = value
    
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# Merging the dictionaries
result = merge_dicts(dict1, dict2)
print(result)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
