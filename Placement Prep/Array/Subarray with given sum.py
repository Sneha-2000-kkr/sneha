p=int(input("Enter no of cases"))
while(p!=0):
  n=int(input("Enter size of list"))
  s=int(input("Enter sum"))
  l=list(map(int,input("Enter the elements").split()[:n]))
  d = []
  for i in range(len(l)+1):
    k=0
    for j in range(i,len(l)):
             if(k<s):
                 k=k+l[j]
                 #print(k)
             elif(k==s):

                 k = (i+1, j)
                 d.append(k)
                 print(d[0])
                 break
  p=p-1
