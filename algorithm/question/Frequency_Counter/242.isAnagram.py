def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)): return False
        result1 = {}
        result2 = {}
        for char in s:
            if (char in result1):
                result1[char] += 1
            else:
                result1[char] = 1

        for char in t:
            if (char in result2):
                result2[char] += 1
            else:
                result2[char] = 1

        if (result1 == result2): return True
        return False

print(isAnagram('anagrams', 'nagarama')); # False
print(isAnagram('anagrams', 'nagarams')); # True