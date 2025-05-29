'''
問題文
N 個の整数 
a1,a 2,⋯,aN
  が与えられます。

(a1+a2+⋯+aN)mod100 の値を出力してください。

制約
1≤N≤50
1≤ai≤100 (1≤i≤N)
入力はすべて整数

入力
N
a1 a2 a3 ... aN

入力例
3
30 50 70

出力例
50
'''
#n = int(input())
#a = list(map(int,input().split()))

a=[30,50,70]
s = 0
#print(a)
for v in a:
  s += v

print(s % 100)

