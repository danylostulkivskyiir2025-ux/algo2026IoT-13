import unittest
#тут до квадратів пілносимо
def sorted_squares(nums):
    result = []
    for i in range (len(nums)):
        result.append(nums[i]*nums[i])
    return sort1(result)
    
def sort1(arr):
    if len(arr) <= 1:
        return arr
    p = arr[0]
    l = []
    r = []                            
    
    for x in arr[1:]:
        if x < p:
            l.append(x)
        else:
            r.append(x)
    return sort1(l) + [p] + sort1(r)

ui = input('input ur numbers: ')
nums = []
for x in ui.split():
    nums.append(int(x))
print('sorted numbers:', sorted_squares(nums))  