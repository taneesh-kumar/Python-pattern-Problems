# Method -  1

#     * 
#    * *  
#   * * * 
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

n = 5

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(end = " ")
    for j in range(1, i+1):
        print("*", end = " ")
    print()

for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print(end = " ")
    for j in range(1, i+1):
        print("*", end = " ")
    print()

print()
# Method - 2

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 

for i in range(1, n+1):
    print(" "*(n-i), "* "*i)
for j in range(n-1, 0, -1):
    print(" "*(n-j), "* "*j)
   