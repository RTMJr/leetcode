#!/usr/bin/env python3

from typing import List


def max_subarray(nums: List[int]) -> int:
    if (len(nums) == 1):
        return nums[0]

    return aux(nums, 0, 0, 0)



def aux(nums: List[int], i: int, curr_max: int , max_sum: int):
    if (i == len(nums)):
        return max(curr_max, max_sum)

    for j in range(i, len(nums)):
        curr_max += nums[j]
        curr_max = max(curr_max, aux(nums, j + 1, curr_max, max_sum))
        max_sum = curr_max
        curr_max = 0

    return max_sum

nums = [-2, 1, 3, 4, -1, 2, 1, -5, 4]

print(max_subarray(nums))



