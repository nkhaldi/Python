#!/usr/bin/env python3

"""
После окончания уроков n групп школьников вышли на улицу и
собрались ехать домой к Артуру на празднование его дня рождения.
Известно, что i-ая группа состоит из s друзей (1 ≤ s_≤ 4),
которые не хотят расставаться по пути к Артуру.
Решено ехать на такси. Каждая машина может вместить
не более четырех пассажиров. Какое минимальное количество
машин потребуется школьникам, если каждая группа должна
целиком находиться в одной из машин такси
(одна машина может вмещать более чем одну группу)?
"""

num = int(input())
groups = sorted([int(i) for i in input().split()])[::-1]
taxis = list()

for gr in groups:
    put = False
    for i in range(len(taxis)):
        if gr + taxis[i] <= 4:
            taxis[i] += gr
            put = True
            break
    if not put:
        taxis += [gr]

print(len(taxis), "cars")
print(taxis)
