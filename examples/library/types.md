# types 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `attribute?`

Documentation: https://arturo-lang.io/documentation/library/types/attribute-

### Example 1

```arturo
attribute? first [.something x]
; => true
```

## `attributeLabel?`

Documentation: https://arturo-lang.io/documentation/library/types/attributelabel-

### Example 1

```arturo
attributeLabel? first [.something: x]
; => true
```

## `binary?`

Documentation: https://arturo-lang.io/documentation/library/types/binary-

### Example 1

```arturo
binary? to :binary "string"
; => true
```

## `block?`

Documentation: https://arturo-lang.io/documentation/library/types/block-

### Example 1

```arturo
print block? [1 2 3]            ; true
print block? #[name: "John"]    ; false
print block? "hello"            ; false
print block? 123                ; false
```

## `bytecode?`

Documentation: https://arturo-lang.io/documentation/library/types/bytecode-

### Example 1

```arturo
code: [print 1 + 2]
bcode: to :bytecode code

print bytecode? bcode      ; true
print bytecode? code       ; false
```

## `char?`

Documentation: https://arturo-lang.io/documentation/library/types/char-

### Example 1

```arturo
print char? 'a'         ; true
print char? 123         ; false
```

## `color?`

Documentation: https://arturo-lang.io/documentation/library/types/color-

### Example 1

```arturo
print color? #FF0000        ; true
print color? #green         ; true

print color? 123            ; false
```

## `complex?`

Documentation: https://arturo-lang.io/documentation/library/types/complex-

### Example 1

```arturo
c: to :complex [1 2]
print complex? c            ; true

print complex? 123          ; false
```

## `constructor`

Documentation: https://arturo-lang.io/documentation/library/types/constructor

### Example 1

```arturo
define :cat [
    init: constructor [nick :string]

    meow: method [][
        print [this\nick ":" "'meow!'"
    ]
]

snowflake: to :cat [15]
; Assertion | [is? :string nick]
;     error |

snowflake: to :cat ["Snowflake"]
snowflake\meow
; Snowflake: 'meow!'
```

## `database?`

Documentation: https://arturo-lang.io/documentation/library/types/database-

### Example 1

```arturo
database? open "my.db"
; => true
```

## `date?`

Documentation: https://arturo-lang.io/documentation/library/types/date-

### Example 1

```arturo
print date? now             ; true
print date? "hello"         ; false
```

## `define`

Documentation: https://arturo-lang.io/documentation/library/types/define

### Example 1

```arturo
; define a simple type
define :person [name surname]

; and create an object
someone: to :person ["John" "Doe"]
print someone       ; [name:John surname:Doe]
```

### Example 2

```arturo
; define a simple type
define :person [name surname]

; and create an object
; using a dictionary with field values
someone: to :person #[surname: "Doe", name: "John"]
print someone       ; [name:John surname:Doe]
```

### Example 3

```arturo
; define a new type
; with custom constructor

define :person [
    init: method [name, surname, age][
        this\name: name
        this\surname: surname
        this\dob: now\year - age
    ]
]

; create an object
jd: to :person ["John" "Doe" 38]
print jd            ; [name:John surname:Doe dob:1986]
```

### Example 4

```arturo
; define type with overloaded
; magic methods
define :natural [
    init: constructor [value]

    ; custom `+` overload
    add: method [x :integer :natural][
        (integer? x)? -> this\value + x
                      -> to :natural @[this\value + x\value]
    ]

    ; custom `to :string` overload
    string: method [][
        to :string this\value
    ]
]

; create two new 'natural' numbers
n1: to :natural @[3]
n2: to :natural @[5]

print n1 + n2           ; 8
```

## `defined?`

Documentation: https://arturo-lang.io/documentation/library/types/defined-

### Example 1

```arturo
defined? :cat
; => false
defined? "cat"
; => false
defined? 'cat
; => false

define :cat [
    init: constructor [name :string age :integer]
]

defined? :cat
; => true
defined? "cat"
; => true
defined? 'cat
; => true

defined? :dog
; => false
```

## `dictionary?`

Documentation: https://arturo-lang.io/documentation/library/types/dictionary-

### Example 1

```arturo
print dictionary? #[name: "John"]   ; true
print dictionary? 123               ; false
```

## `error?`

Documentation: https://arturo-lang.io/documentation/library/types/error-

### Example 1

```arturo
error? try -> throw "Some Error"
; => true
```

## `errorKind?`

Documentation: https://arturo-lang.io/documentation/library/types/errorkind-

### Example 1

