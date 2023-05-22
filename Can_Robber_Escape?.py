n=int(input())
s=0
lst=list(map(int,input().split()))
for i in lst:
    if i>=n:
        print("NO")
        s=1
        break
if s!=1:
    print("YES")