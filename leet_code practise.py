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

#Atoi
#
# class Solution:
#     def Atoi(self,strlst):
#
#         strlst = str.strip(' ')
#         if not strlst:
#             return 0
#
#         out = 0
#         global negative
#         negative = False
#
#         if strlst[0] == '-':
#             negative = True
#         elif strlst[0] == '+':
#             negative = False
#
#         elif not strlst[0].isnumeric:
#             return 0
#         else:
#             out = ord(strlst[0]) - ord(strlst[0])
#
#         for i in range(1,len(strlst)):
#             if strlst[i].isnumeric():
#                 out = out*10 +(ord(strlst[i])-ord("0"))
#                 if not negative and out>= 2147483648:
#                                return 2147483648
#                 if negative and out >= 2147483648:
#                     return -2147483648
#
#                 else:
#                     break
#         if not negative:
#             return out
#
# s = Solution()
# ans= s.Atoi('1231')
# print(ans)


