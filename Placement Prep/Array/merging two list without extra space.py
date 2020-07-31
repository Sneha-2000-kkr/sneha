n=int(input())
m=int(input())
l=list(map(int,input().split()[:n]))
o=list(map(int,input().split()[:m]))
for i in l:
    o.append(i)
print(sorted(o))
