# 1 1
# 2 1*1 1
# 3 1*2 2
# 4 2*2 4
# 5 2*3 6
# 6 3*3 9
# 7 2*2*3 or 3*4 12

def cut_rope(rope_len):
    if rope_len < 2:
        return 0
    elif rope_len == 2:
        return 1
    elif rope_len == 3:
        return 2
    temp = [0, 1, 2, 3]
    max_num = 0
    for i in range(4, rope_len + 1):
        for j in range(1, i//2 + 1):
            num = temp[j] * temp[i-j]
            if max_num < num:
                max_num = num
        temp.append(max_num)
    return temp[-1]
test = cut_rope(7)
print(test)
