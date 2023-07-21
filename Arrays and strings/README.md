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
* for x in [1, 2, 3]: print(x, end=" ")

遍历
* for in range(start, end, step)