# strings 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `alphabet`

Documentation: https://arturo-lang.io/documentation/library/strings/alphabet

### Example 1

```arturo
alphabet'es
; => [a b c d e f g h i j k l m n ñ o p q r s t u v w x y z]

alphabet.upper 'es
; => [A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z]

alphabet.all 'es
; => [a b c d e f g h i j k l m n ñ o p q r s t u v w x y z á é í ó ú ü]

alphabet.lower.upper.all 'es
; => [a b c d e f g h i j k l m n ñ o p q r s t u v w x y z á é í ó ú ü A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z Á É Í Ó Ú Ü]
```

## `ascii?`

Documentation: https://arturo-lang.io/documentation/library/strings/ascii-

### Example 1

```arturo
ascii? 'd'              ; true
```

### Example 2

```arturo
ascii? '😀'             ; false

ascii? "hello world"    ; true
ascii? "Hællø wœrld"    ; false
ascii? "Γειά!"          ; false
```

## `capitalize`

Documentation: https://arturo-lang.io/documentation/library/strings/capitalize

### Example 1

```arturo
print capitalize "hello World"      ; "Hello World"
```

### Example 2

```arturo
str: "hello World"
capitalize 'str                     ; str: "Hello World"
```

## `escape`

Documentation: https://arturo-lang.io/documentation/library/strings/escape

### Example 1

```arturo
str: {a long "string" + with \diffe\rent symbols.}

print escape str
; "a long \"string\" + with \\diffe\\rent symbols."

print escape.json str
; a long \"string\" + with \\diffe\\rent symbols.

print escape.regex str
; a\x20long\x20\x22string\x22\x20\x2B\x20with\x20\x5Cdiffe\x5Crent\x20symbols\x2E

print escape.shell str
; 'a long "string" + with \diffe\rent symbols.'

print escape.xml str
; a long &quot;string&quot; + with \diffe\rent symbols.
```

## `indent`

Documentation: https://arturo-lang.io/documentation/library/strings/indent

### Example 1

```arturo
str: "one\ntwo\nthree"

print indent str
;     one
;     two
;     three

print indent .n:10 .with:"#" str
; ##########one
; ##########two
; ##########three
```

## `jaro`

Documentation: https://arturo-lang.io/documentation/library/strings/jaro

### Example 1

```arturo
jaro "one" "one"        ; => 1.0

jaro "crate" "trace"    ; => 0.7333333333333334
jaro "dwayne" "duane"   ; => 0.8222222222222223

jaro "abcdef" "fedcba"  ; => 0.3888888888888888
jaro "abcde" "vwxyz"    ; => 0.0
```

## `join`

Documentation: https://arturo-lang.io/documentation/library/strings/join

### Example 1

```arturo
arr: ["one" "two" "three"]
print join arr
; onetwothree

print join.with:"," arr
; one,two,three

join 'arr
; arr: "onetwothree"
```

### Example 2

```arturo
print join ['H' 'e' 'l' 'l' 'o' '!']
; Hello!

print join @["1 + 2 = " 1+2]
; 1 + 2 = 3
```

### Example 3

```arturo
join.with:'-' ["Hello" "world"]
; => "Hello-world"
```

### Example 4

```arturo
join.words ["This" "is" "a" "sentence."]
; => "This is a sentence."
```

### Example 5

```arturo
; This example uses the universal new line character
; If you need to use carriage return for some reason, use join.with: "\\r\\n" instead.
$> join.lines ["# Recipe", "", "1. Apple", "2. Banana"]
=> # Recipe

1. Apple
2. Banana
```

## `levenshtein`

Documentation: https://arturo-lang.io/documentation/library/strings/levenshtein

### Example 1

```arturo
print levenshtein "for" "fur"         ; 1
print levenshtein "one" "one"         ; 0
```

### Example 2

```arturo
print join.with:"\n" levenshtein .align "ACTGCACTGAC" "GCATGACTAT"
; AC-TGCACTGAC
; GCATG-ACT-AT
```

## `lower`

Documentation: https://arturo-lang.io/documentation/library/strings/lower

### Example 1

```arturo
print lower "hello World, 你好!"      ; "hello world, 你好!"
```

### Example 2

```arturo
str: "hello World, 你好!"
lower 'str                           ; str: "hello world, 你好!"
```

### Example 3

```arturo
ch: 'A'
lower ch    
; => 'a'
```

