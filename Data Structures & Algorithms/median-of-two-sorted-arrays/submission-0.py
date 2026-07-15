class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = len(nums1), len(nums2)
        i = j = 0
        m1 = m2 = 0

        for k in range((a+b)//2+1):
            m2 = m1
            if i<a and j<b:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j+=1
                else:
                    m1 = nums1[i]
                    i+=1
            elif i<a:
                m1 = nums1[i]
                i+=1
            else:
                m1 = nums2[j]
                j+=1
        if (a+b)%2 == 1:
            return m1
        return (m1+m2)/2