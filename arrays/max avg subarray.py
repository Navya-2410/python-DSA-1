a=[-1,5,3,2,1,0,7,6]
def maxavgsubarra(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  maxavg=sum/k
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    avg=sum/k
    if maxavg<avg:
      maxavg=avg
  print(maxavg)
a=maxavgsubarra(a,2)
