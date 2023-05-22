n=int(input())
s=0
a=n
for i in range(1,n):
    if(n%i==0):
        s=s+i
if s==a:
    print("True")
else:
    print("False")