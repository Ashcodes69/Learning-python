"""
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""

fruits = [1, 2, 3, 2, 2]

l = 0
max_fruits = 0
dictt = {}

# Right pointer of the sliding window
for r in range(len(fruits)):
    # Add the current fruit to the basket (dictionary) and update its count
    dictt[fruits[r]] = dictt.get(fruits[r], 0) + 1
    # If we have more than 2 types of fruits, shrink the window from the left
    while len(dictt) >= 3:
        # Reduce the count of the leftmost fruit
        dictt[fruits[l]] -= 1
        # If the count becomes 0, remove it completely from the dictionary
        if dictt.get(fruits[l], 0) == 0:
            del dictt[fruits[l]]
        # Move the left pointer to the right (shrink the window)
        l += 1
    # Update the max fruits collected so far (valid window size)
    max_fruits = max(max_fruits, (r - l) + 1)
print(max_fruits)
