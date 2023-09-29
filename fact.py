def fact(n):
    prod = 1

    for i in range(n+1):
        prod*=i
    return prod
n = 5
print(fact(n))
