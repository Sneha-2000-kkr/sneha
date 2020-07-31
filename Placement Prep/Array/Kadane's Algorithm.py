n=int(input())
l=list(map(int,input().split()[:n]))
u=[]
for i in range(len(l)):
    k=0
    for j in range(i,len(l)):
        k=k+l[j]
        u.append(k)
print(max(u))
