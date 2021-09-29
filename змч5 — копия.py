a = int(input())
b = int(input())
for i in range(10):
    while a < b:
       if 3 == str(a).count(str(i)):
           print(a)
    a += 1
