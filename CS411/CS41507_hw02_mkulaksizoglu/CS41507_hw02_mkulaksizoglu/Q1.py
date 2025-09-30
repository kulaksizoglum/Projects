n=367


def generate(n):
    results = []

    initial=[]
    for i in range(1,367):
        initial.append(i)


    for i in range (1,367):
        check=[]

        for x in range(1,367):
            
            elem= pow(i,x,n)
            check.append(elem)
        check.sort()

        if check== initial:
            results.append(i)

    return results


gens = generate(367)
print("Z367 has generators", gens)