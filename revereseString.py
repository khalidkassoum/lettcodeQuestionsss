def reverseString(str):
        str_list = list(str)
        i=0
        j=len(str)-1
        while i<=j:
            temp=str_list[i]
            str_list[i]=str_list[j]
            str_list[j]=temp
            i+=1
            j-=1


        print(str_list)




if __name__ == "__main__":
        reverseString("abcdef")