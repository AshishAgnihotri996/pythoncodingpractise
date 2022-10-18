# def calc(n):
#     if n>0:
#         calc(n - 1)
#         k = n**2
#         print(k)
#         calc(n - 1)
# calc(4)

#sum of n natural number

# def sumofnat(n):
#     if n==0:
#         return 0
#     return sumofnat(n-1)+n
#
# num = int(input('enter the number'))
# print(sumofnat(num))

#factorail

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return fact(n-1)*n
#
# n = int(input('enter the number to compute the factorial'))
# print(fact(n))

#linear search
# def linearsearch(arr,target):
#     index = 0
#     while index < len(arr):
#         if arr[index] == target:
#             print(index,arr[index])
#         index+=1
#     return -1
#
# arr = [1,2,3,4,5,6,7,8,9,9,78,6,65,5,54]
# target = 54
# linearsearch(arr,target)


#binary search


# def binseaech(arr,key):
#     l = 0
#     r = len(arr)-1
#
#     i=0
#     while l <= r:
#         mid = (l + r) // 2
#         if key==arr[i]:
#             return i-+

#         elif key < arr[i]:
#             r = mid-1
#         elif key > arr[i]:
#             l = mid+1
#     print('not found')
#
#
# arr =[1,2,3,4,5,6,7,8]
# key = 1
# binseaech(arr,key)

#merge k linkes list

#backtracking series


#three sum
# class Solution:
#     def threesum(self,arr):
#         res=[]
#         arr.sort()
#
#         length = len(arr)
#         l = 0
#         r = length-1
#         for i in range(length-2):
#             if l<0 and arr[i]==arr[i-1]:
#                 continue
#             l = i+1
#             r = length-1
#
#             while l< r:
#                 total = arr[i]+arr[l]+arr[r]
#                 if total < 0:
#                     l = l+1
#                 elif total > 0:
#                     r  = r-1
#
#                 else:
#                     res.append(total)
#                     while l<r and arr[l]==arr[l+1]:
#                         l = l+1
#
#                     while l<r and arr[r]==arr[r-1]:
#                         r = r-1
#
#                     l = l+1
#                     r = r-1
#         return res
#
#
# s = Solution()
# ans = s.threesum([-1,0,1,2,-1,-4])
# print(ans)


#maximyhm substring problem
# class Solution:
#     def maxsubstring(self,arr):
#         map ={}
#         n = len(arr)
#
#         if n==0:
#             return
#         max_len= 0
#         start = 0
#
#         for i in range(len(arr)):
#             if arr[i] in map and start <= map[arr[i]]:
#                 start = map[arr[i]]+1
#             else:
#                 max_len = max(max_len,i-start+1)
#             map[arr[i]] = i
#         return (max_len)
# arr = 'ashish'
# s = Solution()
# ans = s.maxsubstring(arr)
# print(ans)
import collections
import heapq
from collections import defaultdict

class Solution:
    def networkdelay(self,time:list[list[int]],N,k):
        g = collections.defaultdict(list)

        for u,v,cost in time:
            g[u].append(cost,v)

        min_heap = [(0,k)]
        visited = set()
        i = 0
        distace= {i:(float('inf') for i in range(1,N+1))}

        distace[k] = 0

        while min_heap:
            cur_distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if len(visited)==N:
                return cur_distance

            for direct_distance, v in g[u]:
                if cur_distance + direct_distance < distace[v] and v not in distace:
                    distace[v] = cur_distance + direct_distance
                    heapq.heappush(min_heap,(direct_distance[v],v))
        return -1
