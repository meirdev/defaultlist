# defaultlist

`defaultlist` is like `defaultdict`, but for a list.

# Example

```python
from defaultlist import defaultlist

mylist = defaultlist(int)

mylist[4] = 7

print(mylist)  # [0, 0, 0, 0, 7]

print(mylist[6])  # 0

print(mylist)  # [0, 0, 0, 0, 7, 0, 0]
```
