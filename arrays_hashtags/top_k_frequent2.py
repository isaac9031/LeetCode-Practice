def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    # freq = [[]for i in range(len (nums) + 1)]
    freq = []

    for i in range(len(nums) + 1):
        freq.append([])

    for n in nums:
        count[n] = 1 + count.get(n, 0) #adds the key to keep_t and starts it at 0 if it doesn't exist, then it adds on
                                        #{4:1, 1:1, -1:2, 2:2, 3:1}
    for key, value in count.items():  # makes a list that places the key in the index of how many times it was seen.
        freq[value].append(key)         #...index 1(freq[value]) will append 4 , then to append 1 to index 1, then in index 2 to append -1, then append 2 to index 2, and at the end place 3 in index 1...
    print(freq)             #...[[], [4, 1, 3], [-1, 2], [], [], [], [], []]

    res=[]
    for i in range(len(freq) - 1, 0, -1): #will start from the last of the list
        for n in freq[i]:   #will go inside each list and add one element at the time from the freq list to the res list
            res.append(n)  # adds -1 first then 2 on the next loop
            if len (res) == k:
                return res


nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums, k))
