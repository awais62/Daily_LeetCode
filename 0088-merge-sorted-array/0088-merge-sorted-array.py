class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1  # Last index of nums1
        i, j = m - 1, n - 1  # Pointers for nums1 and nums2

        # Merge from the back to front
        while j >= 0:  # Only need to check nums2, nums1 is already in place
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1
