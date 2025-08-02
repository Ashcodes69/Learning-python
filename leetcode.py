# Example 1:
# Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# Output: 1
# Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
# Example 2:
# Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
# Output: -1
# Explanation: It can be shown that it is impossible to make both the baskets equal.

basket1 = [2, 3, 4, 1]
basket2 = [3, 2, 5, 1]
dic = {}
for i in basket1:
    dic[i] = basket1.count(i)
for i in basket2:
    dic[i] = dic.get(i, 0) + 1

extra1 = []
extra2 = []
for i, count in dic.items():
    if count % 2 != 0:
        print(-1)
        break
    else:
        count1 = basket1.count(i)
        count2 = basket2.count(i)
        target = (count1 + count2) // 2
        if count1 > target:
            for j in range(count1 - target):
                extra1.append(i)
        elif count2 > target:
            for j in range(count2 - target):
                extra2.append(i)


extra1.sort()
extra2.sort(reverse=True)

minVal = min(basket1 + basket2)
cost = 0
for a, b in zip(extra1, extra2):
    cost += min(2 * minVal, min(a, b))

print(cost)
