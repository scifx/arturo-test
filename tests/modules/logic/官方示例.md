# logic 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `all?`

Documentation: https://arturo-lang.io/documentation/library/logic/all-

### Example 1

```arturo
if all? @[2>1 "DONE"=upper "done" true] 
    -> print "yes, all are true"
; yes, all are true
```

### Example 2

```arturo
print all? @[true false true true]
; false
```

### Example 3

```arturo
all? []
; => true
```

## `and?`

Documentation: https://arturo-lang.io/documentation/library/logic/and-

### Example 1

```arturo
x: 2
y: 5

if and? x=2 y>5 [
    print "yep, that's correct!"]
]

; yep, that's correct!
```

## `any?`

Documentation: https://arturo-lang.io/documentation/library/logic/any-

### Example 1

```arturo
if any? @[false 3=4 2>1] 
    -> print "yes, one (or more) of the values is true"
; yes, one (or more) of the values is true
```

### Example 2

```arturo
print any? @[false false false]
; false
```

## `false`

Documentation: https://arturo-lang.io/documentation/library/logic/false

### Example 1

```arturo

```

## `false?`

Documentation: https://arturo-lang.io/documentation/library/logic/false-

### Example 1

```arturo
print false? 1 = 2          ; true
print false? 1 <> 2         ; false
print false? odd? 2         ; true

print false? [1 2 3]        ; false
```

## `maybe`

Documentation: https://arturo-lang.io/documentation/library/logic/maybe

### Example 1

```arturo

```

## `nand?`

Documentation: https://arturo-lang.io/documentation/library/logic/nand-

### Example 1

```arturo
x: 2
y: 3

switch nand? x=2 y=3 
    -> print "yep, that's correct!"
    -> print "nope, that's not correct

; nope, that's not correct
```

## `nor?`

Documentation: https://arturo-lang.io/documentation/library/logic/nor-

### Example 1

```arturo
x: 2
y: 3

switch nor? x>2 y=3
    -> print "yep, that's correct!"
    -> print "nope, that's not correct

; nope, that's not correct
```

## `not?`

Documentation: https://arturo-lang.io/documentation/library/logic/not-

### Example 1

```arturo
ready: false
if not? ready [
    print "we're still not ready!"
]

; we're still not ready!
```

## `or?`

Documentation: https://arturo-lang.io/documentation/library/logic/or-

### Example 1

```arturo
x: 2
y: 4

if or? x=2 y>5 [
    print "yep, that's correct!"
]

; yep, that's correct!
```

## `true`

Documentation: https://arturo-lang.io/documentation/library/logic/true

### Example 1

```arturo

```

## `true?`

Documentation: https://arturo-lang.io/documentation/library/logic/true-

### Example 1

```arturo
print true? 1 = 2           ; false
print true? 1 <> 2          ; true
print true? even? 2         ; true

print true? [1 2 3]         ; false
```

## `xnor?`

Documentation: https://arturo-lang.io/documentation/library/logic/xnor-

### Example 1

```arturo
x: 2
y: 3

switch xnor? x=2 y=3
    -> print "yep, that's correct!"
    -> print "nope, that's not correct

; yep, that's correct!
```

## `xor?`

Documentation: https://arturo-lang.io/documentation/library/logic/xor-

### Example 1

```arturo
x: 2
y: 3

switch xor? x=2 y=3
    -> print "yep, that's correct!"
    -> print "nope, that's not correct

; nope, that's not correct
```
