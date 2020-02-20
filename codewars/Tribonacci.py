tribb = [1, 1, 1]


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[:n]
    for index in range(int(n-3)):
        number = signature[index] + signature[index+1] + signature[index+2]
        signature.append(number)
        index += 1
    return signature


print(tribonacci(tribb, 10))
