def count(s):
    uniq = set(s)
    dic = {}
    for i in uniq:
        dic[i] = s.count(i)
    return dic


print(count("aabb"))
