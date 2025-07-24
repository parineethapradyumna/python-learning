nums = [71,29,89,90,78,28]
max = nums[0]
for i in range(len(nums)):
    if(nums[i]>max):
        max = nums[i]

print(f"Max = ",max)