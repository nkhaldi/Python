#!/usr/bin/env python3

"""
Часто в игре и в жизни мы встречаемся с некоторыми квестами.
Василий занимается разработкой новой игры и, конечно же,
занимается продумыванием квестов. В квестах принимают участие n npc
(npc- неигровой персонаж). Каждый из npc может вас отправить
по какому-то заданию к другому npc или же дать то, что вы просите.
Василий очень переживает насчет того, что он ошибся и какой-либо квест
окажется вечным. Помогите Василию проверить что квест проходим.

В первой строке содержится ровно одно число n <= 1
В следующей строке содержится ровно n чисел,
каждое из которых может быть от 1 до n - в случае
если этот npc отправит вас к следующему npc.
Или -1, если он отдаст вам награду ждя npc, отправившего вас.

Выведите "Yes если все получившиеся квесты будут конечными
и "No"в противном случае.
"""


def is_imposible(quest, quests, passed):
    if quests[quest] == -1:
        return False

    if quest in passed:
        return True

    passed.add(quest)
    return is_imposible(quests[quest], quests, passed)


if __name__ == "__main__":
    n = int(input())
    quests = [0] + [int(i) for i in input().split()]

    for quest in range(1, n + 1):
        passed = set()
        impossible = is_imposible(quest, quests, passed)
        if impossible:
            break

    print("No" if impossible else "Yes")
