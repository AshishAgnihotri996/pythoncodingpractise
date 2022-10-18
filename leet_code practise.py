#sums equals k
#
# class Solution:
#     def sumequalsk(self,arr):
#         count = 0
#         sumdict = {0:1}
#         s = 0
#         k =7
#         sum =0
#
#         for i in arr:
#             s+=i
#             if s-k in sumdict:
#                 count+=sumdict[s-k]
#             if s in sumdict:
#                 sumdict[s]+=1
#             else:
#                 sumdict[s]=1
#         return count
#
#
# arr = [3,4,7,2,-3,1,4,2]
#
# s = Solution()
# ans = s.sumequalsk(arr)
# print(ans)
