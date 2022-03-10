n=int(input("enter a no:"))
i=2
flag=0
while i<n:
    if n%i==0:
      flag=1
      break
    i+=1

if flag==1:
    print("non-prime no")
else:
    print("prime no")