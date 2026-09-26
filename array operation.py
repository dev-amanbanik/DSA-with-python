# Array operations with different methods

# 1. First occurrence of an element
def first_occurrence(arr,key):
  for i in range(len(arr)):
   if arr[i]==key: 
    print("element found at index: ",i)
    return i
  else:
    print("element not found")

# 2. Last occurrence of an element  
def position (arr,key):
 for i in range(len(arr)):
  if arr[i]==key:
   print("The value is ",i+1," position in the list.")
   break
  else:
   print("not found")

# 3. Last occurrence of an element
def last_occurrence(arr,key):
 last=-1
 for i in range(len(arr)):
  if arr[i]==key:
   last=i
 print("last occurrence at index",last)

# 4. All occurrence of an element
def all_occurrence(arr,key):
 for i in range(len(arr)):
  if arr[i]==key:
   print(i)

# 5. Count occurrence of an element
def count_occurrence(arr,key):
 count=0
 for i in range(len(arr)):
  if arr[i]==key:
   count +=1
 print(key,"found in" ,count,"in the given list")

# 6. Remove all occurrence of an element
def remove_occurrence(arr,key):
 while key in arr:
  arr.remove(key)
 print(arr)

# Array 
arr=[10,20,30,40,50,30,60,40,30,69,90,30]
# Search element
key=30
# functions calling
count_occurrence(arr,key)

