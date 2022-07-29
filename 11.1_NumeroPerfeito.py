n = int(input())
for i in range(n):
    divisores = []
    soma = 0
    x = int(input())
    if 1 <= x  and x <= 10**8:
        for divisor in range(1, x):
            if x%divisor == 0:
                divisores.append(divisor)
        for div in divisores:
            soma += div
    if soma == x:
        print(x," é perfeito!")
    else:
        print(x," não é perfeito!")
