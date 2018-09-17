nums = [2,9,6,3,6,5,5]
temp = []
for i in range(len(nums)):
    if nums[i] in nums[i+1:] and nums[i] not in temp:
        temp.append(nums[i])
print(temp)
