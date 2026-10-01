def binarysearch(a,target):
  l=0
  r=len(a)-1
  m=l+r//2
  while l<r:
    if a[m]==target:
      print(f'{target} is found at index{m}')
      return
    elif a[m]<target:
      l=m
      m=l+r//2
    else:
      r=m
      m=l+r//2
a=[1,2,3,4,5]
print(binarysearch(a,5))
