from sortedcontainers import SortedDict

# Initialize a SortedDict with a few countries and their populations in millions
population_dict = SortedDict({"USA": 331, "China": 1439, "India": 1380, "Russia": 146})

# Print the left insertion point for 'India', which should correspond to its index
print(
    "Left insertion point for India:", population_dict.bisect_left("India")
)  # Output should be 1 because 'India' comes after 'China'

# Simulating the rotation of items, ensuring the order doesn't matter for SortedDict
# Convert SortedDict to a list of items, perform the rotation directly without ensuring order, and convert back
items = list(population_dict.items())  # Convert to list of tuples
rotated_items = items[1:] + items[:1]  # Perform the rotation
rotated_dict = dict(rotated_items)  # Convert back to the dict

print(
    "Country at the start after one rotation:", rotated_dict["Russia"]
)  # This line is expected to output the smallest item in the rotated dict
