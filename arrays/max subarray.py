a=[-1,5,3,2,1,0,7,6]
def slidingwindow(a,key):
  sum=0
  for i in range(0,key):
    sum=sum+a[i]
  max=0
  for i in range(key,len(a)):
    sum+=a[i]
    sum-=a[i-key]
    if sum>max:
      max=sum
  print(max)
a=slidingwindow(a,3)
