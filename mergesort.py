def merge_sort(arr):
# this function use for divide the array into two parts and then merge them in sorted order
  if len(arr)<=1:
    return arr
  
  start=0
  end=len(arr)-1 
  mid=start+(end-start)//2

  left=arr[start:mid+1]
  right=arr[mid+1:end+1]

  leftsort=merge_sort(left)
  rightsort=merge_sort(right)

  return merge(leftsort,rightsort)

   

def merge(left, right):
# this function use for merge the two sorted array into one sorted array
   result=[]
   i=0
   j=0

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
      
          
arr=[2,4,5,7,1,6,8,11,9,10,18,12,15,14,13,17,16,19,20]
new=merge_sort(arr)
print(new)
