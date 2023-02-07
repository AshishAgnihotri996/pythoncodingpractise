# sums equals k
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

# Atoi
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


# 3sumclosetesst
#
# class Solution:
#     def sumset(self,arr,target):
#         arr = arr.sort()
#         res = sum(arr)
#
#         for i in range(len(arr)-2):
#             s = i+1
#             e = len(arr)-1
#
#             while s< e:
#                 sumwhere = arr[s]+arr[e]+arr[i]
#                 if abs(sumwhere -target) < abs(res - target):
#                     res = sumwhere
#                 if sumwhere < res:
#                     s+=1
#                 else:
#                     e -=1
#         return res
#
# arr = [1,32,4,5,6,7,10]
#
# s = Solution()
# ans = s.sumset(arr,15)
# print(ans)


# BINAry tree creation and insertion


# class Node:
#     def __del__(self, val):
#         self.data = val
#         self.right = None
#         self.left = None
#
# def insert(root, node):
#     if (root is None):
#         root = node
#         return
#
#     if (root.data < node.data):
#         if (root.right is None):
#             root.right = node
#         else:
#             insert(root.right, node)
#
#     else:
#         if (root.left is None):
#             root.left = node
#             return
#         else:
#             insert(root.left, node)
#
#
# def preoder(node):
#     if(node is not None):
#         print(node.data)
#         preoder(node.left)
#         preoder(node.right)
#
#
# tree = Node(5)
#
# insert(tree, Node(4))
# insert(tree, Node(7))
# insert(tree, Node(6))
# insert(tree, Node(8))
#
# preoder(tree)

#
# class Node:
#     def __int__(self,value):
#         self.left = None
#         self.right = None
#         self.data = value
#
#
# def insert(root,node):
#     if (root is None):
#         root= node
#         return
#     if root.data > node.data:
#         if (root.right is None):
#             root.right = Node
#         else:
#             insert(root.right,node)
#     else:
#         if (root.left is None):
#             root.left = Node
#         else:
#             insert(root.left, node)
#
# def serach(node,key):
#     print('current node is',node.data)
#
#     if node is None:
#         print('no data found')
#         return
#     else:
#         if node.data == key:
#             print('node found')
#             return node
#
#     if node.data < key:
#         return serach(node.right,key)
#     return serach(node.left,key)
#
# t = Node(5)

#asymertric tree
# class Solution:
#     def is_mirror(self,t1,t2):
#         if (t1 is None and t2 is None):
#             return True
#         if t1 is None and t2 is None:
#             return False
#         return (t1.val == t2.val) and self.is_mirror(t1.right,t2.left) and self.is_mirror(t1.left,t2.right)
#
#     def isSymmetric(self,root:TreeNode)->bool:
#         return self.is_mirror(root,root)


#longest common subsequence


#20 random pick with weight
# import random
#
#
# class Solution:
#     def __init__(self,w):
#         self.prefix_sum = []
#         prefix_sum = 0
#         for weight in w:
#             self.prefix_sum += weight
#             self.prefix_sum.append(prefix_sum)
#         self.total_sum = prefix_sum
#
#
#     def pickIndex(self)->int:
#         random_num = self.total_sum *random.random()
#         low = 0
#         high = len(self.prefix_sum)
#         while low < high:
#             mid = (low+high)//2
#             if random_num > self.prefix_sum:
#                 l = mid+1
#             else:
#                 high = mid
#         return low

#maximum sum circular subaarray


# class Solution:
#
#     def maxsubarrayCircular(self,A):
#         k = self.kadane(A)
#         cs = 0
#         for i in range(len(A)):
#             cs+=A[i]
#             A[i] = -A[i]
#         cs = cs + self.kadane(A)
#
#         if cs > k and cs!= 0 :
#             return cs
#         else:
#             return k
#
#
#     def kadane(self,nums):
#         cursum,maxsum = nums[0],nums[0]
#
#         for n in nums[1:]:
#             cursum = max(n,cursum+n)
#             maxsum = max(cursum,maxsum)
#         return maxsum

#count square submartrices wih all ones leletcode
#
# class Solution:
#     def countSquare(self,matrix):
#         n = len(matrix)
#         m = len(matrix[0])
#
#         ansMatrix = [[0]*(m+n) for _ in range(n+1)]
#         count= 0
#
#         for row in range(1,n+1):
#             for col in range(1,m+1):
#                 if matrix[row-1][col-1]==1
#                     ansMatrix[row][col] = 1+min(ansMatrix[row][col-1],ansMatrix[row-1][col],ansMatrix[row][col])
#                     count+=ansMatrix[row][col]
#                     print(count)
#
#         return count


