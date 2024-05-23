'''
Intuition
    This is a very simple two pointer based question. Here we will intiate two pointers w1 and w2 pointing towards index 0 of the words word1 and word2 respectively. Then we will alternatively store the characters pointed by w1 and w2 into a answer string till either one of them gets over. Finally we will add the characters left in any of the words.

Approach
1. Initiate w1=w2=0.
2. Initiate ansStr=""
3. Run a while loop till w1 < len(word1) and w2 < len(word2)
4. Withing the while loop perform two steps:
    ansStr += word1[w1] + word2[w2]
    w1 += 1 and w2 += 1
5. Finally check that if w1 < len(word1) then add word1[w1:] at the end of ansStr.
6. Else if w2 < len(word2) then add word2[1:] at the end of ansStr.
7.  Finally return ansStr.

Complexity
    Time complexity: O(n)
    Space complexity: O(1)
'''


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1 = 0
        w2 = 0
        ansStr = ""

        while w1 < len(word1) and w2 < len(word2):
            ansStr += word1[w1] + word2[w2]
            w1 += 1
            w2 += 1

        if w1 < len(word1):
            ansStr += word1[w1:]
        elif w2 < len(word2):
            ansStr += word2[w2:]

        return ansStr