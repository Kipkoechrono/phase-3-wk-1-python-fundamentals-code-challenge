def sort_by_age(people):
    # Sort the list of tuples by the second element (age) in each tuple
    return sorted(people, key=lambda person: person[1])

#tuples containing names and ages
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sorting the list per ages

sorted_people = sort_by_age(people)
print(sorted_people) 
