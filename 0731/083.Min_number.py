nums = [71,29,89,90,78,28]
min = nums[0]
for i in range(len(nums)):
    if(nums[i]<min):
        min = nums[i]
print(f"min = ",min)

###OUTPUT###
# min =  28