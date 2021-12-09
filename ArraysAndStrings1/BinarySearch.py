import math
import threading


class BinarySearch:
    '''Helper Functions'''

    def getLastIndex(self, A):
        right = len(A) - 1
        while A[right] == -1 and right > 0:
            right -= 1
        return right

    def swap(self, A, index1, index2):
        temp = A[index1]
        A[index1] = A[index2]
        A[index2] = temp

    '''---------'''

    # Implement Binary Search
    '''Use mid = start + (end - start)/2 instead of mid = start + end/2 '''

    def binarySearch(self, A, target):
        start, end = 0, len(A) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if A[mid] > target:
                end = mid - 1
            elif A[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1

    # Question
    '''1. (Level: Easy) Given a sorted array that can contain duplicates, find the first occurrence of a target
     element T.
    For example, if A = [2,3,4,4,5,6] and T = 4, return index 2.'''

    def firstOccurence(self, A, target):
        start, end = 0, len(A) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if A[mid] > target or (A[mid] == target and mid > 0 and A[mid - 1] == target):
                end = mid - 1
            elif A[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1

    # Question
    '''You are given a sorted array A and a target T. Return the index where T would be placed if inserted in order.
    For example, 
    A = [1,2,4,5,6,8] and T = 3, return index 2
    A = [1,2,4,5,6,8] and T = 0, return index 0
    A = [1,2,4,5,6,8] and T = 4, return index 3.
    '''
    # Approach
    '''If duplicate element exists. Insert it at end of the same elements'''

    def insertPosition(self, A, target):
        start, end = 0, len(A) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if A[mid] <= target:
                if mid == len(A) - 1:
                    return mid
                start = mid + 1
            else:
                if mid == 0 or A[mid - 1] <= target:
                    return mid
                end = mid - 1

    # Question
    '''1. (Level: Easy) Given a sorted array A and a target T, find the target.
    If the target is not in the array, find the number closest to the target.
    For example, if A = [2,3,5,8,9,11] and T = 7, return index of 8, i.e. return 3.'''

    # Approach
    '''Record and move on'''

    def closestToTarget(self, A, target):
        start, end = 0, len(A) - 1
        result = None
        while (start <= end):
            mid = start + (end - start) // 2
            result = self.record(A, mid, result, target)
            if A[mid] > target:
                end = mid - 1
            elif A[mid] < target:
                start = mid + 1
            else:
                return mid
        return result

    def record(self, A, mid, result, target):
        if result is None or abs(target - A[mid]) < abs(target - A[result]):
            return mid

        return result

    # Question
    '''1. (Level: Easy) Given a sorted array A that has been rotated in a cycle, 
    find the smallest element of the array in O(log(n)) time. 
    For example,
    [1,2,4,5,7,8] rotated by 3 gives us A = [5,7,8,1,2,4] and the smallest number is 1.
    [1,2,4,5,7,8] rotated by 1 gives us A = [8,1,2,4,5,7] and the smallest number is 1.
    '''

    def minCyclicalSorted(self, A):
        start, end, right = 0, len(A) - 1, A[-1]
        while (start <= end):
            mid = start + (end - start) // 2
            if A[mid] <= right and (mid == 0 or A[mid - 1] > A[mid]):
                return mid
            else:
                if A[mid] < right:
                    end = mid - 1
                else:
                    start = mid + 1
        return - 1

    def searchOfUnknown(self, A, target):
        length = self.findLength(A)
        start, end = 0, length - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if A[mid] > target :
                end = mid - 1
            elif A[mid] < target :
                start = mid + 1
            else :
                return mid
        return - 1


    def findLength(self, A):
        start = 2
        end = 0
        while (True):
            try:
                mid = A[start]
                start *= 2
            except Exception:
                end = start
                start /= 2
                break
        print(start,end)
        while start <= end:
            mid = start + (end - start) // 2
            try :
                temp = A[mid]
            except Exception :
                end = mid - 1
                continue

            try :
                temp = A[mid + 1]
            except Exception:
                return mid

            start = mid + 1

    def squareRoot(self, number):
        start,end = 0,number
        while(start<=end):
            mid = (start+end)//2
            if mid*mid > number:
                end = mid - 1
            elif mid*mid < number:
                if (mid+1)**2 > number :
                    return mid
                start = mid + 1
            else :
                return mid

    #Question
    '''Search for a Peak: A peak element in array A is an A[i] where its adjacent elements are less than A[i].
    So, A[i - 1] < A[i] and A[i + 1] < A[i].

    Assume there are no duplicates. Also, assume that A[-1] and A[length] are negative infinity (-∞).
    So A[0] can be a peak if A[1] < A[0].'''

    #Approach
    ''''''

    def findPeak(self, A):
        start,end = 0,len(A)-1

        while(start<= end) :
            mid = start + (end-start)//2
            prev = A[mid-1] if mid > 0 else float('-inf')
            next = A[mid+1] if mid < len(A)-1 else float('-inf')

            if prev > A[mid] and next>A[mid] :
                start = mid + 1
            elif prev > A[mid] and next<A[mid] :
                end = mid - 1
            elif prev < A[mid] and next>A[mid] :
                start = mid + 1
            else :
                return mid
        return -1
print(BinarySearch().findPeak([1,2,3,1,5,7,8]))

