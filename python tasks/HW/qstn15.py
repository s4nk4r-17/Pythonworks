# Write a Python program to split a list into two halves.


arr = [2, 5, 3, 6, 77, 9, 3]

midpoint = len(arr) // 2

first_half = arr[:midpoint]
second_half = arr[midpoint:]

print("First half:", first_half)

print("Second half:", second_half)