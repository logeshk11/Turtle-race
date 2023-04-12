num=[5, 34, 54, 4, 23, 44, 33]
n=5
num.sort()
mid=int(len(num)/2)
for n in range(1, len(num)):
    if num[mid]== n:
        print("Found")
        print(n)
        break
    elif num[mid]<n:
        mid=int((mid+len(num))/2)
    else:
        mid=int(mid/2)
