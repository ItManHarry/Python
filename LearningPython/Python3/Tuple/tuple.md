# Tuple

## Tuple methods

| Operation | Interpretation |
| --- | --- |
| () | An empty tuple |
| T = (0,) | A one-item tuple (not an expression) |
| T = (0, 'Ni', 1.2, 3) | A four-item tuple |
| T = 0, 'Ni', 1.2, 3 | Another four-item tuple (same as prior line) |
| T = ('Bob', ('dev', 'mgr')) | T = ('Bob', ('dev', 'mgr')) |
| T = tuple('spam') | Tuple of items in an iterable |
| T[i] | Index |
| T[i][j] | index of index |
| T[i:j] | slice |
| len(T) | length |
| T1 + T2 | Concatenate |
| T * 3 | repeat |
| for x in T: print(x) | Iteration |
| 'spam' in T | membership |
| [x ** 2 for x in T] |  |
| T.index('Ni') | Methods in 2.6, 2.7, and 3.X: search, count |
| T.count('Ni') |  |
| namedtuple('Emp', ['name', 'jobs']) | Named tuple extension type |

## Tuple in action