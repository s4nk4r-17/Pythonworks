# *   *   *   *   *
# *   *   *   *
# *   *   *
# *   *
# *

# for row in range(5,0,-1):

#     for col in range(1,row+1):
        
#         print("*",end="\t")

#     print()

#another method

# for row in range(1,6):

#     for col in range(5,row-1,-1):#range(5,0,-1),(5,1,-1)
        
#         print("*",end="\t")

#     print()

#half pyramid
# *
# *       *
# *       *       *
# *       *       *       *
# *       *       *       *       *
# *       *       *       *       *       *

# for row in range(1,7):
#     for col in range(1,row+1):
#         print("*",end="\t")
#     print()

#inverted Half pyramid
# *       *       *       *       *       *
# *       *       *       *       *
# *       *       *       *
# *       *       *
# *       *
# *

# for row in range(6,0,-1):
#     for col in range(1,row+1):
#         print("*",end="\t")
#     print()

#full pyramid
#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

for row in range(1,7):
    for sp in range(1,7-row):
        print(" ",end="")
    for col in range(1,row+1):
        print("* ", end="")    
    
    print()


#inverted full pyramid

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

for row in range(6,0,-1):
    for sp in range(1,7-row):
        print(" ",end="")
    for col in range(1,row+1):
        print("* ", end="")    
    
    print()    




