'''
N枚のカードが並べられています。左からi番目(1 ≦ i ≦ N)のカードには整数Aiが書かれています。カードの中からいくつかを選んで、合計がちょうどSとなるようにする方法はありますか。 たとえば以下の入力の場合、カード1・3を選べば合計が11になるので答えはYesです。 ・N = 3 ・S = 11 ・(A1, A2, A3) = (2, 5, 9) 制約：1 ≦ N ≦ 60, 1 ≦ Ai ≦ 10000, 1 ≦ S ≦ 10000


米田 優峻. 問題解決のための「アルゴリズム×数学」が基礎からしっかり身につく本 (pp.95-96). 株式会社技術評論社. Kindle 版. 

'''
def subset_sum(N, S, A):
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True  # 0枚で0を作るのは常に可能

    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True  # カードiを使わない
                if j + A[i] <= S:
                    dp[i + 1][j + A[i]] = True  # カードiを使う

    return "Yes" if dp[N][S] else "No"

# 入力例
N = 3
S = 11
A = [2, 5, 9]

print(subset_sum(N, S, A))  
