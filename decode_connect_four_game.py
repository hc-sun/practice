# In:
# string = "9_r4_brbrbr_3b2rb_b2r2br_r2b3rb"
# Out:
# // |_|_|_|_|_|_|_|
# // |_|_|r|_|_|_|_| |
# // |b|r|b|r|b|r|_| | (GRAVITY)
# // |b|b|b|r|r|b|_| v
# // |b|r|r|b|b|r|_|
# // |r|b|b|r|r|r|b|

def decode_cfn_string(string):
    matrix = [[] for i in range(6)]
    row = i = 0
    row_len = 1
    while i < len(string):
        if string[i].isdigit(): #s.isalpha() check if letter
            for j in range(int(string[i])):
                if row_len == 8:
                    row_len = 1
                    row += 1
                print(string[:i])
                print(matrix)
                matrix[row].append(string[i+1])
                row_len += 1
            i += 2
        else:
            if row_len == 8:
                row_len = 1
                row += 1
            matrix[row].append(string[i])
            row_len += 1
            i += 1
    return matrix
