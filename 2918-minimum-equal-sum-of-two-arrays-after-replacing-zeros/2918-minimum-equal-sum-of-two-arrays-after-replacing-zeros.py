class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_nums1 = 0
        sum_nums2 = 0

        count_0_nums1 = 0
        count_0_nums2 = 0

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        for i in range(len_nums1):
            sum_nums1 += nums1[i]
            if nums1[i] == 0:
                count_0_nums1 += 1

        for i in range(len_nums2):
            sum_nums2 += nums2[i]
            if nums2[i] == 0:
                count_0_nums2 += 1

        if count_0_nums1 == 0 and count_0_nums2 == 0:
            if sum_nums1 == sum_nums2:
                return sum_nums1
            return -1

        if count_0_nums2 == 0:
            if sum_nums1 + count_0_nums1 * 1 > sum_nums2:
                return -1

        if count_0_nums1 == 0:
            if sum_nums2 + count_0_nums2 * 1 > sum_nums1:
                return -1

        if sum_nums1 + count_0_nums1 * 1 >= sum_nums2 + count_0_nums2 * 1:
            return sum_nums1 + count_0_nums1 * 1
        else:
            return sum_nums2 + count_0_nums2 * 1