## `lower?`

Documentation: https://arturo-lang.io/documentation/library/strings/lower-

### Example 1

```arturo
lower? "ñ"               ; => true
lower? "X"               ; => false
lower? "Hello World"     ; => false
lower? "hello"           ; => true
```

### Example 2

```arturo
lower? 'a'               ; => true
lower? 'A'               ; => false
```

## `match`

Documentation: https://arturo-lang.io/documentation/library/strings/match

### Example 1

```arturo
match "hello" "hello"                   ; => ["hello"]
match "x: 123, y: 456" {/[0-9]+/}       ; => ["123" "456"]
match "this is a string" {/[0-9]+/}     ; => []
```

### Example 2

```arturo
match.once "x: 123, y: 456" {/[0-9]+/}      ; => ["123"]
```

### Example 3

```arturo
match.count "some words" {/\w+/}        ; => 2
```

### Example 4

```arturo
match.capture "abc" {/(.)/}             ; => ["a" "b" "c"]

match.capture "x: 123, y: 456 - z: 789, w: 012" 
              {/\w: (\d+), \w: (\d+)/}
; => [["123" "456"] ["789" "012"]]
```

### Example 5

```arturo
inspect match.capture.named "x: 123, y: 456 - z: 789, w: 012" 
                            {/\w: (?<numA>\d+), \w: (?<numB>\d+)/}
;[ :block
;    [ :dictionary
;        numA  :		123 :string
;        numB  :		456 :string
;    ]
;    [ :dictionary
;        numA  :		789 :string
;        numB  :		012 :string
;    ]
;]
```

### Example 6

```arturo
match.bounds "hELlo wORLd" {/[A-Z]+/} 
; => [1..2 7..9]
```

### Example 7

```arturo
match.in:0..2 "hello" {/l/}             ; => ["l"]
```

## `match?`

Documentation: https://arturo-lang.io/documentation/library/strings/match-

### Example 1

```arturo
match? "hello" {/l/}            ; => true
match? "hello" {/x/}            ; => false

match? "hello" "l"              ; => true
```

### Example 2

```arturo
match?.in:0..1 "hello" {/l/}        ; => false
match?.in:2..4 "hello" {/l/}        ; => true
```

## `numeric?`

Documentation: https://arturo-lang.io/documentation/library/strings/numeric-

### Example 1

```arturo
numeric? "hello"            ; => false
numeric? "3.14"             ; => true
numeric? "18966"            ; => true
numeric? "3:5"              ; => true
numeric? "0xdeadbeef"       ; => true
numeric? "123xxy"           ; => false
```

## `outdent`

Documentation: https://arturo-lang.io/documentation/library/strings/outdent

### Example 1

```arturo
print outdent {:
    one
        two
        three
:}
; one
;     two
;     three
```

### Example 2

```arturo
print outdent.n:1 {:
    one
        two
        three
:}
;  one
;      two
;      three
```

## `pad`

Documentation: https://arturo-lang.io/documentation/library/strings/pad

### Example 1

```arturo
pad "good" 10                 ; => "      good"
pad.right "good" 10           ; => "good      "
pad.center "good" 10          ; => "   good   "
```

### Example 2

```arturo
a: "hello"
pad 'a 10                     ; a: "     hello"
```

### Example 3

```arturo
pad.with:`0` to :string 123 5   
; => 00123
```

## `prefix?`

Documentation: https://arturo-lang.io/documentation/library/strings/prefix-

### Example 1

```arturo
prefix? "hello" "he"          ; => true
prefix? "boom" "he"           ; => false
```

### Example 2

```arturo
prefix? "hello" {/\w+/}       ; => true
prefix? "world" {/\d+/}       ; => false
```

### Example 3

```arturo
prefix? "hello" 'h'           ; => true
```

## `render`

Documentation: https://arturo-lang.io/documentation/library/strings/render

### Example 1

```arturo
x: 2
greeting: "hello"
print ~"|greeting|, your number is |x|"       ; hello, your number is 2
```

## `replace`

Documentation: https://arturo-lang.io/documentation/library/strings/replace

### Example 1

```arturo
replace "hello" "l" "x"         ; => "hexxo"
```

### Example 2

```arturo
str: "hello"
replace 'str "l" "x"            ; str: "hexxo"
```

### Example 3

