n=int(input())
k=int(input())
b=1
c=1
d=1
a=n-k
for i in range(1, n+1):
    b=b*i
for i in range(1, k+1):
    c=c*i
for i in range(1, a+1):
    d=d*i
print(int(b/(c*d)))
