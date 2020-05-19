#!/usr/bin/python
# -*- coding: utf-8 -*-


# n皇后问题
result = []
su = set()  # 存放竖直方向
pie = set()  # 撇方向
na = set()  # 捺方向


def huanghouN(n):
    def dfs(n, row, current_stat):
        if row == n:
            result.append(current_stat)
            return

        for i in range(n):
            if i in su or (row + i) in pie or (row - i) in na:  # 判断该位置是否可以放皇后
                continue
            su.add(i)
            pie.add(row + i)
            na.add(row - i)
            dfs(n, row + 1, current_stat + [i])

            # 恢复现场，目的不影响同行中的其他列
            su.remove(i)
            pie.remove(row + i)
            na.remove(row - i)

    dfs(n, 0, [])




if __name__ == '__main__':
    huanghouN(8)
    print(result)
