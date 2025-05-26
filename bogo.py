"""
#ボゴソートのコード例
Udemyの酒井氏の講座から
ランダムに並べ替えを行い、ソートが完了したら並べ替え終了
ギャンブル好きにはたまらないソーティングメソッド

in_order関数のreturnの書き方が秀逸。

これを何も見ずにかけるようになりたいなーと日々精進を誓う。

あと、自分はwhile文が苦手。
無限ループを嫌うことにより、while文を使用する選択肢が最初から頭にない。

この苦手意識を克服しないと。
"""



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
