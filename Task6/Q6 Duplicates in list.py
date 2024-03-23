
def find_duplicates(list1, list2, list3):
    
    duplicates = []
    
    
    for item in list1:
        
        if item in list2 and item in list3:

            duplicates.append(item)
    
    
    return duplicates
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
result = find_duplicates(list1, list2, list3)
print("The duplicates among the three lists are:", result)
