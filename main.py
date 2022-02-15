a = 1
b = 0
n = int(input())
for i in range (0, n + 1):
    a = a + b
    a, b = b, a
    print (a)