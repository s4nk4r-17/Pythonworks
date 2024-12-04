# Write a Python program to remove duplicates from a list.

arr=[1,2,4,5,3,2,4,5,3]

duplicate_elements=[]

arr.sort() #[1,2,2,3,3,4,4,5,5]

for element in arr:

        if element not in duplicate_elements:

            duplicate_elements.append(element)

print("List with duplicates removed:",duplicate_elements)

