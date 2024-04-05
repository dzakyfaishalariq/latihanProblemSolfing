def solution(nums):
    if nums == None:
        return []
    return sorted(nums)


print(solution([1, 4, 3, 2, 6, 5, 1]))
print(solution(None))
