MAX = 5
stack = [0]*MAX

sp = 0
#print(stack)

def push(d):
    global sp

    if sp <MAX:
        stack[sp] =d
        sp = sp+ 1
        print(f"データ{d}を追加しました。")
    else:
        print("これ以上データを入れられません")
    print(f"現在のデータ{stack}")
def pop():
    global sp
    if sp > 0:
        sp = sp -1
        return stack[sp]

    else:
        print("取り出すデータが存在しません")
        return None

for i in range(6):
    push(i)
for i in range(6):
    d = pop()
    print(f"取り出したデータ: {d}")


