# given array is like 
# arr = [2,7,3,4,8,7,7,2,3]
# seg = 4
# key = 7
# if key is present in every segment window then it give True otherwise give False

def find_key(arr, key, seg):
    _len = len(arr)
    _intial = 0

    for i in range(_intial, _len, seg):
        flag = False
        k = i+seg
        if k > _len:
            k = _len
        for j in range(i, k):
            if arr[j] == key:
                flag = True
                break
    return flag

arr = [2,7,3,4,8,7,7,2,3]
key = 7
seg = 4

result = find_key(arr, key, seg)

if result:
    print(True)
else:
    print(False)




