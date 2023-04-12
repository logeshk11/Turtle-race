# You are given a string
# S  Determine if it is possible to find two non-empty strings
# A and  B which satisfy the following conditions:
# A+B=S, where + denotes string concatenation
# B is a substring of  A


s=input("Enter a string : ")
point=0
def check_substring(a, b):
    st=0
    for x in range(len(b) ,len(a)+1):
        c=a[st:x]
        if c==b:
            return True
        st+=1

if len(s) % 2==0:
    st=int(len(s)/2)
else:
    st=int(len(s)/2)+1

for  let in range(st ,len(s)):
    a=s[0:let]
    b=s[let:len(s)]
    ans=check_substring(a,b)
    if ans is True:
        print("YES")
        print(f"a is {a}, b is {b}")
        point=1
        break

if(point==0):
    print("NO")
