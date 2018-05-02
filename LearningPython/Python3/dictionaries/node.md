# Dictionaries

| Operation | Interpretation|
| --- | --- |
| D = {}  | Empty dictionary |
| D = {'name': 'Bob', 'age': 40}  | Two-item dictionary |
| E = {'cto': {'name': 'Bob', 'age': 40}} |  Nesting |
| D = dict(name='Bob', age=40) |  Alternative construction techniques: |
| D = dict([('name', 'Bob'), ('age', 40)]) | keywords, key/value pairs |
| D = dict(zip(keyslist, valueslist)) | zipped key/value pairs |
| D = dict.fromkeys(['name', 'age'])|key lists|
| D['name']	| Indexing by key |
| E['cto']['age']||
| 'age' in D | Membership: key present test |
| D.keys()|Methods: all keys|
| D.values()|all values|
| D.items()|all key+value tuples|
| D.copy()|copy (top-level)|
| D.clear()|clear (remove all items)|
| D.update(D2)|merge by keys|
| D.get(key, default?)|fetch by key, if absent default (or None)|
| D.pop(key, default?)|remove by key, if absent default (or error)|
| D.setdefault(key, default?)|fetch by key, if absent set default (or None)|
| D.popitem()|remove/return any (key, value) pair; etc|
| len(D) | Length: number of stored entries| 
| D[key] = 42 | Adding/changing keys| 
| del D[key] | Deleting entries by key| 
| list(D.keys())|Dictionary views (Python 3.X) | 
| D1.keys() & D2.keys()||
| D.viewkeys(), D.viewvalues() |Dictionary views (Python 2.7)|
| D = {x: x*2 for x in range(10)} |Dictionary comprehensions (Python 3.X, 2.7)|