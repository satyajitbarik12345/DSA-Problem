def getconcatination(nums):
    n=len(nums)
    ans= [0] *(2 * n)
    for i in range(n):
        ans[i] = nums[i]
        ans[i+n] = nums[i]
    return ans
nums=eval(input("enter an array:-"))
result=getconcatination(nums)
print(result)