import random

while True:
    r = input('請按任意鍵擲骰, 連續骰到兩次相同數字就過關囉~')
    r = random.randint(1,6)
    print(r)
    a = input('請再按任意鍵擲骰')
    a = random.randint(1,6)
    print(a)
    if r == a:
        print('lucky man')
        break
    else:
        print('再來囉~')
