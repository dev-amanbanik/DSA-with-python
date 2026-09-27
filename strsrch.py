# 1. using slicing
def all_occurrence_using_slicing(text,key):
  found=False
  count=0
  for i in range(len(text)):
      if text[i:i+len(key)]==key:
          count+=1
          print("found at index",i) 
          found=True
        # break
  print("number of appearance of the",key,"is",count)
  if not found:
    print("not found")

# 2. using nested loop
def all_occurrence_using_nested_loop(text,key):
  found=False
  count=0
  for i in range(len(text)):
    for j in range(len(key)):
      if text[i+j] != key[j]:
        break
    else:
      count+=1
      print("found at index",i)
      found=True
  print("number of appearance of the",key,"is",count)
  if not found:
    print("not found")
    

text="aman is a good chess player in his school , other player cant beat him but one player is very good and he is the best player in his school"
key="player"
all_occurrence_using_slicing(text,key)
