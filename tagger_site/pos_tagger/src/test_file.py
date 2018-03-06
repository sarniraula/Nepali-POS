a = [1, 2, 3, 4, 5, 6, 7]
for i, element in enumerate(a):
    print(a[i])
    if i==4:
        a.insert(i+1, 100)