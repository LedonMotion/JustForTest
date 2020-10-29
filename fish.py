# !usr/bin/env python
# _*_ coding:utf-8 _*_

num = 1

while True:
    flag = True
    total = num
    for _ in range(5):
        if (total - 1) % 5== 0:
            total = (total - 1) // 5
        else:
            flag = False
            break
    if not flag:
        break

print(num)
