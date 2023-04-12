#bubble sort
num=list(map(int, input().split()))
print(num)
for i in range(1,len(num)):
    for n in range(0,len(num)-i):
        if num[n]>num[n+1]:
            var=num[n]
            num[n]=num[n+1]
            num[n+1]=var

print(num)