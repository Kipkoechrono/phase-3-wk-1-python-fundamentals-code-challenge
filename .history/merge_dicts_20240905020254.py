def merge_dicts(dict1, dict2):
    #new dictionary that will hold the merged results
    merged_dict = dict1.copy()
    
    # Iterate through the second dictionary
    for key, value in dict2.items():
        # sum the values,If the key exists in the merged dictionary
        if key in merged_dict:
            merged_dict[key] += value
        else:
            #add the key-value pair to the merged dictionary
            merged_dict[key] = value
    
    return merged_dict

#dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# Merging dictionaries
result = merge_dicts(dict1, dict2)
print(result) 
