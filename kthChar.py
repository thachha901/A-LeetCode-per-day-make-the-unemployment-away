# Alice and Bob are playing a game. Initially, Alice has a string word = "a".

# You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.

# Now Bob will ask Alice to perform all operations in sequence:

# If operations[i] == 0, append a copy of word to itself.
# If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
# Return the value of the kth character in word after performing all the operations.

# Note that the character 'z' can be changed to 'a' in the second type of operation.

class Solution(object):
    def kthCharacter(self, k, operations):
        m = len(operations)
        # 1) Tính len[i] = 2^i
        length = [1] * (m + 1)
        for i in range(1, m+1):
            length[i] = length[i-1] * 2

        # 2) Lùi ngược từ bước m về 1
        shift = 0
        for i in range(m, 0, -1):
            half = length[i-1]
            if k > half:
                k -= half
                if operations[i-1] == 1:
                    shift = (shift + 1) % 26

        # 3) Bước gốc: "a" → áp shift
        return chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
