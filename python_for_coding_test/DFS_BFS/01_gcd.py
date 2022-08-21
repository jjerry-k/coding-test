def gcd(a, b):
    tmp_a, tmp_b = b, a % b
    if tmp_b == 0:
        return b
    else:
        return gcd(tmp_a, tmp_b)

print(gcd(192, 162))