#String search using different methods
# 1. Using loop
def using_loop(text,key):
  for i in range(len(text)):
    if text[i:i+len(key)]==key:
      print("found at index",i)
      break
  else:
    print("not found")

# 2. Using find() method
def find_function(text,key):
  index = text.find(key)
  if index != -1:
      print("found at index", index)
  else:
      print("not found")

# 3. Using index() method with try-except
def try_catch(text,key):
 try:
    index = text.index(key)
    print("found at index", index)
 except ValueError:
    print("not found")


text="aman is a good boy"
key="boy"  


try_catch(text,key)
# find_function(text,key)