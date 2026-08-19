# reflection 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `arity`

Documentation: https://arturo-lang.io/documentation/library/reflection/arity

### Example 1

```arturo
print arity\print   ; 1
```

## `attr`

Documentation: https://arturo-lang.io/documentation/library/reflection/attr

### Example 1

```arturo
multiply: function [x][
    switch attr? "with" 
        -> x * attr "with"
        -> 2*x 
]

print multiply 5
; 10

print multiply.with: 6 5
; 30
```

## `attr?`

Documentation: https://arturo-lang.io/documentation/library/reflection/attr-

### Example 1

```arturo
greet: function [x][
    switch attr? 'later
      -> ~"|x| I'm afraid, I'll greet you later"
      -> ~"Hello, |x|!"
]

greet "John"
; => Hello, John!

greet.later "John"
; => John I'm afraid, I'll greet you later!

; Have in mind that `attr?` won't pop your attribute's stack

greet "Joe"
; => Joe I'm afraid, I'll greet you later!
```

## `attrs`

Documentation: https://arturo-lang.io/documentation/library/reflection/attrs

### Example 1

```arturo
greet: function [x][
    print ["Hello" x "!"]
    print attrs
]

greet.later "John"

; Hello John!
; [
;    later:    true
; ]
```

## `benchmark`

Documentation: https://arturo-lang.io/documentation/library/reflection/benchmark

### Example 1

```arturo
benchmark [ 
    ; some process that takes some time
    loop 1..10000 => prime? 
]

; [benchmark] time: 0.065s
```

### Example 2

```arturo
benchmark.get [
    loop 1..10000 => prime?
]
; => 0.3237628936767578
```

## `info`

Documentation: https://arturo-lang.io/documentation/library/reflection/info

### Example 1

```arturo
info 'print

; |--------------------------------------------------------------------------------
; |          print  :function                                                   Io
; |--------------------------------------------------------------------------------
; |                 print given value to screen with newline
; |--------------------------------------------------------------------------------
; |          usage  print value :any
; |
; |        options  .lines -> print each value in block in a new line
; |
; |        returns  :nothing
; |--------------------------------------------------------------------------------
```

### Example 2

```arturo
info '++

; |--------------------------------------------------------------------------------
; |         append  :function                                          0x107555A10
; |          alias  ++
; |--------------------------------------------------------------------------------
; |                 append value to given collection
; |--------------------------------------------------------------------------------
; |          usage  append collection :char :string :literal :block
; |                        value :any
; |
; |        returns  :string :block :nothing
; |--------------------------------------------------------------------------------
```

### Example 3

```arturo
print info.get 'print
; [name:print address:0x1028B3410 type::function module:Io args:[value:[:any]] attrs:[] returns:[:nothing] description:print given value to screen with newline example:print "Hello world!"          ; Hello world!]
```

## `inspect`

Documentation: https://arturo-lang.io/documentation/library/reflection/inspect

### Example 1

```arturo
inspect 3                 ; 3 :integer

a: "some text"
inspect a                 ; some text :string
```

## `methods`

Documentation: https://arturo-lang.io/documentation/library/reflection/methods

### Example 1

```arturo
define :cat [
    init: method [nick][
        this\nick: join.with: " " @["Mr." capitalize nick]
    ]

    meow: method [][
        print [this\nick ":" "'meow!'"]
    ]
]

snowflake: to :cat ["snowflake"]
methods snowflake
; => [init meow]
```

## `stack`

Documentation: https://arturo-lang.io/documentation/library/reflection/stack

### Example 1

```arturo
1 2 3 "done"

print stack
; 1 2 3 done
```

## `standalone?`

Documentation: https://arturo-lang.io/documentation/library/reflection/standalone-

### Example 1

```arturo
doSomething: function [x][
    print ["I'm doing something with" x]
]

if standalone? [
    print "It's running from command line and not included."
    print "Nothing to do!"
]
```

## `symbols`

Documentation: https://arturo-lang.io/documentation/library/reflection/symbols

### Example 1

```arturo
a: 2
b: "hello"

print symbols

; [
;    a: 2
;    b: "hello"
;_]
```
