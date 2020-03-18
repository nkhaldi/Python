# Вам дана в архиве (ссылка) файловая структура,
# состоящая из директорий и файлов.

# Вам необходимо распаковать этот архив, и затем
# найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py". 

# Ответом на данную задачу будет являться файл со списком
# таких директорий, отсортированных в лексикографическом порядке.

import os

dirs = list()
for current_dir, dirs, files in os.walk('main'):
    if list(filter(lambda x: x.endswith('.py'), files)):
        dirs.append('{}\n'.format(current_dir))

dirs.sort()
with open('result.txt', 'w') as fd:
    for dr in dirs:
        fd.write(dr)
