# each time climb 1 or 2 stairs to to the top
def climb_stair(stair_num):
    if stair_num == 0 or stair_num == 1:
        return 1
    num_ways = [1,2]
    for i in range(2, stair_num):
        num_ways.append(num_ways[i-1] + num_ways[i-2])
    return num_ways[-1]
n = climb_stair(4)
print(n)
# num of stairs can take[1,3,5], num_ways[i]=num_ways[i-1]+nums_ways[i-3]+num_ways[i-5]
