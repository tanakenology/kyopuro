from __future__ import annotations
from collections import defaultdict

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = set()
        before_dict = defaultdict(list)
        N = len(nums)

        print(f"nums: {nums}")
        print('---------')
        for i, num in enumerate(nums):
            print(f"i: {i}, num: {num}")
            for j in range(i - 1):
                before_dict[nums[j] + nums[i - 1]].append([j, i - 1])
            print([f"{k}: {v}" for k, v in before_dict.items()])

            for j in range(i + 1, N):
                val = num + nums[j]
                look_for = target - val
                print(f"j = {j}, look_for = {target} - ({num} + {nums[j]}) = {look_for}")
                if look_for in before_dict:
                    for bef1, bef2 in before_dict[look_for]:
                        print(f"bef1: {bef1}, bef2: {bef2}, i: {i}, j: {j}")
                        res.add((nums[bef1], nums[bef2], nums[i], nums[j]))
            print('---------')

        return [list(item) for item in list(res)]

    def fourSum2(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = set()
        left_side_sum_index_dict = defaultdict(list)

        for i in range(2, len(nums)):


if __name__ == "__main__":
    nums = list(map(int,input()[1:-1].split(',')))
    target = int(input())

    solution = Solution()
    ans = solution.fourSum(nums, target)

    print(ans)
