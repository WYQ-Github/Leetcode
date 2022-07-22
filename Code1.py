'''leetcode算法入门'''
'''删除排序数组中的重复项'''
# class Solution:
#     def removeDuplicates(self, nums):
#         j = 0
#         b = []
#         for i in range(0,len(nums)):
#             if i != len(nums)-1:
#                 j = i + 1
#                 if nums[i] != nums[j]:
#                     b.append(nums[i])
#             else:
#                 j = i
#                 b.append(nums[i])
#         return  b

'''买卖股票的最佳时机'''
# 执行用时：44 ms, 在所有 Python3 提交中击败了54.31%的用户
# 内存消耗：15.7 MB, 在所有 Python3 提交中击败了80.05%的用户
# class Solution:
#     def maxProfit(self, prices) -> int:
#         a = []
#         for i in range(0,len(prices)-1):
#             if prices[i+1]-prices[i]>0:
#                 a.append(prices[i+1]-prices[i])
#         return sum(a)

'''旋转数组'''
#执行用时：48 ms, 在所有 Python3 提交中击败了63.32%的用户
#内存消耗：21 MB, 在所有 Python3 提交中击败了77.04%的用户
# class Solution:
#     def rotate(self, nums, k) -> None:
#         if len(nums) >= k:
#             nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
#         else:
#             k = k % len(nums)
#             nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

'''存在重复元素'''
# 执行用时：60 ms, 在所有 Python3 提交中击败了64.66%的用户
# 内存消耗：25.2 MB, 在所有 Python3 提交中击败了66.51%的用户
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(set(nums)) == len(nums):
#             return False
#         else:
#             return True

'''只出现一次的数字'''
#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
#注意审题
# class Solution:
#     def singleNumber(self, nums) -> int:
#         return sum(set(nums)) * 2 - sum(nums)

'''两个数组的交集 II'''
# 执行用时：56 ms, 在所有 Python3 提交中击败了17.63%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了79.74%的用户
# a = [1,2]
# b = [1,1]
# c = []
# if len(a) >= len(b):
#     pass  
# else:
#     c = a
#     a = b
#     b = c 
# d = []
# for i in b:
#     if i in a:
#         d.append(i)
#         a.remove(i)
# print(d)


# list1 = ['a','b','c','d']
# list2 = ['a','b','e']

# list1_not_in_list2 = [i for i in list1 if i not in list2]
# print(list1_not_in_list2)

# list2_not_in_lis1 = [i for i in list2 if i not in list1]

'''加一'''
#执行用时：24 ms, 在所有 Python 提交中击败了8.47%的用户
#内存消耗：12.9 MB, 在所有 Python 提交中击败了83.84%的用户

# def plusOne(digits):
#     for i in range(len(digits)-1, -1, -1):
#         if digits[i] != 9:
#             digits[i] += 1
#             return digits
#         else:
#             digits[i] = 0
#     digits.insert(0,1)
#     return digits



# plusOne(digits=[9,8,9])


#b = list(map(int,str(a)))数字变成列表，列表变成数字
#a[-1]=a[-1]+1
#b = int("".join(map(str,a)))数字变成列表，列表变成数字


'''移动数字0'''
# def moveZeroes(nums):
#     b = []
#     for i in nums:
#         if i != 0:
#             b.append(i)
#     for j in range(0,len(nums)-len(b)):
#         b.append(0)
    
#     return b

# print(moveZeroes(nums=[1,0,0,3,4,5]))
'''两数之和'''
# a = [2,3,0,4,8]
# b = []
# for i in range(len(a)-1,-1,-1):#5,4,3,2
#     for j in a[0:i]:
#         if a[i] + j == 3:
#             x = a.index(j)
#             b.append(x)
#             b.append(i)
            
# print(b)
    # for j in a.remove(i):
    #     if i+j == 7:
    #         print(i,j)

# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]

# 判断行
#board[0].remove('.')
#print(board[8])

# for i in range(0,9):
#     DotNum = board[i].count('.')
#     if len(set(board[i])) != len(board[i]) - DotNum + 1:
#         print('行存在重复元素')

