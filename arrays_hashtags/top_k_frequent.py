def topKFrequent(nums: list[int], k: int) -> list[int]:
    d_track = {}
    for n in nums:
        if n not in d_track:
            d_track[n] = 0
        d_track[n]+=1   #keeps track of element(key) : value
    print(d_track)
    sort_by_value = sorted(d_track.items(), key=lambda x :x[1], reverse =True) #tuple comes from d_track.items(). at the end we have a list of tuples organized from greates to lowest value
    print(sort_by_value)

    lista = []
    for i in range(k):
        lista.append(sort_by_value[i][0]) #we first access the first tuple (-1,2) and return index 0, which is element -1
    return lista


nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums, k))



# Then sorted_tuple is created. This part was a new learning for me, as
# I didnt know sorted didn't have so many parameters. I need to sort the dictionary using the values, in an decending order.

# Sorted parameters are as follows sorted(iterable, key, reverse=?) where iterable is what you
# ... wanna iterate through, key is the function you wanna apply, and reverse=True sorts in decreasing order.
# ..So in this case the iterable will be d_track.items() which is in the tuple format, key is a lambda fucntion lambda x:x[1], which
# is telling the sort to happen in terms of the values and reverse=True to sort in a decending order. The output is in a tuple format.




# In your code, the tuples are not being created inside the
# ..list by the sorted function. Instead, the tuples come from the dict_track.items() metho
