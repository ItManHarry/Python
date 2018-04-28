# List

- Common list literals and operations

| Operation | Interpretation |
| --- | --- |
| L = [] |  An empty list |
| L = [123, 'abc', 1.23, {}] |  Four items: indexes 0..3 |
| L = ['Bob', 40.0, ['dev', 'mgr']]  | Nested sublists |
| L = list('spam') | List of an iterable’s items |
| L = list(range(-4, 4)) | list of successive integers |
| L[i]		 | Index |
| L[i][j]	 | index of index |
| L[i:j]	 | slice |
| len(L)	 | length |
| L1 + L2 	 | Concatenate |
| L * 3 	 | repeat |
| for x in L: print(x) | Iteration |
| 3 in L | membership |
| L.append(4) | Methods: growing |
| L.extend([5,6,7]) |  |
| L.insert(i, X) |  |
| L.index(X) | Methods: searching |
| L.count(X) |  |
| L.sort() | Methods: sorting |
| L.reverse() | Methods: reversing |
| L.copy() | copying (3.3+) |
| L.clear() | clearing (3.3+) |
| L.pop(i)| Methods, statements: shrinking |
| L.remove(X) |  |
| del L[i] |  |
| del L[i:j]|  |
| L[i:j] = [] |  |
| L[i] = 3 | Index assignment, slice assignment |
| L[i:j] = [4,5,6] |  |
| L = [x**2 for x in range(5)] | List comprehensions and maps |
| list(map(ord, 'spam')) |  |

- List in action
