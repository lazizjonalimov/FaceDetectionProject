def array_diff(a, b):
    #your code here
    aaa = len(a)
    for char in range(0, aaa + 1):
        for j in b:
            if j in aaa:
                a.remove(j)
    return a


kd = array_diff([1 ,2, 2, 2, 2, 2, 3, 2,], [2])
print(kd)