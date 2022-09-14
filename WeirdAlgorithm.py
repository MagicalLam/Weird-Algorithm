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
