## List

Create List
* list1 = ['google', 1, 2]
* list2 = [1, 2, 3, 4]
* list3 = ['a', 'b', 'c', 'd']

length
* len(list)

get item from list
* list1[0] >> 'google'
* 从尾部开始 list1[-1] >> 2, list1[-2] >> 1
* list2[1:4] >> [头下标:尾下标]: [2, 3, 4]

add
* list1.append('test')
* list1.extend(list2), 合并, list2添加到list1末尾

delete
* del list1[2]
* list1.pop()
* list1.remove(val) >> 删除匹配的第一个val

操作
* len([1, 2, 3]) >> 3
* [1, 2, 3] + [4, 5, 6] >> [1, 2, 3, 4, 5, 6]
* ['Hi!'] * 4 >> ['Hi!', 'Hi!', 'Hi!', 'Hi!']
* 3 in [1, 2, 3] >> true

遍历
* for in range(start, end, step)
* for x in [1, 2, 3]: print(x, end=" ")
* continue
* break

无穷大(小)
* float('inf')
* float('-inf')

除法
* 舍弃小数部分：a // b
* 向上取整：math.ceil(1.1) => 2
* 向下取整：math.floor(1.1) => 1
* 四舍五入：round(a)

排序
* sorted(): sorted_list = sorted(my_list, reverse=True), 返回新list，不会改变原始list
* list.sort(): 改变原始列表

## String
* 大小写判断和转换
* s.isupper()
* s.islower()
* s.upper()
* s.lower()

String to List
* str = 'abcde'
* arr = list(str) -> arr = [a,b,c,d,e]
* arr = str.split('') -> arr = [a,b,c,d,e]

List to String
* arr = [a,b,c,d,e]
* str = ','.join(arr) -> str = a,b,c,d,e
* 在string中插入间隔符：'#'.join(s) -> s = 'ab', '#'.join(s) = '#a#b#'


正则
* import re
* re.match(pattern, s)
* eg: pattern = r'^[0-9a-fA-F]+$'   判断s中是否只包含0-9, a-f, A-F

str和Unicode
* str to unicode -> ord('a')
* unicode to str -> chr(97)
