def merge_list(a, b):
    c = []
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


a = [1, 13, 22, 23, 34, 43, 44, 51, 72]
b = [-34, -8, 2, 12, 34, 54, 65, 87, 90]
print(merge_list(a, b))

# [-34, -8, 1, 2, 12, 13, 22, 23, 34, 34, 43, 44, 51, 54, 65, 72, 87, 90]