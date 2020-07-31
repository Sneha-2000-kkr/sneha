p=[]
n=int(input())
l=list(map(int,input().split()[:n]))
while(len(l)!=0):
  mn = min(l)
  p.append(mn)
  l.remove(mn)
  #print(len(l))
print(p)
