'''
Intuition
    Here we will find the max element of the array and then for every element we will add the extra candies which we have and check if it is greater than max element of the array or not if yes then add "True" to the answer array else add "False" to the array.

Complexity
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_ele = max(candies)

        ansArr = []
        for i in candies:
            if i + extraCandies >= max_ele:
                ansArr.append(True)
            else:
                ansArr.append(False)

        return ansArr