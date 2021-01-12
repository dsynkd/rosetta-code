from typing import List

def hundred_doors(doors: List[bool]) -> List[bool]:
    for i in range(0,100):
        for j in range(0,100,i+1):
            doors[j] = not doors[j]
    print(doors)

hundred_doors([False for i in range(0,100)])
