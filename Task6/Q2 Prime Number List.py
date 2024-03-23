list= [10, 501, 22, 37, 100, 999, 87, 351]

primelist= []

for x in list:

    if x==0 or x<=1:
        continue

    for y in range (2, x):
            if x%y==0:
                break
    else:
        primelist.append(x)

print("Prime Numbers List: ", primelist)