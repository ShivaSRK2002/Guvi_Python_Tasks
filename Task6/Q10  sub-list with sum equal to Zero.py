lst = [4, 2, -3, 1, 6]
for i in range(len(lst)):
    sum_of_sublist = 0
    for j in range(i, len(lst)):
        sum_of_sublist += lst[j]
        
        if sum_of_sublist == 0:
            print("Sublist with sum equal to zero:", lst[i:j+1])
            break
   
    if sum_of_sublist == 0:
        break

else:
    print("There is no sublist with sum equal to zero.")
