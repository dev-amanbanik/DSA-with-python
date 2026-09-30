def merge_sort(arr):
# this function use for divide the array into two parts and then merge them in sorted order
  if len(arr)<=1:
    return arr
   
  mid=len(arr)//2
  leftsort=merge_sort(arr[:mid])
  rightsort=merge_sort(arr[mid:])

  return merge(leftsort,rightsort)

def merge(left, right):
# this function use for merge the two sorted array into one sorted array
   result=[]
   i=j=0
   while i<len(left) and j<len(right):
      
      if left[i]<right[j]:
         result.append(left[i])
         i+=1
      else:
         result.append(right[j])
         j+=1
   result.extend(left[i:])
   result.extend(right[j:])
   return result
         
arr=[2,4,5,7,6,8,11,9,10,18,12,15,14,13,17,16,19,1,20]
print(merge_sort(arr))

