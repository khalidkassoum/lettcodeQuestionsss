def happyNumber(num):

    count=0
    while num>=0:
        module=num%10
        num/=10
        count+=pow(module,2)
        if count==1:
            print(count)
            return True

        num=count
        count=0
        print("lloop")
    return False

if __name__ == "__main__":
 happyNumber(555)
