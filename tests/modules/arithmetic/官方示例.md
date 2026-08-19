# arithmetic 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `add`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/add

### Example 1

```arturo
print add 1 2      ; 3
print 1 + 3        ; 4
```

### Example 2

```arturo
a: 4
add 'a 1           ; a: 5
```

### Example 3

```arturo
; adding a time quantity to a date gives us a new date
print (to :date "2021-03-22T11:25:30+01:00") + 3`days
; 2021-03-25T11:25:30+01:00
```

## `dec`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/dec

### Example 1

```arturo
print dec 5        ; 4
```

### Example 2

```arturo
a: 4
dec 'a             ; a: 3
```

## `div`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/div

### Example 1

```arturo
print div 5 2      ; 2
print 9 / 3        ; 3
```

### Example 2

```arturo
a: 6
div 'a 3           ; a: 2
```

## `divmod`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/divmod

### Example 1

```arturo
print divmod 15 5       ; 3 0
print 14 /% 3           ; 4 2
```

### Example 2

```arturo
[q,r]: 10 /% 3          ; q: 3, r: 1
```

### Example 3

```arturo
a: 6
divmod 'a 4             ; a: [1, 2]
```

## `fdiv`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/fdiv

### Example 1

```arturo
print fdiv 5 2     ; 2.5
print 5 // 2       ; 2.5
```

### Example 2

```arturo
a: 6
fdiv 'a 3          ; a: 2.0
```

## `inc`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/inc

### Example 1

```arturo
print inc 5        ; 6
```

### Example 2

```arturo
a: 4
inc 'a             ; a: 5
```

## `mod`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/mod

### Example 1

```arturo
print mod 5 2      ; 1
print 9 % 3        ; 0
```

### Example 2

```arturo
a: 8
mod 'a 3           ; a: 2
```

## `mul`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/mul

### Example 1

```arturo
print mul 1 2      ; 2
print 2 * 3        ; 6
```

### Example 2

```arturo
a: 5
mul 'a 2           ; a: 10
```

## `neg`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/neg

### Example 1

```arturo
print neg 1        ; -1
```

### Example 2

```arturo
a: 5
neg 'a             ; a: -5
```

## `pow`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/pow

### Example 1

```arturo
print pow 2 3      ; 8
print 3 ^ 2        ; 9
```

### Example 2

```arturo
a: 5
pow 'a 2           ; a: 25
```

## `sub`

Documentation: https://arturo-lang.io/documentation/library/arithmetic/sub

### Example 1

```arturo
print sub 2 1      ; 1
print 5 - 3        ; 2
```

### Example 2

```arturo
a: 7
sub 'a 2           ; a: 5
```

### Example 3

```arturo
; subtracting two dates gives us the elapsed time, as a quantity
d1: to :date "1995-02-03T12:00:00+08:00"
d2: to :date "2025-06-09T12:00:00+08:00"
print (d2 - d1) --> `day
; 11084.0`day
```
