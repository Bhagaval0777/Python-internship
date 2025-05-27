def palindrome(x):
    y=str(x)
    i=0
    j=len(y)-1
    while i<j:
        if y[i]!=y[j]:
            return False
        else:
            i+=1
            j-=1
    return True
        

def palindrome1(x):
    y= reversed(str(x))
    if x==y:
        return True
    return False


print(palindrome1(121))