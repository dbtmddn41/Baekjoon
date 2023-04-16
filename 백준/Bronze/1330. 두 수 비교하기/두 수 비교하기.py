nums = input().split()
nums0 = int(nums[0])
nums1 = int(nums[1])
if nums0 > nums1:
    print('>')
elif nums0 < nums1:
    print('<')
else:
    print('==')
