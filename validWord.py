# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.

# Return true if word is valid, otherwise, return false.

# Notes:

# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowel = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for char in word:
            if not char.isalnum():
                return False
            if char.isalpha():
                if char in vowel:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant