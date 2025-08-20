import array

# Create an array of integers
arr = array.array('i', [10, 20, 30, 40, 50])
print("Original array:", arr)
# Search for the index of an element
search_value = 30
if search_value in arr:
    index = arr.index(search_value)
    print(f"Element {search_value} found at index {index}")
else:
    print(f"Element {search_value} not found")
    # Modify the element at a specific index
arr[2] = 35  # Changing value at index 2 from 30 to 35
print("Modified array:", arr)
# Increase all values greater than 25 by 5
for i in range(len(arr)):
    if arr[i] > 25:
        arr[i] += 5

print("Conditionally modified array:", arr)