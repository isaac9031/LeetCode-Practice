def arithmeticTriplets( nums: list[int], diff: int) -> int:
    seen = set()
    cnt = 0
    for num in nums:
        print(num-diff)
        print(num - diff * 2 )
        print(num)
        if num - diff in seen and num - diff * 2 in seen:
            cnt += 1
        seen.add(num)
    print(seen)
    return cnt



diff = 3
nums = [0,1,4,6,7,10]
print(arithmeticTriplets((nums), diff))


#review this problem
