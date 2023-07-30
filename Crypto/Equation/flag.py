def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

a = 30188147721117215781129100297502653147720244598096
b = 21570432690338300962113223428601821765217196091704

gcd, x, y = extended_euclidean_algorithm(a, b)
if gcd == 1:
    x %= b  # 取模确保 x 的值在 [0, b-1] 范围内
    print("x =", x)
    print("y =", y)
else:
    print("无解")