```arturo
replace "hello" ["h" "l"] "x"           ; => "xexxo"
replace "hello" ["h" "o"] ["x" "z"]     ; => "xellz"
```

## `strip`

Documentation: https://arturo-lang.io/documentation/library/strings/strip

### Example 1

```arturo
str: "     Hello World     "

print ["strip all:"      ">" strip str       "<"]
print ["strip leading:"  ">" strip.start str "<"]
print ["strip trailing:" ">" strip.end str   "<"]

; strip all: > Hello World < 
; strip leading: > Hello World      < 
; strip trailing: >      Hello World <
```

## `suffix?`

Documentation: https://arturo-lang.io/documentation/library/strings/suffix-

### Example 1

```arturo
suffix? "hello" "lo"          ; => true
suffix? "boom" "lo"           ; => false
```

### Example 2

```arturo
suffix? "hello" {/\w/}        ; => true
suffix? "world" {/\d/}        ; => false
```

### Example 3

```arturo
suffix? "hello" 'o'           ; => true
suffix? "world" 'o'           ; => false
```

## `translate`

Documentation: https://arturo-lang.io/documentation/library/strings/translate

### Example 1

```arturo
print translate "the brown fox jumped over the lazy dog" #[
    brown: "green" 
    fox: "wolf" 
    jumped:"flew" 
    dog:"cat"
]
; the green wolf flew over the lazy cat
```

## `truncate`

Documentation: https://arturo-lang.io/documentation/library/strings/truncate

### Example 1

```arturo
str: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse erat quam"

truncate str 30
; => "Lorem ipsum dolor sit amet, con..."

truncate.preserve str 30
; => "Lorem ipsum dolor sit amet,..."

truncate.with:"---" str 30
; => "Lorem ipsum dolor sit amet, con---"

truncate.preserve.with:"---" str 30
; => "Lorem ipsum dolor sit amet,---"
```

## `upper`

Documentation: https://arturo-lang.io/documentation/library/strings/upper

### Example 1

```arturo
print upper "hello World, 你好!"       ; "HELLO WORLD, 你好!"
```

### Example 2

```arturo
str: "hello World, 你好!"
upper 'str                           ; str: "HELLO WORLD, 你好!"
```

### Example 3

```arturo
ch: 'a'
upper ch    
; => 'A'
```

## `upper?`

Documentation: https://arturo-lang.io/documentation/library/strings/upper-

### Example 1

```arturo
upper? "Ñ"               ; => true
upper? "x"               ; => false
upper? "Hello World"     ; => false
upper? "HELLO"           ; => true
```

### Example 2

```arturo
upper? 'A'               ; => true
upper? 'a'               ; => false
```

## `whitespace?`

Documentation: https://arturo-lang.io/documentation/library/strings/whitespace-

### Example 1

```arturo
whitespace? "hello"           ; => false
whitespace? " "               ; => true
whitespace? "\n \n"           ; => true
whitespace? ""                ; => false
```

### Example 2

```arturo
whitespace? ' '               ; => true
whitespace? '\n'              ; => true
whitespace? 'a'               ; => false
```

## `wordwrap`

Documentation: https://arturo-lang.io/documentation/library/strings/wordwrap

### Example 1

```arturo
print wordwrap {Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eget mauris non justo mattis dignissim. Cras in lobortis felis, id ultricies ligula. Curabitur egestas tortor sed purus vestibulum auctor. Cras dui metus, euismod sit amet suscipit et, cursus ullamcorper felis. Integer elementum condimentum neque, et sagittis arcu rhoncus sed. In luctus congue eros, viverra dapibus mi rhoncus non. Pellentesque nisl diam, auctor quis sapien nec, suscipit aliquam velit. Nam ac nisi justo.}
; Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eget mauris non
; justo mattis dignissim. Cras in lobortis felis, id ultricies ligula. Curabitur
; egestas tortor sed purus vestibulum auctor. Cras dui metus, euismod sit amet
; suscipit et, cursus ullamcorper felis. Integer elementum condimentum neque, et
; sagittis arcu rhoncus sed. In luctus congue eros, viverra dapibus mi rhoncus
; non. Pellentesque nisl diam, auctor quis sapien nec, suscipit aliquam velit. Nam
; ac nisi justo.
```

### Example 2

```arturo
print wordwrap.at: 10 "one two three four five six seven eight nine ten"
; one two
; three four
; five six
; seven 
; eight nine
; ten
```