# for j in range(0,9):
#     board_col = [x[j] for x in board] 对列的处理
#     DotNum = board_col[j].count('.')
#     if len(set(board_col[j])) != len(board_col[j]) - DotNum + 1:
#         print('列存在重复元素')

# for i in range(0,9,3):
#     for j in range(0,9,3):
#         m = []
#         for k in range(i, i+3):
#                 for z in range(j, j+3):
#                     m.append(board[k][z])
        
# class Solution:
#     def isValidSudoku(self, board) -> bool:
#         res = True
#         # 判断行
#         for i in range(len(board)):
#             dotCount = board[i].count('.')
#             rightCount = len(board[i]) - dotCount + 1
#             judgeCount = len(set(board[i]))
#             if rightCount != judgeCount:
#                 res = False
#         # 判断列
#         for i in range(len(board[0])):
#             l = []
#             for j in range(len(board)):
#                 l.append(board[j][i])
#             dotCount = l.count('.')
#             rightCount = len(board[0]) - dotCount + 1
#             judgeCount = len(set(l))
#             if rightCount != judgeCount:
#                 res = False
#         # 判断3*3宫内是否重复
#         for i in range(0, len(board), 3):
#             for j in range(0, len(board[0]), 3):
#                 m = []
#                 for k in range(i, i+3):
#                     for z in range(j, j+3):
#                         m.append(board[k][z])
#                 dotCount = m.count('.')
#                 rightCount = len(m) - dotCount + 1
#                 judgeCount = len(set(m))
#                 if rightCount != judgeCount:
#                     res = False
#         return res
        

# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# new_matrix = []
# for i in range(len(matrix)-1,-1,-1):
#     new_matrix.append(matrix[i])
# new_matrix_2 = []
# for i in range(len(matrix)):
#     new_matrix_2.append([x[i] for x in new_matrix])
# print(new_matrix_2)
# for i, vec in enumerate(zip(*matrix)):
#     matrix[i] = list(vec)
#     matrix[i].reverse()

# s = ["h","e","l","l","o","5"]
#s = [1,2,3,4,5]
# s.reverse()
# print(s)
# left = 0
# right = len(s)-1
# while right >= left:
#     s[left], s[right] = s[right], s[left]
#     left = left + 1
#     right = right - 1
# print(s)

#print(int(1234 / 1000)%10)
# def reverse(x):
#     if  x < 0 - (2 ** 31) or x > (2 ** 31) - 1:
#         return 0
#     else:
#         sign = False
#         if x < 0:
#             sign = True
#         x = abs(x)
#         num = 0
#         i = len(str(x))-1
#         #for i in range(len(str(x))-1,-1,-1):
#         for j in range(0,len(str(x))):
#             num = num + ((int(x / (10**j)) % 10) * (10**i))
#             i = i - 1  
#         if sign:
#             num = 0 - num
#             if num < 0 - (2 ** 31):
#                 return 0
#         if num > (2 ** 31) - 1:
#             return 0
        
#         return num


#     #     x = abs(x)
#     #     num = 0
#     #     i = len(str(x))-1
#     #     #for i in range(len(str(x))-1,-1,-1):
#     #     for j in range(0,len(str(x))):
#     #         num = num + ((int(x / (10**j)) % 10) * (10**i))
#     #         i = i - 1
#     #     return 0 - num

# print(reverse(1534236469))

# def reverse(x):
#     sign = False
#     if x < 0:
#         sign = True
#     x = abs(x)
#     r = 0
#     while x != 0:
#         r *= 10
#         tmp = x % 10
#         x //= 10
#         r += tmp
#     if sign:
#         r = 0 - r
#         if r < 0 - 2 ** 31:
#             return 0
#     if r > 2 ** 31 - 1:
#         return 0
#     return r
# print(reverse(1534236469))

from audioop import reverse


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        return False
import re

c = "p0"
c = (''.join(re.findall(r'[A-Za-z0-9]', c))).lower()
print(c)
b = ''
for i in range(len(c)-1,-1,-1):
    b = b + (c[i]) 
print(b)






        




