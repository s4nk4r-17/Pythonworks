
def longestCommonPrefix(strs):
    
    if not strs:

        return ""
    

    prefix=strs[0]


    for s in strs:

        while not s.startswith(prefix):

            prefix=prefix[:-1]

            if not prefix:

                return ""
            
    return prefix



strs1=["flower","flow","flight"]

print(longestCommonPrefix(strs1))

strs2 = ["dog", "racecar", "car"]

print(longestCommonPrefix(strs2)) 