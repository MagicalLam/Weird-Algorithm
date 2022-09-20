'''
Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three 
and adds one.
'''
def solve(n):
    s = ""
    while n != 1:
        s += str(n) + " "
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1
    s += "1 " + "\n"
    return s
