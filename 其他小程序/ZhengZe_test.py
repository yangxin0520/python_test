# 学习正则表达式时用的

import re

text = ""
PATH = 'H:/'
file = open(PATH + "test.txt",'r')
for lines in file:
    text = lines + text
file.close()


result = re.findall(' ([Aa][a-z][a-z]) |(A[a-z][a-z]) ',text)
final_result =set()
for pair in result:
    if pair[0] not in final_result:
        final_result.add(pair[0])
    if pair[1] not in final_result:
        final_result.add(pair[1])

final_result.remove('')
print(final_result)
