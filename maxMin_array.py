from collections import deque
def maxMinInArray(arr):
  length=len(arr)
  max=arr[0]
  min=arr[0]
  for i in range(length):
   if arr[i]>max:
       max=arr[i]
   if arr[i]<min:
       min=arr[i]
  print(max,min)
  # myrr=[1,2,3,4]
  # myrr.pop()
  # hm = {}  for hash map
  # hm
  # sample_dict = {'Name': 'Aditya', 'Age': 22, 'City': 'Las-Vegas'}
  # sample_dict.__delitem__()
  # llist=deque()
  # llist.n

if __name__ == "__main__":
    maxMinInArray([2,4,-1,-5,8])
