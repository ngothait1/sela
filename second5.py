IDS = {}
for i in range(20):
    name = input("Enter your name: ")
    ID = input("Enter your ID: ")
    IDS[name] = ID
print(IDS)
def returnKeyIndex( dict : dict , key : str) -> int:
 index = -1
 for i, name in enumerate(dict):
        if name == key:
            index = i

 return index


grades={ 'sela' : 100 , 'david' : 90 , 'yossi' : 80 }
print(returnKeyIndex( grades , 'david' ))
print(returnKeyIndex( grades , 'amit' ))
for i in grades:
 print(dict[i])


 werid_dict = { 'sela' : { '32277' : 24 } , 'david' : { '35277' : 25 } , 'yossi' : { '32237' : 26 } , 'amit' : { '32923477' : 27 } }