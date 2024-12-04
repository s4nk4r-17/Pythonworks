
def findRanges(nums):

    if not nums:

        return []
    
    result=[]

    start=nums[0]

    for i in range(1,len(nums)):

        if nums[i]!=nums[i-1]+1:

            result.append(f"{start}-->{i-1}")

            start=nums[i]

    


nums1 = [0, 1, 2, 4, 5, 7]
nums2 = [1, 3, 5, 6, 7, 10]

print(findRanges(nums1))
print(findRanges(nums2))