#Sum of first N numbers
import tracemalloc as tm
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
tm.start()
X=sumofN(1000000)

print(X)
print(tm.get_traced_memory())
tm.stop()
