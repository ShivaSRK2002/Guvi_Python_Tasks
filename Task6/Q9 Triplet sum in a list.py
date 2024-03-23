list= [10,20, 30,9]
value=59
counter=0

for x in list:
    if counter==1:
        break
    else:
        for y in list:
            if counter == 1:
                break
            else:
              for z in list:
                 if x+y+z==value:
                   print("The Triplets in the list with a sum value equal to 59 is: ",x,y,z)
                   counter=counter+1
                   break

