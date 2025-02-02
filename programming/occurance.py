def find_first_last_occurrences(lst):
    occurrences = {}

    for i in range(len(lst)):
        element = lst[i]
        if element not in occurrences:
            occurrences[element] = [i, i]
        else:
            occurrences[element][1] = i

    return occurrences

# Example usage
my_list = [1, 3, 3, 2, 1, 4, 3, 2, 1]
occurrences = find_first_last_occurrences(my_list)

# Print first and last occurrences
for element, (first, last) in occurrences.items():
    print(f"Element {element} - First occurrence: {first}, Last occurrence: {last}")

# Output:
# Element 1 - First occurrence: 0, Last occurrence: 8
# Element 3 - First occurrence: 1, Last occurrence: 6
# Element 2 - First occurrence: 3, Last occurrence: 7
# Element 4 - First occurrence: 5, Last occurrence: 5