# intersection of two array II
# class Solution:
#     def intersectionArraY(self,l1,l2):
#         l1.sort()
#         l2.sort()
#         result = []
#         i = 0
#         j = 0
#
#         while i < len(l1) and j < len(l2):
#             if l1[i] == l2[j]:
#                 result.append(l1[i])
#                 i +=1
#                 j +=1
#             elif l1[i] < l2[j]:
#                 i+=1
#             else:
#                 j+=1
#         return result


# merged k sorted list

# Python3 program to merge k sorted
# arrays of size n each

# A Linked List node
# class Node:
#
# 	def __init__(self):
#
# 		self.data = 0
# 		self.next = None
#
# # Function to print nodes in a
# # given linked list
# def printList(node):
#
# 	while (node != None):
# 		print(node.data, end=' ')
# 		node = node.next

# Takes two lists sorted in increasing order,
# and merge their nodes together to make one
# big sorted list. Below function takes
# O(Log n) extra space for recursive calls,
# but it can be easily modified to work with
# same time and O(1) extra space
# def SortedMerge(a, b):
#
# 	result = None
#
# 	# Base cases
# 	if (a == None):
# 		return(b)
# 	elif (b == None):
# 		return(a)
#
# 	# Pick either a or b, and recur
# 	if (a.data <= b.data):
# 		result = a
# 		result.next = SortedMerge(a.next, b)
# 	else:
# 		result = b
# 		result.next = SortedMerge(a, b.next)
#
# 	return result
#
# # The main function that takes an array of lists
# # arr[0..last] and generates the sorted output
# def mergeKLists(arr, last):
#
# 	# Repeat until only one list is left
# 	while (last != 0):
# 		i = 0
# 		j = last
#
# 		# (i, j) forms a pair
# 		while (i < j):
#
# 			# Merge List i with List j and store
# 			# merged list in List i
# 			arr[i] = SortedMerge(arr[i], arr[j])
#
# 			# Consider next pair
# 			i += 1
# 			j -= 1
#
# 			# If all pairs are merged, update last
# 			if (i >= j):
# 				last = j
#
# 	return arr[0]
#
# # Utility function to create a new node.
# def newNode(data):
#
# 	temp = Node()
# 	temp.data = data
# 	temp.next = None
# 	return temp
#
#
# # Driver code
# if __name__ == '__main__':
#
# 	# Number of linked lists
# 	k = 3
#
# 	# Number of elements in each list
# 	n = 4
#
# 	# An array of pointers storing the
# 	# head nodes of the linked lists
# 	arr = [0 for i in range(k)]
#
# 	arr[0] = newNode(1)
# 	arr[0].next = newNode(3)
# 	arr[0].next.next = newNode(5)
# 	arr[0].next.next.next = newNode(7)
#
# 	arr[1] = newNode(2)
# 	arr[1].next = newNode(4)
# 	arr[1].next.next = newNode(6)
# 	arr[1].next.next.next = newNode(8)
#
# 	arr[2] = newNode(0)
# 	arr[2].next = newNode(9)
# 	arr[2].next.next = newNode(10)
# 	arr[2].next.next.next = newNode(11)
#
# 	# Merge all lists
# 	head = mergeKLists(arr, k - 1)
#
# 	printList(head)


# Search in Rotated Sorted Array python

# class Solution:
#     def search(self,arr,target):
#         if arr is None:
#             return -1
#         low = 0
#         high = len(arr)-1
#         mid = (low+high)//2
# 
#         while low < high:
#             if target ==arr[mid]:
#                 return mid
# 
#             if arr[low]<=arr[mid]:
#                 if arr[low] <= target <= arr[mid]:
#                     high = mid-1
#                 else:
#                     low = mid+1
#             else:
#                 if arr[mid] <= target < arr[high]:
#                     low = mid+1
#                 else:
#                     high = mid-1
#             return -1

#the maze
# class Solution:
#     def dfs(self,maze,start,destination):
#         n = len(maze)
#         m = len(maze[0])
#         visited = set()
#         def dfs(x,y):
#             if (x,y) not in visited:
#                 visited.add((x,y))
#             else:
#                 return False
#             for i,j in (0,-1),(0,1),(-1,0),(1,0):
#                 new_X ,new_Y = x,y
#                 while 0 <= new_X+i < m and 0 <= new_Y+j <n and maze[new_X+i][new_Y+j]!= 1:
#                     new_X+=i
#                     new_Y+=j
#                 if dfs(new_X,new_Y):
#                     return True
#             return False
#         return (dfs(start))







