def fun(n):
    h=[]
    for i in range(len(n)):
        if n[i]=="(" or n[i]=="{" or n[i]=="[":
            h.append(n[i])
        else:
            if h and((h[-1]=="(" and n[i]==')')or
              (h[-1]=="{" and n[i]=='}') or
              (h[-1]=="[" and n[i]=="]")):
                h.pop() 
            else:
                return False       
    return not h
    


s = "{([])}"
print(fun(s))


