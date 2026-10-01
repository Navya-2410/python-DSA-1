a=[20,10,30,50,60] 
def bubblesort(a):
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      if a[i]>a[j]:
        a[i],a[j]=a[j],a[i]
  print(a)
bubblesort(a)