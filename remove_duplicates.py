def removeDuplicates(arr):
  length=len(arr)
  new_arr=[arr[0]]
  for i in range (1,length):
      if arr[i]!=arr[i-1]:
         new_arr.append(arr[i])
  print(new_arr)


if __name__ == "__main__":
    removeDuplicates([2,3,3,4,5,5,6])