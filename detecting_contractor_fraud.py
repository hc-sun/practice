import sys

def detection():
    #datafeed = ["Alice;START", "Bob;START", "Bob;1", "Carson;START","Alice;15", "Carson;6", "David;START", "David;24", "Evil;START", "Evil;24", "Evil;START", "Evil;18", "Fiona;START"]
    #datafeed = ["Tom;START", "Jeremy;START", "Dana;START", "Jeremy;4", "Dana;2", "James;START", "Leah;START", "James;5", "Nick;START", "Tom;1", "Nick;6", "Leah;3"]
    #datafeed = ["Nick;START", "Jeremy;START", "Leah;START", "Nick;10", "Jeremy;START", "Jeremy;START", "Leah;15", "Jeremy;8,14,9"]#12
    #datafeed = ["Nick;START", "Jeremy;START", "Leah;START", "Nick;10", "Jeremy;START", "Leah;15", "Jeremy;8,14"]#14 kong
    #datafeed = ["Jeremy;START", "Leah;START", "Leah;50", "Jeremy;START", "Leah;START", "Leah;100", "Jeremy;START", "Leah;START", "Leah;150", "Jeremy;START", "Jeremy;37,52,68,86", "John;START", "John;START", "John;500,5000"]
    #datafeed = ["Jeremy;START", "Jeremy;2147483648","Jeremy;START","Jeremy;5"]
    #datafeed = ["Jeremy;START", "Jeremy;-5", "Tom;START", "Tom;-6"]

    result = []
    dic = {}
    line_num = 1
    large_num = -sys.maxsize
    for data in datafeed:
        temp = data.split(';')
        if temp[1] == "START":
            if temp[0] in dic:
                dic[temp[0]][0].append(line_num)
                dic[temp[0]][1].append(large_num)
            else:
                dic[temp[0]] = [[line_num], [large_num]]
        else:
            ids = sorted([int(n) for n in temp[1].split(',')])
            ori_id = dic.get(temp[0])
            suspicious = False
            shortened = True
            for i in range(len(ids)):
                if int(ids[i]) < int(ori_id[1][i]):
                    suspicious = True
                    for j in range(i+1, len(ids)):
                        if int(ids[j]) >= int(ori_id[1][j]):
                            shortened = False
                            break
                    if shortened:
                        result.append(str(ori_id[0][i]) + ";" + temp[0] + ";" + "SHORTENED_JOB")
                else:
                    pass
            if suspicious and len(ids) > 1:
                result.append(str(line_num) + ";" + temp[0] + ";" + "SUSPICIOUS_BATCH")
            if large_num < ids[-1]:
                large_num = ids[-1]
            dic[temp[0]] = [[], []]
        line_num += 1
    return result


print(detection())
