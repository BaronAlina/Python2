a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a + ((a % d != c) * (d-c)), b, d):
    print(i, end=' ')
