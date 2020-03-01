def sortTransformedArray(nums, a, b, c):
        if not a:
            if b >= 0:
                res = list(map(lambda n: b*n+c, nums))
            else:
                res = list(map(lambda n: b * n + c, reversed(nums)))
        else:
            i = 0
            while nums[i] < -b/2/a:
                i += 1
            nums_left = nums[:i][::-1]
            nums_right = nums[i:]
            print(nums_right)
            record = []
            while nums_left and nums_right:
                if nums_left[0] + nums_right[0] > -b/a:
                    record.append(nums_left[0])
                    nums_left = nums_left[1:]
                else:
                    record.append(nums_right[0])
                    nums_right = nums_right[1:]
            record += nums_left + nums_right
            if a > 0:
                res = list(map(lambda n: a * n **2 + b*n+c, record))
            else:
                res = list(map(lambda n: a * n **2 + b * n + c, reversed(record)))
        return res

print(sortTransformedArray(nums = [-4,-2,2,4], a = -1, b = 3, c = 5))