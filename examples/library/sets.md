# sets 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `difference`

Documentation: https://arturo-lang.io/documentation/library/sets/difference

### Example 1

```arturo
print difference [1 2 3 4] [3 4 5 6]
; 1 2
```

### Example 2

```arturo
a: [1 2 3 4]
b: [3 4 5 6]
difference 'a b
; a: [1 2]
```

### Example 3

```arturo
print difference.symmetric [1 2 3 4] [3 4 5 6]
; 1 2 5 6
```

## `disjoint?`

Documentation: https://arturo-lang.io/documentation/library/sets/disjoint-

### Example 1

```arturo
disjoint? [1 2 3 4] [3 4 5 6]
; => false

disjoint? [1 2 3 4] [5 6 7 8]
; => true
```

## `intersect?`

Documentation: https://arturo-lang.io/documentation/library/sets/intersect-

### Example 1

```arturo
intersect? @1..10 @8..12
; => true

intersect? ["one" "two" "three"] ["three" "four" "five"]
; => true

intersect? ["one" "two" "three"] ["four" "five" "six"]
; => false
```

## `intersection`

Documentation: https://arturo-lang.io/documentation/library/sets/intersection

### Example 1

```arturo
print intersection [1 2 3 4] [3 4 5 6]
; 3 4
```

### Example 2

```arturo
a: [1 2 3 4]
b: [3 4 5 6]
intersection 'a b
; a: [3 4]
```

## `powerset`

Documentation: https://arturo-lang.io/documentation/library/sets/powerset

### Example 1

```arturo
powerset [1 2 3]
;  [[] [1] [2] [1 3] [3] [1 2] [2 3] [1 2 3]]
```

## `subset?`

Documentation: https://arturo-lang.io/documentation/library/sets/subset-

### Example 1

```arturo
subset? [1 3] [1 2 3 4]
; => true

subset?.proper [1 3] [1 2 3 4]
; => true

subset? [1 3] [3 5 6]
; => false

subset? [1 3] [1 3]
; => true

subset?.proper [1 3] [1 3]
; => false
```

## `superset?`

Documentation: https://arturo-lang.io/documentation/library/sets/superset-

### Example 1

```arturo
superset? [1 2 3 4] [1 3]
; => true

superset?.proper [1 2 3 4] [1 3]
; => true

superset? [3 5 6] [1 3]
; => false

superset? [1 3] [1 3]
; => true

superset?.proper [1 3] [1 3]
; => false
```

## `union`

Documentation: https://arturo-lang.io/documentation/library/sets/union

### Example 1

```arturo
print union [1 2 3 4] [3 4 5 6]
; 1 2 3 4 5 6
```

### Example 2

```arturo
a: [1 2 3 4]
b: [3 4 5 6]
union 'a b
; a: [1 2 3 4 5 6]
```
