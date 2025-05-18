
arr=[10,8,7,12,13,20,25]

search_element=int(input("Enter number:"))

arr.sort() #[7,8,10,12,13,20,25]

low=0

high=len(arr)-1

is_present=False

while low<=high:

    mid=(high+low)//2

    if arr[mid]==search_element:

        is_present=True

        break

    elif arr[mid]<search_element:

        low=mid+1

    else:

        high=mid=-1

print(is_present)

