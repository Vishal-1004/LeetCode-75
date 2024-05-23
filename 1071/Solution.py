'''
Intuition
    We will be using the concept of GCD to find the answer over here. Using the length of both the strings we will find their GCD and then check string to length [:GCD] divides both the strings or not.

Approach
1. Find the length of both the strings
2. Create a function to find the GCD of two number using Euclidie's Method
3. Find the GCD for the calculated length and store it in num.
4. Check if the the count of str2[:num] in str1 and multiplied with num is equal to l1 (length of str1) and also check that whether count of str2[:num] in str2 multiplied with num is equal to l2 or not.
5. If yes then return str2[:num].
6. Else return "".

Complexity
    Time complexity: O(logmin(a,b))
    Space complexity: O(1)
'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)

        num = gcd(l1,l2)
        if str1.count(str2[:num])*num == l1 and str2.count(str2[:num])*num == l2:
            return str2[:num]

        return ""