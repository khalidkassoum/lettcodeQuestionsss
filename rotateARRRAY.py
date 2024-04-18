
def rotatearr(arr,k):

  length=len(arr)
  for i in arr:
      if ((i+k)>(length-1)):
          j=(i+k-length+1)

      