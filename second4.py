def multiplyListBy2(list:list)->list:
    return [i*2 for i in list]

def strListToInt(list:list)->list:
    return [int(i) for i in list]

def printList(list:list):
    for index,i in enumerate (list):
        print(f'Index: {index} Value: {i}')







numList=[]
for i in range(50):
    numList.append(input("Enter a number: "))
numList=strListToInt(numList)
printList(numList)
print(len(numList))



list2=[1,2,3,4,44]
print(multiplyListBy2(list2))

for i in range (1001):
        print(i)
