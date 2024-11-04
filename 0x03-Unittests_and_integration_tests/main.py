#!/usr/bin/env python3
from utils import access_nested_map

nestedMap = {
    "a": {
        "z": {
            "b": {
                "c": [
                        3,
                        {
                            "d": 1
                        }
                    ]
            }
        }
    }
}


result = access_nested_map(nestedMap, ["a", "z", "b", "c"])
print(result)

set_variables = {
    1: {
        2: {
            3: {
                "user": ["azuka", "gideon", "david", "ibinabo"]
            }
        }
    }
}

nested_map={"a": {"b": 2}}
print(access_nested_map.__doc__)
checkKeyFormat = access_nested_map(nested_map, ("a",))

print(checkKeyFormat)
