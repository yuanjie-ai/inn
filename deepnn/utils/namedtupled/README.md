```python
import os
import namedtupled

print(namedtupled.map({"a": {"b": "v"}}))
print(namedtupled.json('{"a": {"b": "v"}}'))
print(namedtupled.yaml("a: a"))

os.environ['a'] = 'a'
os.environ['b'] = 'b'
print(namedtupled.env(['a', 'b']))

print(namedtupled.zip(['a', 'b'], ['a', 'b']))
```