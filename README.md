 Python Array Manipulation Demo
This project demonstrates basic array operations using Python's built-in array module. It covers creating arrays, searching for elements, modifying values, and applying conditional logic to update array contents.
📌 Features
- ✅ Create an array of integers
- 🔍 Search for a specific value and return its index
- ✏️ Modify an element at a given index
- 🔄 Conditionally update values greater than a threshold
📦 Requirements
- Python 3.x (no external libraries required)
🚀 Getting Started
Clone the Repository
git clone https://github.com/your-username/python-array-demo.git
cd python-array-demo


Run the Script
python array_demo.py


🧠 Code Overview
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
arr[2] = 35
print("Modified array:", arr)

# Increase all values greater than 25 by 5
for i in range(len(arr)):
    if arr[i] > 25:
        arr[i] += 5

print("Conditionally modified array:", arr)


🧪 Sample Output
Original array: array('i', [10, 20, 30, 40, 50])
Element 30 found at index 2
Modified array: array('i', [10, 20, 35, 40, 50])
Conditionally modified array: array('i', [10, 20, 40, 45, 55])

