# io 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `clear`

Documentation: https://arturo-lang.io/documentation/library/io/clear

### Example 1

```arturo
clear             ; (clears the screen)
```

## `color`

Documentation: https://arturo-lang.io/documentation/library/io/color

### Example 1

```arturo
print color #green "Hello!"                ; Hello! (in green)
print color #red.bold "Some text"          ; Some text (in red/bold)
```

## `cursor`

Documentation: https://arturo-lang.io/documentation/library/io/cursor

### Example 1

```arturo
cursor false    ; (hides the cursor)
cursor true     ; (shows the cursor)
```

## `goto`

Documentation: https://arturo-lang.io/documentation/library/io/goto

### Example 1

```arturo
goto 10 15      ; (move cursor to column 10, line 15)
goto 10 ø       ; (move cursor to column 10, same line)
```

## `input`

Documentation: https://arturo-lang.io/documentation/library/io/input

### Example 1

```arturo
name: input "What is your name? "
; (user enters his name: Bob)

print ["Hello" name "!"]
; Hello Bob!
```

### Example 2

```arturo
; creating a simple REPL
while [true][ 
    inp: input.repl 
              .history: "myhistory.txt"
              .complete:["Hello there", "Hello world!"] 
              .hint:#[he: "perhaps you want to say hello?"] 
              "## "

    print ["got:" inp] 
]
; will show a REPL-like interface, with arrow navigation enabled
; show previous entries with arrow-up, store entries in
; a recoverable file and also use autocompletions and hints
; based on give reference
```

### Example 3

```arturo
character: input ø
; (User types a key, for example "A")
print character
; A
```

## `print`

Documentation: https://arturo-lang.io/documentation/library/io/print

### Example 1

```arturo
print "Hello world!"          ; Hello world!
```

### Example 2

```arturo
print.lines [1 2 3]
; 1
; 2
; 3
```

### Example 3

```arturo
print.lines map.iterator 1..3 'x -> x+1
; 2
; 3
; 4
```

## `prints`

Documentation: https://arturo-lang.io/documentation/library/io/prints

### Example 1

```arturo
prints "Hello "
prints "world"
print "!"             

; Hello world!
```

## `terminal`

Documentation: https://arturo-lang.io/documentation/library/io/terminal

### Example 1

```arturo
print terminal      ; [width:107 height:34]
terminal\width      ; => 107
```
