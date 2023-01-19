if  not nums: 
        return 0
    lower, ctr, res, max_num = 0, 0 , 1, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            ctr += 1
        while ctr > res:
            if nums[lower] == 0:
                ctr -= 1
            lower += 1
        max_num = max(max_num, i-lower)
    return max_num
