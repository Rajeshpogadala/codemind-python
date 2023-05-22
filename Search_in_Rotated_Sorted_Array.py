n=int(input())
lst=list(map(int,input().split()))
tar=int(input())
s=0
for i in range(len(lst)):
    if lst[i]==tar:
        print(i)
        s=1
        break
if s!=1:
    print("-1")