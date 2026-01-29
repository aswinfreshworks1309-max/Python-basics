# *********
# *       *
# *       *
# *       *
# *       *
# *       *
# *       *
# *       *
# *********





# a = 9

# for i in range(1,a+1):
#     if i == 1 or i == a:
#         print('*'*a)
#     else:
#         print('*' + ' '*(a-2) + '*')



#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *


n = 5
for i in range(1,n+1):
    if i == 1 or i == n:
        print(' '*(n-i) + '*')
    else:
        print(' '*(n-i) + '*' + ' '*(2*i-3) + '*')
    
