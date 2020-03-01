def twoSum(numbers, target: int):
        nums = numbers

        def couple(num1, nums, n0):
            n = len(nums)
            if not n:
                return False
            p = n // 2
            if num1 + nums[p] > target:
                return couple(num1, nums[:p], n0)
            if num1 + nums[p] < target:
                return couple(num1, nums[p + 1:], n0 + p + 1)
            if num1 + nums[p] == target:
                return n0 + p + 1

        # while True:
        # print(nums)
        num1 = nums[0]

        nums = nums[1:]
        if couple(num1, nums, 1):
            return couple(num1, nums, 1)

print(twoSum(numbers = [2, 7, 11, 15], target = 9))