```arturo
errorKind? to :errorKind "Some error kind"
; => true
errorKind? genericError
; => true
```

## `floating?`

Documentation: https://arturo-lang.io/documentation/library/types/floating-

### Example 1

```arturo
print floating? 3.14        ; true
print floating? 123         ; false
print floating? "hello"     ; false
```

## `function?`

Documentation: https://arturo-lang.io/documentation/library/types/function-

### Example 1

```arturo
print function? $[x][2*x]       ; true
print function? var 'print      ; true
print function? "print"         ; false
print function? 123             ; false
```

### Example 2

```arturo
f: function [x][x+2]

function? var'f                 ; => true
function? var'print             ; => true
function?.builtin var'f         ; => false
function?.builtin var'print     ; => true
```

## `inline?`

Documentation: https://arturo-lang.io/documentation/library/types/inline-

### Example 1

```arturo
inline? first [(something) x]
; => true
```

## `integer?`

Documentation: https://arturo-lang.io/documentation/library/types/integer-

### Example 1

```arturo
print integer? 123                  ; true
print integer? "hello"              ; false
```

### Example 2

```arturo
integer?.big 123                    ; => false
integer?.big 12345678901234567890   ; => true
```

## `is`

Documentation: https://arturo-lang.io/documentation/library/types/is

### Example 1

```arturo
define :animal [
    init: constructor [nick :string age :integer]
    
    speak: method [][
        print "..."
    ]
]

define :fish is :animal []

define :cat is :animal [
    speak: method [][
        print [~"|this\nick|:" "'meow!'"]
    ] 
]                                                   

a: to :cat []
; >> Runtime | cannot initialize object of type :cat
;      error | wrong number of parameters: 0
;            | expected: 2 (nick, age)

scooby: to :animal ["Scooby" 7]
scooby\speak
; ...

bubble: to :fish ["Bubble" 1]            
bubble\speak
; ...

snowflake: to :cat ["Snowflake" 3]
snowflake\speak
; Snowflake: 'meow!'
```

## `is?`

Documentation: https://arturo-lang.io/documentation/library/types/is-

### Example 1

```arturo
is? :string "hello"       ; => true
is? :block [1 2 3]        ; => true
is? :integer "boom"       ; => false

is? [:string] ["one" "two"]     ; => true
is? [:integer] [1 "two]         ; => false
```

## `label?`

Documentation: https://arturo-lang.io/documentation/library/types/label-

### Example 1

```arturo
label? first [something: x]
; => true
```

## `literal?`

Documentation: https://arturo-lang.io/documentation/library/types/literal-

### Example 1

```arturo
print literal? 'x           ; true
print literal? "x"          ; false
print literal? 123          ; false
```

## `logical?`

Documentation: https://arturo-lang.io/documentation/library/types/logical-

### Example 1

```arturo
print logical? true         ; true
print logical? false        ; true
print logical? maybe        ; true
```

### Example 2

```arturo
print logical? 1=1          ; true
print logical? 123          ; false
```

## `method?`

Documentation: https://arturo-lang.io/documentation/library/types/method-

### Example 1

```arturo
greet: method [name :string][print ~"How are you, |name|?"]
reply: function [name :string][print ~"Hi, I'm fine |name|!"]

method? greet
; => true

method? reply
; => false
```

## `null?`

Documentation: https://arturo-lang.io/documentation/library/types/null-

### Example 1

```arturo
print null? null            ; true
print null? ø               ; true

print null? 123             ; false
```

## `object?`

Documentation: https://arturo-lang.io/documentation/library/types/object-

### Example 1

```arturo
define :person [name,surname][]

x: to :person ["John","Doe"]

print object? x             ; true
print object? "hello"       ; false
```

## `path?`

Documentation: https://arturo-lang.io/documentation/library/types/path-

### Example 1

```arturo
path? first [a\b\c x]
; => true
```

## `pathLabel?`

Documentation: https://arturo-lang.io/documentation/library/types/pathlabel-

### Example 1

```arturo
pathLabel? first [a\b\c: x]
; => true
```

## `pathLiteral?`

Documentation: https://arturo-lang.io/documentation/library/types/pathliteral-

### Example 1

```arturo
pathLiteral? 'a\b\c
; => true
```

## `quantity?`

Documentation: https://arturo-lang.io/documentation/library/types/quantity-

### Example 1

```arturo
print quantity? 1:m         ; true
print quantity? 2:yd2       ; true    

print quantity? 3           ; false
```

## `range?`

Documentation: https://arturo-lang.io/documentation/library/types/range-

### Example 1

