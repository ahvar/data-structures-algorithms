from sortedcontainers import SortedDict

sorted_dict = SortedDict({"banana": 3, "apple": 2, "pear": 1, "orange": 4})
print(sorted_dict)

print(sorted_dict.bisect_left("apple"))
print(sorted_dict.bisect_right("apple"))
item = sorted_dict.pop("apple")
print(item)

value = sorted_dict.get("apple", "not found")
print(value)

last_item = sorted_dict.peekitem()
print(last_item)
