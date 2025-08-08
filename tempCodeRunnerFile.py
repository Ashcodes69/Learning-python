"""
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
"""

# fruits = [4, 2, 5]
# baskets = [3, 5, 4]

# for i in range(len(fruits)):
#     for j in range(len(baskets)):
#         if baskets[j] >= fruits[i]:
#             baskets[j] = -1
#             fruits[i] = 0
#             break
# count = fruits.count(i > 0)
# # for f in fruits:
# #     if f > 0:
# #         count += 1
# print(count)


def numOfUnplacedFruits(fruits, baskets):
    i = j = 0
    while i < len(fruits) and j < len(baskets):
        if baskets[j] >= fruits[i]:
            i += 1
            j += 1
        else:
            j += 1
    return len(fruits) - i


fruits = [3, 6, 1]
baskets = [6, 4, 7]
print(numOfUnplacedFruits(fruits, baskets))
