a = int(input())
b = int(input())
c = int(input())
d = int(input())
e=int(input())
summ=0
for x in range(1001):
    if x==e:
        summ+=0
    else:
        if((a*x**3+b*x**2+c*x+d)/(x-e))==0:
            summ+=1
print(summ)
