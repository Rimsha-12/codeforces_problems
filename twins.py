n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
l=0
h=len(a)
m=(l+h)//2
print(m+a)