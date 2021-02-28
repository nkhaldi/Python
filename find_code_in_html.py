#!/usr/bin/env python3

# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит
# статью с Википедии про язык Python. В этой статье есть теги code,
# которыми выделяются конструкции на языке Python.
# Вам нужно найти все строки, содержащиеся между тегами
# <code> и </code> и найти те строки, которые встречаются чаще всего
# и вывести их в алфавитном порядке, разделяя пробелами.


from re import findall
from collections import Counter
from urllib.request import urlopen


url = "https://stepik.org/media/attachments/lesson/209719/2.html"
html = str(urlopen(url).read().decode('utf-8'))
regex = r'<code>(.*?)</code>'
lst = sorted(findall(regex, html))

ans = list()
count = Counter(lst)
max_cnt = max(count.values())
for key in count:
    if count[key] == max_cnt:
        ans.append(key)
print(' '.join(ans))
