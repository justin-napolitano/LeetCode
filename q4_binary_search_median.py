#principlas of the search tree...  
#reduce the size of the search with each iteration by dividing in two 
#how to accomplish this? 
import random
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        lengthA = 0 
        lengthB = 0
        lengthA = len(nums1)
        lengthB = len(nums2)

        A = nums1
        B = nums2
        
        if lengthA > lengthB:
            A, B, lengthA, lengthB = B, A, lengthB, lengthA
        if lengthA == 0:
            raise ValueError

        imin, imax, half_len = 0, lengthA, (lengthB + lengthA + 1) / 2

        while imin < imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < lengthB and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (lengthB + lengthA) % 2 == 1:
                    return max_of_left

                if i == lengthB: min_of_right = B[j]
                elif j == lengthA: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

def main():
    arr1 = []
    arr1.extend(range(-100, 101))
    arr2 = range(101, 201)
    answer = 0
    answer = Solution.findMedianSortedArrays(arr1, arr2)
    print(answer)


if __name__ == "__main__": 
    main()
        
