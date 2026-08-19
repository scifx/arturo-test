# exceptions 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `arithmeticError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/arithmeticerror

### Example 1

```arturo

```

## `assertionError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/assertionerror

### Example 1

```arturo

```

## `conversionError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/conversionerror

### Example 1

```arturo

```

## `indexError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/indexerror

### Example 1

```arturo

```

## `libraryError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/libraryerror

### Example 1

```arturo

```

## `nameError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/nameerror

### Example 1

```arturo

```

## `packageError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/packageerror

### Example 1

```arturo

```

## `runtimeError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/runtimeerror

### Example 1

```arturo

```

## `syntaxError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/syntaxerror

### Example 1

```arturo

```

## `systemError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/systemerror

### Example 1

```arturo

```

## `throw`

Documentation: https://arturo-lang.io/documentation/library/exceptions/throw

### Example 1

```arturo
err: try -> throw "Page not found"
err\kind
; => Generic Error
err\message
; => Page not found

; or you can alternatively use custom errorKind

pageNotFound: to :errorKind "404: Page not Found"

err: try -> throw.as: pageNotFound "Seems that the page does not exist"
err\kind
; => 404: Page not Found
err\message
; => Seems that the page does not exist

; Or even use the :errorKind's label as the message itself

err: try -> throw pageNotFound
err\kind
; => 404: Page not Found
err\message
; => 404: Page not Found
```

## `throws?`

Documentation: https://arturo-lang.io/documentation/library/exceptions/throws-

### Example 1

```arturo
throws? [
    1 + 2
] 
; => false

throws? -> 1/0
; => true
```

## `try`

Documentation: https://arturo-lang.io/documentation/library/exceptions/try

### Example 1

```arturo
err: try [
    ; let's try something dangerous
    print 10 / 0
]

type err
; => :error

; Tips: mixing errors and returned values

f: $[][ throw "some error" ]
g: $[][ return "hi" ]

(genericError = err: <= try -> val: f)?
    -> print err
    -> print val
; => Generic Error: some error

(genericError = err: <= try -> val: g)?
    -> print err
    -> print val
; => hi
```

## `typeError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/typeerror

### Example 1

```arturo

```

## `uiError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/uierror

### Example 1

```arturo

```

## `valueError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/valueerror

### Example 1

```arturo

```

## `vmError`

Documentation: https://arturo-lang.io/documentation/library/exceptions/vmerror

### Example 1

```arturo

```
