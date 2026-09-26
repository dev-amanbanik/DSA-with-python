#Sum of first N numbers
from time import time
#functions
#solution 1
'''
def sumofN(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
    '''
#solution 2
def sumofN(n):
    return int(n*(n+1))//2

#program

start_time=time()
X=sumofN(100000000)
end_time=time()
duration_time=end_time - start_time

print(X)
print(duration_time)


