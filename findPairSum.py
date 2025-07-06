# You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

# Add a positive integer to an element of a given index in the array nums2.
# Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
# Implement the FindSumPairs class:

# FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
# void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
# int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

from collections import Counter

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index, val):
        old_val = self.nums2[index]
        new_val = old_val + val

        # Cập nhật counter
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.counter2[new_val] += 1

        # Cập nhật mảng
        self.nums2[index] = new_val

    def count(self, tot):
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.counter2.get(complement, 0)
        return result