from __future__ import annotations

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        >>> nums = [1,0,-1,0,-2,2]
        >>> target = 0
        >>> [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        """

        def kSum(nums: list[int], target: int, k: int) -> list[list[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                print(f"i = {i}\nnums = {nums}\ntarget = {target}\nk = {k}")
                if i == 0 or nums[i - 1] != nums[i]:
                    print('---------')
                    a = kSum(nums[i + 1:], target - nums[i], k - 1)
                    print(f"kSum = {a}")
                    for subset in a:
                        res.append([nums[i]] + subset)
                print(f"res = {res}")
                print('---------------------')

            return res

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            res = []
            s = set()
    
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return res

        nums.sort()
        return kSum(nums, target, 4)

if __name__ == "__main__":
    nums = list(map(int,input()[1:-1].split(',')))
    target = int(input())

    solution = Solution()
    ans = solution.fourSum(nums, target)

    print(ans)

def twoSum(nums: list[int], target: int) -> list[list[int]]:
    """
    >>> nums = [0, 0, 1, 2]
    >>> target = 3
    >>> [[1, 2]]
    """

    res = []
    s = set()

    for i in range(len(nums)):
        # nums[i] が連続して同じ値だったらスルー
        if len(res) == 0 or res[-1][1] != nums[i]:
            if target - nums[i] in s:
                res.append([target - nums[i], nums[i]])
        s.add(nums[i])

    return res
