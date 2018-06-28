# coding:utf-8
'''
排序算法实现
1.插入排序
2.

'''
def insert_sort(nums):
    l = len(nums)
    '''
    for i in range(1,l):
        tmp = nums[i]
        j = i
        while j > 0 and nums[j-1] > tmp:
            nums[j] = nums[j-1]
            nums[j-1] = tmp
            j -= 1
    '''
    for i in range(1, l):
        if nums[i-1] > nums[i]:
            tmp = nums[i]
            nums.pop(i)
            for j in range(i-1,-1,-1):
                if tmp > nums[j]:
                    nums.insert(j+1, tmp)
                    break
                if j == 0:
                    nums.insert(j, tmp)
    return nums

#希尔排序


def shell_sort(nums):
    l = len(nums)
    dk = l//2
    while dk > 1:
        for i in range(dk,l):
            if nums[i] < nums[i-dk]:
                nums[i], nums[i-dk] = nums[i-dk], nums[i]
        dk = dk // 2
    return insert_sort(nums)




