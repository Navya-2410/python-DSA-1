n=int(input())
a=list(map(int,input().split(' ')))[:n]
el=int(input())
def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      ar=apnd(ar,i)
  print(ar)
def apnd(a,el):
  ar=[0 for _ in range(len(a)+1)]
  for i in range(len(a)):
    ar[i]=a[i]
  ar[-1]=el
  return ar
linearsearch(a,el)