#use a single list to impliment three stacks
# import math
# class Solution:
#     def countbit(self,n):
#         ans = [0] *(n+1)
#         for i in range(1,n+1):
#             halfpos = math.floor(i/2)
#             if i%2==1:
#                 ans[i] = ans[halfpos]+1
#             else:
#                 ans[i] = ans[halfpos]
#         return ans


#contains duplicate

# def conduipli(arr):
#    seen = set()
#    for num in arr:
#        if num not in seen:
#            seen.add(num)
#        else:
#            return  False
#    return seen
#
# arr = [1,1,2,3,4,5,5,5,6,7,8]
# conduipli(arr)
