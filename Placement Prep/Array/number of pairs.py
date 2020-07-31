n=int(input())
m=int(input())
l=list(map(int,input().split()[:n]))
p=list(map(int,input().split()[:m]))
c=0
for x in range(len(l)):
    for y in range(len(p)):
        if(pow(x,y)>pow(y,x)):
            c=c+1
print(c)
