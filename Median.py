# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.




class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Đảm bảo nums1 là mảng nhỏ hơn
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y +1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY -1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return float(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return float(max(maxLeftX, maxLeftY))

            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

