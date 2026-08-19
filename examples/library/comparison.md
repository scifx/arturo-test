# comparison 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `between?`

Documentation: https://arturo-lang.io/documentation/library/comparison/between-

### Example 1

```arturo
between? 1 2 3      ; => false
between? 2 0 3      ; => true
between? 3 2 3      ; => true
between? 3 3 2      ; => true

1 <=> 2 3           ; => false
1 <=> 3 2           ; => false
2 <=> 0 3           ; => true
2 <=> 3 0           ; => true
3 <=> 2 3           ; => true
```

## `compare`

Documentation: https://arturo-lang.io/documentation/library/comparison/compare

### Example 1

```arturo
compare 1 2           ; => -1
compare 3 3           ; => 0
compare 4 3           ; => 1
```

## `equal?`

Documentation: https://arturo-lang.io/documentation/library/comparison/equal-

### Example 1

```arturo
equal? 5 2            ; => false
equal? 5 6-1          ; => true

print 3=3             ; true
```

## `greater?`

Documentation: https://arturo-lang.io/documentation/library/comparison/greater-

### Example 1

```arturo
greater? 5 2          ; => true
greater? 5 6-1        ; => false

print 3>2             ; true
```

## `greaterOrEqual?`

Documentation: https://arturo-lang.io/documentation/library/comparison/greaterorequal-

### Example 1

```arturo
greaterOrEqual? 5 2   ; => true
greaterOrEqual? 5 4-1 ; => false

print 2>=2            ; true
```

## `less?`

Documentation: https://arturo-lang.io/documentation/library/comparison/less-

### Example 1

```arturo
less? 5 2             ; => false
less? 5 6+1           ; => true

print 2<3             ; true
```

## `lessOrEqual?`

Documentation: https://arturo-lang.io/documentation/library/comparison/lessorequal-

### Example 1

```arturo
lessOrEqual? 5 2      ; => false
lessOrEqual? 5 6-1    ; => true

print 2=<3            ; true
```

## `notEqual?`

Documentation: https://arturo-lang.io/documentation/library/comparison/notequal-

### Example 1

```arturo
notEqual? 5 2         ; => true
notEqual? 5 6-1       ; => false

print 2<>3            ; true
```

## `same?`

Documentation: https://arturo-lang.io/documentation/library/comparison/same-

### Example 1

```arturo
same? 1 2           ; => false
same? 3 3           ; => true
same? 3 3.0         ; => false
```
