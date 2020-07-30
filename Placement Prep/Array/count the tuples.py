n=int(input())
l=list(map(int,input().split()[:n]))
k=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        s=0
        s=l[i]+l[j]
        k.append(s)
#print(k)
c=0
for i in range(len(l)):
    for j in range(len(k)):
        if(l[i]==k[j]):
            c=c+1
        else:
            c=-1
print(c)
