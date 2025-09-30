def find_generator(order, n):
    list=[]

    for i in range(2, n):
        if pow(i, order)%n == 1:
            list.append(i)
    return list

n=367
order = 61

list = find_generator(order, n)

print("Generator of the subgroup of order 61:", list)