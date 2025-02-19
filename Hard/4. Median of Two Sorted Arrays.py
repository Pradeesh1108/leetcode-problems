class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = 0
        j = 0
        n1len = len(nums1)
        n2len = len(nums2)
        nums3 = []
        while i < n1len and j < n2len:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1

        while i < n1len:
            nums3.append(nums1[i])
            i+=1
        while j < n2len:
            nums3.append(nums2[j])
            j+=1

        low = 0
        high = len(nums3) -1
        if len(nums3) % 2 != 0:
            mid = (low+high) // 2
            res = nums3[mid]
        else:
            mid = (low+high) //2
            res = (nums3[mid] + nums3[mid+1]) / 2
        return res

