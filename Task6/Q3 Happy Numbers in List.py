input= [10, 501, 22, 37, 100, 999, 87, 351]

HappyNumList=[]
def CheckHappyNumber(n):
    digit = sum = 0
    while (n > 0):
        digit = n % 10
        sum = sum + (digit * digit)
        n = n // 10
    return sum

for x in input:
  result = x

  while (result != 1 and result != 4):
   result = CheckHappyNumber(result)

  if (result == 1):
    HappyNumList.append(x)

print("Happy Numbers List: ", HappyNumList)



