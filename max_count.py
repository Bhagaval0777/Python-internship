nums = [1,2,2,3,1,4,1,2,4,3,1,5,2]
h ={}
for i in nums:
    if i in h:
        h[i]+=1 
    else:
        h[i]=1
        
print(h)
a = max(h,key=h.get)
print(a)
