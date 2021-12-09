import math
import threading


class Recursion:
    def findFibo(self, n, map):
        if n == 1 or n == 2 :
            return 1

        if n in map :
            return map[n]

        map[n] = self.findFibo(n-1,map) + self.findFibo(n-2,map)
        return map[n]

    def fibonacci(self, n):
        m = {}
        return self.findFibo(n, m)

    def powerFunction(self, x, n ):
        if x == 0 :
            if n < 0 :
                raise ValueError
            else :
                return 0

        positivePower = self.positivePowerFunction(abs(x),abs(n))
        result = positivePower
        if x < 0 and n%2 != 0 :
            result =  -1 * positivePower

        if n < 0 :
            result =  1/positivePower

        return result

    def positivePowerFunction(self, x, n ):
        if n == 1 :
            return x

        if n == 0 :
            return 1

        halfPower = self.positivePowerFunction(x,n//2)
        if n%2 ==0 :
            res = halfPower**2
        else :
            res = halfPower**2 * x
        return res


print(Recursion().powerFunction(5,-2))