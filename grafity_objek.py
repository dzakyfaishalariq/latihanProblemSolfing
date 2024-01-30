import math
def solution(arr_val, arr_unit) :
    lis_all_unit = []
    for i in range(len(arr_unit)):
        if arr_unit[i] == "g" :
            lis_all_unit.append(arr_val[i] * 10**-3 )
        elif arr_unit[i] == "mg":
            lis_all_unit.append(arr_val[i] * 10**-6)
        elif arr_unit[i] == "μg":
            lis_all_unit.append(arr_val[i] * 10**-9)
        elif arr_unit[i] == "lb":
            lis_all_unit.append(arr_val[i] * 0.453592)
        elif arr_unit[i] == "cm":
            lis_all_unit.append(arr_val[i] * 10**-2)
        elif arr_unit[i] == "mm":
            lis_all_unit.append(arr_val[i] * 10**-3)
        elif arr_unit[i] == "μm":
            lis_all_unit.append(arr_val[i] * 10**-6)
        elif arr_unit[i] == "ft":
            lis_all_unit.append(arr_val[i] * 0.3048)
        else:
            lis_all_unit.append(arr_val[i])
    print(lis_all_unit)
    G = 6.67 * (10**(-11))
    return (G*lis_all_unit[0]*lis_all_unit[1])/(lis_all_unit[2]**2)

print(solution([1000, 1000, 100],["kg", "kg", "cm"]))