## dictionary (字典)

Create
* tinydict1 = { 'abc': 456 } 
* tinydict2 = { 'abc': 123, 98.6: 37 }
* emptyDict = {}
* emptyDict = dict()

get
* tinydict1['abc']

update & add
* tinydict1['abc'] = 8
* tinydict1['cd'] = 3

delete
* del tinydict1['abc']
* tinydict1.clear()
* del tinydict1

function
* len(dic)
* dic.clear()
* if key in dict
* for key, value in dict.items()
* dict.keys()
* dict.values()

## set (集合)

create
* set1 = {1, 2, 3, 4}
* set2 = set([4, 5, 6, 7])
* set3 = set('abracadabra')
* emptySet = set()

add
* set1.add(x)

delete
* s.remove(x)  #如果s中不存在x，会报错
* s.discard(x)  #不会报错

function
* len(s)
* s.clear()
* x in s
* x not in s