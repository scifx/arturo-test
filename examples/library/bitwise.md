# bitwise 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `and`

Documentation: https://arturo-lang.io/documentation/library/bitwise/and

### Example 1

```arturo
print and 2 3      ; 2
```

### Example 2

```arturo
a: 2
and 'a 3           ; a: 2
```

## `nand`

Documentation: https://arturo-lang.io/documentation/library/bitwise/nand

### Example 1

```arturo
print nand 2 3     ; -3
```

### Example 2

```arturo
a: 2
nand 'a 3          ; a: -3
```

## `nor`

Documentation: https://arturo-lang.io/documentation/library/bitwise/nor

### Example 1

```arturo
print nor 2 3      ; -4
```

### Example 2

```arturo
a: 2
nor 'a 3           ; a: -4
```

## `not`

Documentation: https://arturo-lang.io/documentation/library/bitwise/not

### Example 1

```arturo
print not 123      ; -124
```

### Example 2

```arturo
a: 123
not 'a             ; a: -124
```

## `or`

Documentation: https://arturo-lang.io/documentation/library/bitwise/or

### Example 1

```arturo
print or 2 3       ; 3
```

### Example 2

```arturo
a: 2
or 'a 3            ; a: 3
```

## `shl`

Documentation: https://arturo-lang.io/documentation/library/bitwise/shl

### Example 1

```arturo
print shl 2 3      ; 16
```

### Example 2

```arturo
a: 2
shl 'a 3           ; a: 16
```

## `shr`

Documentation: https://arturo-lang.io/documentation/library/bitwise/shr

### Example 1

```arturo
print shr 16 3     ; 2
```

### Example 2

```arturo
a: 16
shr 'a 3           ; a: 2
```

## `xnor`

Documentation: https://arturo-lang.io/documentation/library/bitwise/xnor

### Example 1

```arturo
print xnor 2 3     ; -2
```

### Example 2

```arturo
a: 2
xnor 'a 3          ; a: -2
```

## `xor`

Documentation: https://arturo-lang.io/documentation/library/bitwise/xor

### Example 1

```arturo
print xor 2 3      ; 1
```

### Example 2

```arturo
a: 2
xor 'a 3           ; a: 1
```
