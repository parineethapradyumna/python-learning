nums = [12,13,19,10,2,34,43]
min = nums[0]
for i in range(len(nums)):
    if(nums[i]<min):
        min = nums[i]
print(f"Min = ",min)