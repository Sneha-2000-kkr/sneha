n=int(input())
l=list(map(int,input().split()))
p=[]
if(len(l)%2==0):
    while (len(l) != 0):
        mx = max(l)
        p.append(mx)
        mn = min(l)
        p.append(mn)
        l.remove(max(l))
        l.remove(min(l))
        #print(len(l))
    print(p)

else:
    while(len(l)!=1):
        mx = max(l)
        p.append(mx)
        mn = min(l)
        p.append(mn)
        l.remove(max(l))
        l.remove(min(l))
        #print(len(l))
    p.append(l[0])
    print(p)



