# * * * * * 
#   *     * 
#     *   * 
#       * * 
#         * 

n = 5

for i in range(1, n+1):
    for j in range(2, i+1):
        print(" ", end=" ")
    for k in range(n, i-1, -1):
        if k == n or k == i or i == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()