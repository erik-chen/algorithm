def checkPerfectNumber(num: int) -> bool:
    import collections
    num_ori = num
    if num > 0:
        dic = collections.defaultdict(int)
        i = 2
        while num >= i ** 2:
            if num % i == 0:
                num = int(num / i)
                dic[i] += 1
            else:
                i += 1
        if num != 1 and num != num_ori:
            dic[num] += 1
        spe = [1]
        while dic:
            pro = dic.popitem()
            new = []
            for i in spe:
                for j in range(pro[1] + 1):
                    new.append(i * pro[0] ** j)
            spe = new
        print(spe)
        res = sum(spe) - num_ori == num_ori

    else:
        res = False
    return res
checkPerfectNumber(12)