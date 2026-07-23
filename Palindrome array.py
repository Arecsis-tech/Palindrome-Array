s=int(input())
n=list(map(int,input().split()))
m=n[::-1]
if n==m:
    print("YES")
else:
    print("NO")
