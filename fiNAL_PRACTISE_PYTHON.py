# class Solution:
#     def threesum(self,nums,target):
#         nums.sort()
#         res = len(nums[:-3])
#
#         for i in range(len(nums)-2):
#             s = i+1
#             e = len(nums)-1
#
#             while s<e:
#                 sumhere = nums[i]+nums[s]+nums[e]
#                 if abs(sumhere-target) < (res- target):
#                     res = sumhere
#
#                 if sumhere < target:
#                     s+=1
#                 else:
#                     e=-1
#             return res
# nums = [1,2,3,4,54,56,7]
# s = Solution()
# print(s.threesum(nums,7))