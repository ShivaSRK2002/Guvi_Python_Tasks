list= list(input("Enter the list of values: "). split())

list2=[]

for x in list:
    count=0
    for y in list:
        if x==y:
            count=count+1
        if count>1:
            break

    if count==1:
        list2.append(x)

print("The list of non repeating values: ",list2)