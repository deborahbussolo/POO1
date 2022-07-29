Q = int(input())
V = [int(x) for x in input().split()][:Q]

cont = V.count(0)

if cont > Q/2:
    print("S")
else:
    print("N")