"""
In Python's `enum` module, each `Enum` type has a special attribute `_value2member_map_` which is an 
internal dictionary used to map values of the enum members to the members themselves. 
This allows for quick and efficient lookups by value.

For example:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color._value2member_map_)
```

The output will be:

```
{1: <Color.RED: 1>, 2: <Color.GREEN: 2>, 3: <Color.BLUE: 3>}
```

This means if you know a particular value and you want to determine if it corresponds to an 
enum member (or which member it corresponds to), you can use this map. It's a helpful attribute,
 especially when you need to check for the existence of a value within an `Enum`. 

That being said, `_value2member_map_` is technically considered an internal attribute (as indicated by the 
leading underscore). While it can be used as demonstrated, be cautious if you're planning to use it in
 production code since, in theory, internal details of standard library modules can change. In practice,
  however, such attributes tend to remain stable across versions.
"""

from enum import Enum


class Currency(Enum):
    PLN = "PLN"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    NOK = "NOK"
    USD = "USD"
    ZAR = "ZAR"

    @classmethod
    def is_member(cls, value: str) -> bool:
        return value in cls._value2member_map_
