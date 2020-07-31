n=int(input())
l=list(map(int,input().split()[:n]))
for i in range(n):
    if(l[i]+1!=l[i+1]):
        print(i+2)
        break
