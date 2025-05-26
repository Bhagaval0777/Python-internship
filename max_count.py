from collections import Counter
nums = [1,2,2,3,1,4,1,2,4,3,1,5,2]
h = Counter(nums)
max_val = max(h.values())

ans = [i for i in h if h[i] == max_val]
print(ans)

