class ReverseTraversal:
    '''Helper Functions'''
    def getLastIndex(self, A):
        right = len(A) - 1
        while A[right] == -1 and right > 0 :
            right -= 1
        return right

    def swap(self,A, index1,index2):
        temp = A[index1]
        A[index1] = A[index2]
        A[index2] = temp

    '''---------'''

    def cloneEvenNos(self,A):
        rp = len(A) - 1
        lp = self.getLastIndex(A)

        for i in range(lp, -1 , -1):
            if A[i] % 2 == 0:
                A[rp] = A[i]
                rp -= 1
            A[rp] = A[i]
            rp -= 1

        return A

    def reverseWords(self, sentence):
        result = ""
        if sentence is None :
            return None

        rp = len(sentence) -1
        word = ""
        while rp >= 0 :
            if sentence[rp] == " ":
                if len(result) == 0 :
                    result += word
                else :
                    result += " " + word
                word = ""
            else :
                word = sentence[rp] + word
            rp -= 1

        result += " " + word

        return result

    def reverseWordsOptimize(self, sentence):
        result = ""
        if sentence is None:
            return None

        rp = len(sentence) - 1
        start = len(sentence)
        while rp >= 0:
            if sentence[rp] == " ":
                if len(result) != 0:
                    result += " "
                result = result + sentence[rp+1:start]
                start = rp
            rp -= 1

        result += " " + sentence[0:start]
        return result

    def reverseArray(self, A):
        if A is None :
            return None

        lp,rp = 0,len(A)-1
        while(lp<= rp) :
            temp = A[lp]
            A[lp] = A[rp]
            A[rp] = temp
            lp += 1
            rp -= 1
        return A

    def twoSumSorted(self, A, target):
        if A is None :
            return -1
        lp,rp = 0,len(A)-1

        while(lp<= rp) :
            s = A[lp] + A[rp]
            if s < target :
                rp -= 1
            elif s > target :
                lp += 1
            else :
                return(lp,rp)
        return -1

    def squareOfArray(self, A):
        lp,rp = 0,len(A)-1
        result = [None]*(len(A))
        resultP = len(A)-1
        while(lp <= rp ) :
            if A[lp]**2 > A[rp]**2 :
                result[resultP] = A[lp]**2
                lp += 1
            else :
                result[resultP] = A[rp]**2
                rp -= 1
            resultP -= 1
        return result

    #Question
    '''Given an array of integers, find the continuous subarray, which when sorted, results in
     the entire array being sorted. For example: A = [0,2,3,1,8,6,9], 
     result is the subarray [2,3,1,8,6]'''

    #Approach
    '''Look for value dips from start and end from the array. Then expand this subarray according to its
    min and max'''

    def contiguousSubArray(self,A):
        lp,rp= 0,len(A)-1

        while(lp< len(A)-1):
            if A[lp] >A[lp+1] :
                break
            lp += 1

        while(rp>lp) :
            if A[rp] < A[rp-1] :
                break
            rp -= 1

        minimum = min(A[lp:rp+1])
        maximum = max(A[lp:rp+1])

        while (lp >= 0 and A[lp-1] > minimum):
            lp -= 1
        while (rp<len(A) and A[rp+1] < maximum):
            rp += 1

        return A[lp:rp+1]

    '''PARTITIONING ARRAYS '''

    def moveZeroesToStart(self,A):
        boundary = 0
        for i in range(len(A)) :
            if A[i] == 0 :
                temp = A[boundary]
                A[boundary] = A[i]
                A[i] = temp
                boundary += 1
        return A

    def moveZeroesToEnd(self,A):
        boundary = len(A)-1
        for i in range(len(A)-1,-1,-1) :
            if A[i] == 0 :
                temp = A[boundary]
                A[boundary] = A[i]
                A[i] = temp
                boundary -= 1
        return A

    #Question
    '''Dutch National Flag Problem: Given an array of integers A and a pivot, rearrange A in the following order:
    [Elements less than pivot, elements equal to pivot, elements greater than pivot]

    For example, if A = [5,2,4,4,6,4,4,3] and pivot = 4 -> result = [3,2,4,4,4,4,6,5]'''

    #Approach
    '''Use the partition array technique , from both sides'''

    def dutchNationalFlagProblem(self,A, pivot):
        lb,hb,i = 0,len(A)-1,0

        while(i <=hb) :
            if A[i] > pivot :
                self.swap(A,hb,i)
                hb -= 1
            else :
                self.swap(A,lb,i)
                lb += 1
                i += 1
        return A

    '''Given an array with n marbles colored Red, White or Blue, sort them so that marbles of the same color are 
    adjacent, with the colors in the order Red, White and Blue.
    Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).
    For example, if A = [1,0,1,2,1,0,1,2], Output = [0,0,1,1,1,1,2,2].'''

    def redWhiteBlue(self,A):
        lb,hb,i=0,len(A)-1,0

        while(i<=hb) :
            if A[i] == 0 :
                self.swap(A,i,lb)
                lb += 1
                i += 1
            elif A[i] == 2 :
                self.swap(A,i,hb)
                hb -= 1
            elif A[i] == 1 :
                i += 1
            else :
                raise Exception('Invalid Color')
        return A

    '''Given an array of integers that can be both +ve and -ve, find the contiguous subarraywith the largest sum.
    For example:  [1,2,-1,2,-3,2,-5]  -> first 4 elements have the largest sum. Return (0,3) 
    '''

    def kadane(self,A):
        maxSoFar = float('-inf')
        maximum = float('-inf')
        for i in range(len(A)) :
            maxSoFar = max(maxSoFar + A[i],A[i])
            maximum = max(maximum,maxSoFar)
        return maximum

    def kadaneSubArray(self,A):
        maxSoFar = float('-inf')
        maximum = float('-inf')
        fs,fe = 0,0
        start,end = 0,0
        for i in range(len(A)) :
            if maxSoFar + A[i] > A[i] :
                maxSoFar = maxSoFar + A[i]
                end += 1
            else :
                maxSoFar = A[i]
                start = i
                end = i

            if maximum < maxSoFar :
                maximum = maxSoFar
                fs,fe = start,end
        return A[fs:fe+1]

    #Question
    '''Given an array of positive integers, find the contiguous subarray that sums to a given number X.

    For example, input = [1,2,3,5,2] and X=8, Result = [3,5]'''

    #Approach
    '''Use sliding window'''

    def subArrayTarget(self,A,target):
        start,end = 0,0
        s =  A[0]
        while start<len(A) :
            print(start,end)
            if start > end :
                end = start
                s = A[start]

            if s < target :
                if (end == len(A)-1) :
                    break
                end += 1
                s += A[end]
            elif s > target :
                s -= A[start]
                start += 1
            else :
                return A[start:end+1]
        return -1

    #Question
    '''(Level: Medium) Given a String, find the longest substring with unique characters.

    For example: "whatwhywhere" --> "atwhy"'''

    def longestUniqueSubstr(self, S):
        start,end = 0,0
        d = {S[0]:0}
        fs,fe,maximum = 0,0,1
        while(end < len(S)-1):
            end += 1

            if S[end] in d and d[S[end]]>=start :
                start = d[S[end]]+1
            d[S[end]] = end

            if maximum < (end-start+1):
                maximum = end-start+1
                fs = start
                fe = end
        return (fs,fe)




print(ReverseTraversal().longestUniqueSubstr("whatwhywhere"))

