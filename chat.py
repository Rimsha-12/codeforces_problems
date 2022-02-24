'''s=input()
c=0
for i in s:
    if c==0 and i=='h':
        c+=1
    elif c==1 and i=='e':
        c+=1
    elif c==2 and i=='l':
        c+=1
    elif c==3 and i=='l':
        c+=1
    elif c==4 and i=='o':
        c+=1
if c==5:
    print("YES")
else:
    print("NO")'''
n=int(input())
for i in range(n):
    x=int(input())
    