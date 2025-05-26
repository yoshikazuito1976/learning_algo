import random
from typing import List

def in_order(numbers: List[int]) ->bool:

    return all([numbers[i]<= numbers[i+1] for i in range(len(numbers)-1)])
#    for i in range(len(numbers)-1):
#        if numbers[i] >numbers[i+1]:
#            return False
#        return True



def bogo_sort(numbers: List[int])-> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    
    return numbers



if __name__ == "__main__":
    print(bogo_sort([1,5,3,2,6]))
