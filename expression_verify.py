# ONE+ONE
# TWO
# 231+231
# 462

# FOUR+FOUR
# EIGHT
# 5239+5239
# 10478

# FOUR+ONE
# FIVE
# 6130+149
# 6279

def eval_expression(s1, s2, s3, dic):
    s1_num = int(''.join([str(dic.get(ch)) for ch in s1]))
    s2_num = int(''.join([str(dic.get(ch)) for ch in s2]))
    s3_num = int(''.join([str(dic.get(ch)) for ch in s3]))
    return s1_num+s2_num == s3_num
        
# dic = {'O':2, 'N':3, 'E':1, 'T':4, 'W':6}


