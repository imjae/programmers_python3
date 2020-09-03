def solution(arr1, arr2):
    array1 = [[0]*len(arr1) for _ in arr1]

    for i1, v1 in enumerate(arr1):
        for i2, v2 in enumerate(v1):
            print(i1, i2)
            array1[i1][i2] = arr1[i1][i2] + arr2[i1][i2]

    return array1

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))