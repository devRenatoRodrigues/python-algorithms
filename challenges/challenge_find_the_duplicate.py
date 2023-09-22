def find_duplicate(nums):
    if len(nums) <= 1:
        return False
    quick_nums = sorted(nums)
    for index, num in enumerate(quick_nums):
        if isinstance(num, str) or num < 0:
            return False
        if num == quick_nums[index - 1]:
            return num
    return False
