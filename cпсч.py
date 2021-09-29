n=int(input())
b=0
for i in range(2, n+1):
    print(i-1, end='')
    b+=(i-1)*i
    print('*', end='')
    print(i, end='')
    if(i==n):
        print('=', end='')
    else:
        print('+', end='')
print(b)

