import sys
def SumofNnumber(n):
  sum=0
  for i in range(1,n+1):
    sum=sum+i
  return sum
print(SumofNnumber(5))

print(sys.getsizeof(SumofNnumber))