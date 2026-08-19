# colors 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `blend`

Documentation: https://arturo-lang.io/documentation/library/colors/blend

### Example 1

```arturo
blend #red #CCCCCC                  ; => #E66666
```

### Example 2

```arturo
blend .balance: 0.75 #red #CCCCCC   
; => #D99999
```

## `darken`

Documentation: https://arturo-lang.io/documentation/library/colors/darken

### Example 1

```arturo
darken #red 0.2         ; => #CC0000
darken #red 0.5         ; => #7F0000

darken #9944CC 0.3      ; => #6B308F
```

## `desaturate`

Documentation: https://arturo-lang.io/documentation/library/colors/desaturate

### Example 1

```arturo
desaturate #red 0.2         ; => #E61919
desaturate #red 0.5         ; => #BF4040

desaturate #9944CC 0.3      ; => #9558B8
```

## `grayscale`

Documentation: https://arturo-lang.io/documentation/library/colors/grayscale

### Example 1

```arturo
grayscale #red              ; => #808080
grayscale #green            ; => #404040

grayscale #FF44CC           ; => #A2A2A2
```

## `invert`

Documentation: https://arturo-lang.io/documentation/library/colors/invert

### Example 1

```arturo
print #orange               ; #FFA500

invert #orange              ; => #0059FF
```

## `lighten`

Documentation: https://arturo-lang.io/documentation/library/colors/lighten

### Example 1

```arturo
print #lightblue            ; #ADD8E6

lighten #lightblue 0.2      ; => #D0FFFF
lighten #lightblue 0.5      ; => #FFFFFF

lighten #9944CC 0.3         ; => #C758FF
```

## `palette`

Documentation: https://arturo-lang.io/documentation/library/colors/palette

### Example 1

```arturo
palette.triad #red      ; => [#FF0000 #00FF00 #0000FF]
palette.tetrad #red     ; => [#FF0000 #80FF00 #00FFFF #7F00FF]
```

### Example 2

```arturo
palette.split #red      ; => [#FF0000 #CCFF00 #0066FF]
```

### Example 3

```arturo
palette.monochrome #red
; => [#FF0000 #D40000 #AA0000 #7F0000 #550000 #2A0000]

palette.monochrome.size:10 #red
; => [#FF0000 #E50000 #CC0000 #B20000 #990000 #7F0000 #660000 #4C0000 #330000 #190000]
```

### Example 4

```arturo
palette.analogous #red
; => [#FF0099 #FF0066 #FF0033 #FF0000 #FF3300 #FF6600]

palette.analogous.size:10 #red
; => [#FF00FF #FF00CC #FF0099 #FF0066 #FF0033 #FF0000 #FF3300 #FF6600 #FF9900 #FFCC00]
```

### Example 5

```arturo
palette.random #red
; => [#FF0000 #00EC00 #0000D2 #00F000 #0000FF #00FF00]

palette.random.size:10 #red
; => [#FF0000 #00FF00 #0000FF #00FE00 #F30000 #00FD00 #0000ED #EC0000 #00F800 #0000D8]
```

## `saturate`

Documentation: https://arturo-lang.io/documentation/library/colors/saturate

### Example 1

```arturo
print #lightblue            ; #ADD8E6

saturate #lightblue 0.2     ; => #A7DBEC
saturate #lightblue 0.5     ; => #9FDFF4

saturate #9944CC 0.3        ; => #A030E0
```

## `spin`

Documentation: https://arturo-lang.io/documentation/library/colors/spin

### Example 1

```arturo
spin #red 90            ; => #80FF00
spin #red 180           ; => #00FFFF

spin #123456 45         ; => #231256
spin #123456 360        ; => #123456
```
