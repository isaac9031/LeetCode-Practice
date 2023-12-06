def twoSum(numbers: list[int], target: int) -> list[int]:
    lp = 0
    rp = len(numbers)-1
    while lp < rp:
        total = numbers[lp] + numbers[rp]
        if total == target:
            return [lp+1, rp+1]
        if total < target:
            lp+=1
        if total > target:
            rp-=1


numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
