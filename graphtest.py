import numpy as np
import matplotlib.pyplot as plt

# x を -2 から 10 までの範囲で生成
x = np.linspace(-2, 10, 500)

# y = min(x, 5) を要素ごとに適用
y = np.minimum(x, 5)

# グラフを描画
plt.plot(x, y, label='y = min(x, 5)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = min(x, 5)')
plt.grid(True)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.savefig("graph.png")