```arturo
r: 1..3                     ; r: [1 2 3]

print range? r              ; true
print range? [1 2 3]        ; false
```

## `rational?`

Documentation: https://arturo-lang.io/documentation/library/types/rational-

### Example 1

```arturo
r: to :rational 3.14        ; r: 157/50

print rational? r           ; true
print rational? 3.14        ; false
```

## `regex?`

Documentation: https://arturo-lang.io/documentation/library/types/regex-

### Example 1

```arturo
print regex? {/[a-z]+/}     ; true
print regex? "[a-z]+"       ; false
print regex? 123            ; false
```

## `socket?`

Documentation: https://arturo-lang.io/documentation/library/types/socket-

### Example 1

```arturo
server: listen 18966
socket? server
; => true
```

## `sortable`

Documentation: https://arturo-lang.io/documentation/library/types/sortable

### Example 1

```arturo
define :cat [
    init: constructor [name :string age :integer]
    compare: sortable 'age
]

snowflake: to :cat ["Snowflake" 3]
smith: to :cat ["Smith" 6]

compare snowflake smith
; => -1
snowflake < smith
; => true
```

## `store?`

Documentation: https://arturo-lang.io/documentation/library/types/store-

### Example 1

```arturo
store? config
; => true
```

## `string?`

Documentation: https://arturo-lang.io/documentation/library/types/string-

### Example 1

```arturo
print string? "x"           ; true
print string? 'x            ; false
print string? 123           ; false
```

## `symbol?`

Documentation: https://arturo-lang.io/documentation/library/types/symbol-

### Example 1

```arturo
symbol? first [+ x]
; => true
```

## `symbolLiteral?`

Documentation: https://arturo-lang.io/documentation/library/types/symbolliteral-

### Example 1

```arturo
symbolLiteral? '++
; => true
```

## `to`

Documentation: https://arturo-lang.io/documentation/library/types/to

### Example 1

```arturo
to :integer "2020"            ; 2020

to :integer 'A'               ; 65
to :char 65                   ; 'A'

to :integer 4.3               ; 4
to :floating 4                ; 4.0

to :complex [1 2]             ; 1.0+2.0i

; make sure you're using the `array` (`@`) converter here, since `neg` must be evaluated first
to :complex @[2.3 neg 4.5]    ; 2.3-4.5i

to :rational [1 2]            ; 1/2
to :rational @[neg 3 5]       ; -3/5

to :boolean 0                 ; false
to :boolean 1                 ; true
to :boolean "true"            ; true

to :literal "symbol"          ; 'symbol
```

### Example 2

```arturo
to :string 2020               ; "2020"
to :string 'symbol            ; "symbol"
to :string :word              ; "word"

to :string .format:"dd/MM/yy" now
; 22/03/21

to :string .format:".2f" 123.12345
; 123.12
```

### Example 3

```arturo
to :block "one two three"       ; [one two three]

do to :block "print 123"        ; 123
```

### Example 4

```arturo
to :date 0          ; => 1970-01-01T01:00:00+01:00

print now           ; 2021-05-22T07:39:10+02:00
to :integer now     ; => 1621661950

to :date .format:"dd/MM/yyyy" "22/03/2021"
; 2021-03-22T00:00:00+01:00
```

### Example 5

```arturo
to [:string] [1 2 3 4]
; ["1" "2" "3" "4"]

to [:char] "hello"
; ['h' 'e' 'l' 'l' 'o']
```

### Example 6

```arturo
define :person [name surname age][]

to :person ["John" "Doe" 35]
; [name:John surname:Doe age:35]
```

### Example 7

```arturo
to :color [255 0 10]
; => #FF000A

to :color .hsl [255 0.2 0.4]
; => #5C527A
```

## `type`

Documentation: https://arturo-lang.io/documentation/library/types/type

### Example 1

```arturo
print type 18966          ; :integer
print type "hello world"  ; :string
```

## `type?`

Documentation: https://arturo-lang.io/documentation/library/types/type-

### Example 1

```arturo
print type? :string         ; true
print type? "string"        ; false
print type? 123             ; false
```

## `unit?`

Documentation: https://arturo-lang.io/documentation/library/types/unit-

### Example 1

```arturo
unit? `m
; => true
```

## `version?`

Documentation: https://arturo-lang.io/documentation/library/types/version-

### Example 1

```arturo
print version? 1.0.2        ; true
print version? "1.0.2"      ; false
```

## `word?`

Documentation: https://arturo-lang.io/documentation/library/types/word-

### Example 1

```arturo
word? first [something x]
; => true
```
