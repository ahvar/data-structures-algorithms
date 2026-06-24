# Group Anagrams

Given an array of strings `strs`, group the anagrams together.
You can return the answer in any order.

## Example 1

**Input**

```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output**

```text
[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

**Explanation**

- There is no string in `strs` that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams of each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams of each other.

## Example 2

**Input**

```text
strs = [""]
```

**Output**

```text
[[""]]
```

## Example 3

**Input**

```text
strs = ["a"]
```

**Output**

```text
[["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.