n=int(input())
l=[]
for i in range(0,n+1):
    l.append(i)
while(set(l)!=4):
    n+=1
    print(n)
