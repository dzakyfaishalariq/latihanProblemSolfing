def count_positives_sum_negatives(arr):
    count_positif = 0
    sum_negatif = 0
    if arr == []:
        return []
    else: 
        for i in arr:
            if i > 0 :
                count_positif += 1
            elif i < 0:
                sum_negatif += i
            else:
                continue
        return [count_positif, sum_negatif]

print(count_positives_sum_negatives([]))