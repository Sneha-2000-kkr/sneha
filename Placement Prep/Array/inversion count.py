n=int(input())
#m=int(input())
l=list(map(int,input().split()[:n]))
#p=list(map(int,input().split()[:m]))
c=0
for x in range(len(l)):
    for y in range(x+1,len(l)):
        if(l[x]>l[y]):
            l[x],l[y]=l[y],l[x]
            c=c+1
print(c)
