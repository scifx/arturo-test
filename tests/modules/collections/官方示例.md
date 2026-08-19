# collections 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `append`

Documentation: https://arturo-lang.io/documentation/library/collections/append

### Example 1

```arturo
append "hell" "o"         ; => "hello"
append [1 2 3] 4          ; => [1 2 3 4]
append [1 2 3] [4 5]      ; => [1 2 3 4 5]
```

### Example 2

```arturo
print "hell" ++ "o!"      ; hello!
print [1 2 3] ++ [4 5]    ; [1 2 3 4 5]
```

### Example 3

```arturo
a: "hell"
append 'a "o"
print a                   ; hello
```

### Example 4

```arturo
b: [1 2 3]
'b ++ 4
print b                   ; [1 2 3 4]
```

## `array`

Documentation: https://arturo-lang.io/documentation/library/collections/array

### Example 1

```arturo
none: @[]               ; none: []
a: @[1 2 3]             ; a: [1 2 3]

b: 5
c: @[b b+1 b+2]         ; c: [5 6 7]

d: @[
    3+1
    print "we are in the block"
    123
    print "yep"
]
; we are in the block
; yep
; => [4 123]
```

### Example 2

```arturo
; initializing empty array with initial value
x: array.of: 2 "done"
inspect.muted x
; [ :block
;     done :string
;     done :string
; ]
```

### Example 3

```arturo
; initializing empty n-dimensional array with initial value
x: array.of: [3 4] 0          ; initialize a 3x4 2D array
                                ; with zeros
; => [[0 0 0 0] [0 0 0 0] [0 0 0 0]]
```

## `chop`

Documentation: https://arturo-lang.io/documentation/library/collections/chop

### Example 1

```arturo
chop "hellox"               ; => "hello"
chop chop "hellox"          ; => "hell"
```

### Example 2

```arturo
str: "some text"
chop.times:5 str            ; => some
chop.times: neg 5 str       ; => text
```

### Example 3

```arturo
arr: @1..10
chop.times:3 'arr
arr                         ; => [1 2 3 4 5 6 7]
```

### Example 4

```arturo
chop [1 2 3]                ; => [1 2]
```

### Example 5

```arturo
chop.times:1 [1 2 3]        ; => [1 2]
chop.times:2 [1 2 3]        ; => [1]
chop.times:3 [1 2 3]        ; => []
chop.times:4 [1 2 3]        ; => []
```

### Example 6

```arturo
chop.times: neg 1 [1 2 3]   ; => [2 3]
chop.times: neg 2 [1 2 3]   ; => [3]
```

## `combine`

Documentation: https://arturo-lang.io/documentation/library/collections/combine

### Example 1

```arturo
combine [A B C]
; => [[A B C]]

combine.repeated [A B C]
; => [[A A A] [A A B] [A A C] [A B B] [A B C] [A C C] [B B B] [B B C] [B C C] [C C C]]
```

### Example 2

```arturo
combine.by:2 [A B C]
; => [[A B] [A C] [B C]]

combine.repeated.by:2 [A B C]
; => [[A A] [A B] [A C] [B B] [B C] [C C]]

combine.repeated.by: 3 [A B]
; => [[A A A] [A A B] [A B B] [B B B]]
```

### Example 3

```arturo
combine.count [A B C]
; => 1

combine.count.repeated.by:2 [A B C]
; => 6
```

## `contains?`

Documentation: https://arturo-lang.io/documentation/library/collections/contains-

### Example 1

```arturo
arr: [1 2 3 4]

contains? arr 5             ; => false
contains? arr 2             ; => true
```

### Example 2

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

contains? dict "John"       ; => true
contains? dict "Paul"       ; => false

contains? keys dict "name"  ; => true
```

### Example 3

```arturo
contains? "hello" "x"       ; => false
contains? "hello" `h`       ; => true
```

### Example 4

```arturo
contains?.at:1 "hello" "el" ; => true
contains?.at:4 "hello" `o`  ; => true
```

### Example 5

```arturo
print contains?.at:2 ["one" "two" "three"] "two"
; false

print contains?.at:1 ["one" "two" "three"] "two"
; true
```

### Example 6

```arturo
print contains?.deep [1 2 4 [3 4 [5 6] 7] 8 [9 10]] 6
; true
```

### Example 7

```arturo
user: #[ 
    name: "John" surname: "Doe"
    mom: #[ name: "Jane" surname: "Doe" ]
]

print contains?.deep user "Jane"
; true
```

## `couple`

Documentation: https://arturo-lang.io/documentation/library/collections/couple

### Example 1

```arturo
couple ["one" "two" "three"] [1 2 3]
; => [[1 "one"] [2 "two"] [3 "three"]]
```

## `decouple`

Documentation: https://arturo-lang.io/documentation/library/collections/decouple

### Example 1

```arturo
c: couple ["one" "two" "three"] [1 2 3]
; c: [[1 "one"] [2 "two"] [3 "three"]]

decouple c
; => ["one" "two" "three"] [1 2 3]
```

## `dictionary`

Documentation: https://arturo-lang.io/documentation/library/collections/dictionary

### Example 1

```arturo
none: #[]               ; none: []
a: #[
    name: "John"
    age: 34
]
; a: [name: "John", age: 34]

d: #[
    name: "John"
    print "we are in the block"
    age: 34
    print "yep"
]
; we are in the block
; yep
; d: [name: "John", age: 34]
```

### Example 2

```arturo
inspect fromBlock: #.raw [a b c d]
; [ :dictionary
;         a  :        b :word
;         c  :        d :word
; ]
```

### Example 3

```arturo
e: #.lower [
    Name: "John"
    suRnaMe: "Doe"
    AGE: 35
]
; e: [name:John, surname:Doe, age:35]
```

### Example 4

```arturo
entity: "EU"

location: dictionary.with: [entity][
    country: "Spain"
]

print location\entity   ; => EU
```

## `drop`

Documentation: https://arturo-lang.io/documentation/library/collections/drop

### Example 1

```arturo
drop "xhello"               ; => "hello"
drop drop "xhello"          ; => "ello"
```

### Example 2

```arturo
str: "some text"
drop.times:5 str            ; => text
drop.times: neg 5 str       ; => some
```

### Example 3

```arturo
arr: @1..10
drop.times:3 'arr
arr                         ; => [4 5 6 7 8 9 10]
```

### Example 4

```arturo
drop [1 2 3]                ; => [2 3]
```

### Example 5

```arturo
drop.times:1 [1 2 3]        ; => [2 3]
drop.times:2 [1 2 3]        ; => [3]
drop.times:3 [1 2 3]        ; => []
drop.times:4 [1 2 3]        ; => []
```

### Example 6

```arturo
drop.times: neg 1 [1 2 3]   ; => [1 2]
drop.times: neg 2 [1 2 3]   ; => [1]
```

### Example 7

```arturo
it: to :iterator 1..6
drop.times:2 it
to :block it                ; => [3 4 5 6]
```

### Example 8

```arturo
lazy: drop.iterator.times:2 [1 2 3 4 5]
to :block lazy              ; => [3 4 5]
```

## `empty`

Documentation: https://arturo-lang.io/documentation/library/collections/empty

### Example 1

```arturo
a: [1 2 3]
empty 'a              ; a: []
```

### Example 2

```arturo
str: "some text"
empty 'str            ; str: ""
```

## `empty?`

Documentation: https://arturo-lang.io/documentation/library/collections/empty-

### Example 1

```arturo
empty? ""             ; => true
empty? []             ; => true
empty? #[]            ; => true

empty? [1 "two" 3]    ; => false
```

### Example 2

```arturo
it: to :iterator 1..2
empty? it             ; => false
@it
empty? it             ; => true
```

## `extend`

Documentation: https://arturo-lang.io/documentation/library/collections/extend

### Example 1

```arturo
person: #[ name: "john" surname: "doe" ]

print extend person #[ age: 35 ]
; [name:john surname:doe age:35]
```

## `first`

Documentation: https://arturo-lang.io/documentation/library/collections/first

### Example 1

```arturo
print first "this is some text"       ; t
print first ["one" "two" "three"]     ; one
```

### Example 2

```arturo
print first.n:2 ["one" "two" "three"] ; one two
```

### Example 3

```arturo
it: to :iterator 5..7
first it                               ; => 5
first.n:2 it                           ; => [6 7]
```

## `flatten`

Documentation: https://arturo-lang.io/documentation/library/collections/flatten

### Example 1

```arturo
arr: [[1 2 3] [4 5 6]]
print flatten arr
; 1 2 3 4 5 6
```

### Example 2

```arturo
arr: [[1 2 3] [4 5 6]]
flatten 'arr
; arr: [1 2 3 4 5 6]
```

### Example 3

```arturo
flatten [1 [2 3] [4 [5 6]]]
; => [1 2 3 4 5 6]
```

### Example 4

```arturo
flatten.once [1 [2 3] [4 [5 6]]]
; => [1 2 3 4 [5 6]]
```

## `get`

Documentation: https://arturo-lang.io/documentation/library/collections/get

### Example 1

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

print user\name               ; John

print get user 'surname       ; Doe
print user\surname            ; Doe
```

### Example 2

```arturo
arr: ["zero" "one" "two"]

print arr\1                   ; one

print get arr 2               ; two
y: 2
print arr\[y]                 ; two
```

### Example 3

```arturo
str: "Hello world!"

print str\0                   ; H

print get str 1               ; e
z: 0
print str\[z+1]               ; e
print str\[0..4]              ; Hello
```

### Example 4

```arturo
a: to :complex [1 2]
print a\real                  ; 1.0
print a\imaginary             ; 2.0
print a\1                     ; 2.0
```

### Example 5

```arturo
define :person [
    get: method [what][
        (key? this what)? -> get.field this what    ; if the key exists, return the value
                          -> "DEFAULT"              ; otherwise, do something else
    ]
]
```

## `in?`

Documentation: https://arturo-lang.io/documentation/library/collections/in-

### Example 1

```arturo
arr: [1 2 3 4]

in? 5 arr             ; => false
in? 2 arr             ; => true
```

### Example 2

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

in? "John" dict       ; => true
in? "Paul" dict       ; => false

in? "name" keys dict  ; => true
```

### Example 3

```arturo
in? "x" "hello"       ; => false
in? `h` "hello"       ; => true
```

### Example 4

```arturo
in?.at:1 "el" "hello" ; => true
in?.at:4 `o` "hello"  ; => true
```

### Example 5

```arturo
print in?.at:2 "two" ["one" "two" "three"]
; false

print in?.at:1 "two" ["one" "two" "three"]
; true
```

### Example 6

```arturo
print in?.deep 6 [1 2 4 [3 4 [5 6] 7] 8 [9 10]]
; true
```

### Example 7

```arturo
user: #[ 
    name: "John" surname: "Doe"
    mom: #[ name: "Jane" surname: "Doe" ]
]

print in?.deep "Jane" user
; true
```

## `index`

Documentation: https://arturo-lang.io/documentation/library/collections/index

### Example 1

```arturo
ind: index "hello" "e"
print ind                 ; 1
```

### Example 2

```arturo
print index [1 2 3] 3     ; 2
```

### Example 3

```arturo
type index "hello" "x"
; :null
```

## `insert`

Documentation: https://arturo-lang.io/documentation/library/collections/insert

### Example 1

```arturo
insert [1 2 3 4] 0 "zero"
; => ["zero" 1 2 3 4]

print insert "heo" 2 "ll"
; hello
```

### Example 2

```arturo
dict: #[
    name: John
]

insert 'dict 'name "Jane"
; dict: [name: "Jane"]
```

## `key?`

Documentation: https://arturo-lang.io/documentation/library/collections/key-

### Example 1

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

key? user 'age            ; => false
if key? user 'name [
    print ["Hello" user\name]
]
; Hello John
```

## `keys`

Documentation: https://arturo-lang.io/documentation/library/collections/keys

### Example 1

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

keys user
=> ["name" "surname"]
```

## `last`

Documentation: https://arturo-lang.io/documentation/library/collections/last

### Example 1

```arturo
print last "this is some text"       ; t
print last ["one" "two" "three"]     ; three
```

### Example 2

```arturo
print last.n:2 ["one" "two" "three"] ; two three
```

## `max`

Documentation: https://arturo-lang.io/documentation/library/collections/max

### Example 1

```arturo
print max [4 2 8 5 1 9]       ; 9
```

## `min`

Documentation: https://arturo-lang.io/documentation/library/collections/min

### Example 1

```arturo
print min [4 2 8 5 1 9]       ; 1
```

## `one?`

Documentation: https://arturo-lang.io/documentation/library/collections/one-

### Example 1

```arturo
one? 5              ; => false
one? 4-3            ; => true
```

### Example 2

```arturo
one? 1.0            ; => true
one? 0.0            ; => false
```

### Example 3

```arturo
items: ["apple"]
one? items          ; => true

items: [1 2 3]
one? items          ; => false
```

### Example 4

```arturo
one? ø              ; => false
```

## `permutate`

Documentation: https://arturo-lang.io/documentation/library/collections/permutate

### Example 1

```arturo
permutate [A B C]
; => [[A B C] [A C B] [B A C] [B C A] [C A B] [C B A]]

permutate.repeated [A B C]
; => [[A A A] [A A B] [A A C] [A B A] [A B B] [A B C] [A C A] [A C B] [A C C] [B A A] [B A B] [B A C] [B B A] [B B B] [B B C] [B C A] [B C B] [B C C] [C A A] [C A B] [C A C] [C B A] [C B B] [C B C] [C C A] [C C B] [C C C]]
```

### Example 2

```arturo
permutate.by:2 [A B C]
; => [[A B] [A C] [B A] [B C] [C A] [C B]]

permutate.repeated.by:2 [A B C]
; => [[A A] [A B] [A C] [B A] [B B] [B C] [C A] [C B] [C C]]

permutate.repeated.by:3 [A B]
; => [[A A A] [A A B] [A B A] [A B B] [B A A] [B A B] [B B A] [B B B]]
```

### Example 3

```arturo
permutate.count [A B C]
; => 6

permutate.count.repeated.by:2 [A B C]
; => 9
```

## `pop`

Documentation: https://arturo-lang.io/documentation/library/collections/pop

### Example 1

```arturo
a: [0 1 2 3 4 5]
b: pop 'a

inspect a
; [ :block
;         0 :integer
;         1 :integer
;         2 :integer
;         3 :integer
;         4 :integer
; ]
inspect b     ; 5 :integer


b: pop.n: 2 'a

inspect a
; [ :block
;         0 :integer
;         1 :integer
;         2 :integer
; ]
inspect b
; [ :block
;         3 :integer
;         4 :integer
; ]
```

### Example 2

```arturo
a: "Arturoo"
b: pop 'a

inspect a     ; Arturo :string
inspect b     ; o :char

b: pop.n: 3 'a

inspect a     ; Art :string
inspect b     ; uro :string
```

## `prepend`

Documentation: https://arturo-lang.io/documentation/library/collections/prepend

### Example 1

```arturo
prepend "uro" "Art"     ; => "Arturo"
prepend [2 3 4] 1       ; => [1 2 3 4]
prepend [3 4 5] [1 2]   ; => [1 2 3 4 5]
```

### Example 2

```arturo
a: "pend"
prepend 'a "pre"
print a                 ; prepend
```

## `range`

Documentation: https://arturo-lang.io/documentation/library/collections/range

### Example 1

```arturo
; range of :integers

        range 0 5           ; 0..5
        0..5                ; 0..5
        @0..5               ; [0 1 2 3 4 5]
```

### Example 2

```arturo
        ; range of :chars

        'a'..'e'            ; 'a'..'e'
        @'a'..'e'           ; [a b c d e]
```

### Example 3

```arturo
        ; range with steps

        @range.step: 2 1 5   ; [1 3 5]
```

### Example 4

```arturo
        ; iterate a range

        0..5 | loop 'i -> print ~"|i|. hello"
        ; 0. hello
        ; 1. hello
        ; 2. hello
        ; 3. hello
        ; 4. hello
        ; 5. hello
```

### Example 5

```arturo
        ; check bounds

        in? 5 0..10     ; => true
```

## `remove`

Documentation: https://arturo-lang.io/documentation/library/collections/remove

### Example 1

```arturo
remove "hello" "l"        ; => "heo"
print "hello" -- "l"      ; heo
remove [1 2 3 4] 4        ; => [1 2 3]
```

### Example 2

```arturo
str: "mystring"
remove 'str "str"
print str                 ; mying
```

### Example 3

```arturo
remove.key #[name: "John" surname: "Doe"] "surname" ; => #[name: "John"]
```

### Example 4

```arturo
print remove.once "hello" "l"
; helo

; Remove each element of given block from collection once
remove.once  [1 2 [1 2] 3 4 1 2 [1 2] 3 4]  [1 2]
; [[1 2] 3 4 1 2 [1 2] 3 4]
```

### Example 5

```arturo
remove.index: 2 "Ruby" "u"  ; => Rby
remove.index: 2 "Ruby" "a"  ; => Ruby
```

### Example 6

```arturo
remove.prefix "--empty --flag" "--"         ; => "empty --flag"
remove.suffix "test.txt file.txt" ".txt"   ; => "test.txt file"
```

### Example 7

```arturo
remove.instance [1 [6 2] 5 3 [6 2] 4 5 6] [6 2]  ; => [1 5 3 4 5 6]
remove.instance.once [1 [6 2] 5 3 [6 2] 4 5 6] [6 2]  ; => [1 5 3 [6 2] 4 5 6]
```

## `repeat`

Documentation: https://arturo-lang.io/documentation/library/collections/repeat

### Example 1

```arturo
print repeat "hello" 3
; hellohellohello
```

### Example 2

```arturo
repeat [1 2 3] 3
; => [1 2 3 1 2 3 1 2 3]
```

### Example 3

```arturo
repeat 5 3
; => [5 5 5]
```

### Example 4

```arturo
repeat [[1 2 3]] 3
; => [[1 2 3] [1 2 3] [1 2 3]]
```

## `reverse`

Documentation: https://arturo-lang.io/documentation/library/collections/reverse

### Example 1

```arturo
print reverse [1 2 3 4]           ; 4 3 2 1
print reverse "Hello World"       ; dlroW olleH
```

### Example 2

```arturo
str: "my string"
reverse 'str
print str                         ; gnirts ym
```

## `rotate`

Documentation: https://arturo-lang.io/documentation/library/collections/rotate

### Example 1

```arturo
rotate [a b c d e] 1            ; => [e a b c d]
rotate.left [a b c d e] 1       ; => [b c d e a]

rotate 1..6 4                   ; => [3 4 5 6 1 2]
```

## `sample`

Documentation: https://arturo-lang.io/documentation/library/collections/sample

### Example 1

```arturo
sample [1 2 3]        ; (return a random number from 1 to 3)
print sample ["apple" "appricot" "banana"]
; apple
```

## `set`

Documentation: https://arturo-lang.io/documentation/library/collections/set

### Example 1

```arturo
myDict: #[
    name: "John"
    age: 34
]

set myDict 'name "Michael"        ; => [name: "Michael", age: 34]
```

### Example 2

```arturo
arr: [1 2 3 4]
set arr 0 "one"                   ; => ["one" 2 3 4]

arr\1: "dos"                      ; => ["one" "dos" 3 4]

x: 2
arr\[x]: "tres"                   ; => ["one" "dos" "tres" 4]
```

### Example 3

```arturo
str: "hello"
str\0: `x`
print str
; xello
```

### Example 4

```arturo
define :person [
    set: method [what, value][
        ; do some processing...

        set.field this what value
        ; and actually set the value internally
    ]
]
```

## `shuffle`

Documentation: https://arturo-lang.io/documentation/library/collections/shuffle

### Example 1

```arturo
shuffle [1 2 3 4 5 6]         ; => [1 5 6 2 3 4 ]
```

### Example 2

```arturo
arr: [2 5 9]
shuffle 'arr
print arr                     ; 5 9 2
```

## `size`

Documentation: https://arturo-lang.io/documentation/library/collections/size

### Example 1

```arturo
arr: ["one" "two" "three"]
print size arr                ; 3
```

### Example 2

```arturo
dict: #[name: "John", surname: "Doe"]
print size dict               ; 2
```

### Example 3

```arturo
str: "some text"
print size str                ; 9

print size "你好!"              ; 3
```

## `slice`

Documentation: https://arturo-lang.io/documentation/library/collections/slice

### Example 1

```arturo
slice "Hello" 0 3             ; => "Hell"
```

### Example 2

```arturo
print slice 1..10 3 4         ; 4 5
```

## `sort`

Documentation: https://arturo-lang.io/documentation/library/collections/sort

### Example 1

```arturo
a: [3 1 6]
print sort a                  ; 1 3 6
```

### Example 2

```arturo
print sort.descending a       ; 6 3 1
```

### Example 3

```arturo
b: ["one" "two" "three"]
sort 'b
print b                       ; one three two
```

### Example 4

```arturo
; Creating a Priority Queue
tasks: []

; add tasks with priorities
'tasks ++ #[priority: 3 task: "Low priority"]
'tasks ++ #[priority: 1 task: "Urgent!"]
'tasks ++ #[priority: 2 task: "Important"]

; sort by priority
sorted: sort.by: 'priority tasks
loop sorted 'item ->
    print [item\priority ":" item\task]
; 1 : Urgent!
; 2 : Important
; 3 : Low priority
```

### Example 5

```arturo
spanishWords: ["uno","dos","tres","Uno","perversión","ábaco","abismo", "aberración"]
sort.as: 'es spanishWords
; => ["ábaco" "aberración" "abismo" "dos" "perversión" "tres" "uno" "Uno"]
```

### Example 6

```arturo
sort.sensitive ["c" "C" "CoffeeScript" "nim" "Arturo" "coffeescript" "arturo" "Nim"]
; => ["Arturo" "C" "CoffeeScript" "Nim" "arturo" "c" "coffeescript" "nim"]
```

### Example 7

```arturo
sort.values #[ name: "John" surname: "Doe" age: 35 income: 5000]
; => #[age: 35 income: 5000 surname: "Doe" name: "John" ]
```

## `sorted?`

Documentation: https://arturo-lang.io/documentation/library/collections/sorted-

### Example 1

```arturo
sorted? [1 2 3 4 5]         ; => true
sorted? [4 3 2 1 5]         ; => false
sorted? [5 4 3 2 1]         ; => false
```

### Example 2

```arturo
sorted?.descending [5 4 3 2 1]      ; => true
sorted?.descending [4 3 2 1 5]      ; => false
sorted?.descending [1 2 3 4 5]      ; => false
```

## `split`

Documentation: https://arturo-lang.io/documentation/library/collections/split

### Example 1

```arturo
split "hello"                 ; => [`h` `e` `l` `l` `o`]
```

### Example 2

```arturo
split.words "hello world"     ; => ["hello" "world"]
split.by: "," "hello,world"   ; => ["hello" "world"]
split.lines "hello\nworld"    ; => ["hello" "world"]
split.path "/usr/bin"         ; => ["usr" "bin"]

; windows only:
split.path "\\usr\\bin"       ; => ["usr" "bin"]
```

### Example 3

```arturo
split.every: 2 "helloworld"
; => ["he" "ll" "ow" "or" "ld"]
```

### Example 4

```arturo
split.at: 4 "helloworld"
; => ["hell" "oworld"]
```

### Example 5

```arturo
arr: 1..9
split.at:3 'arr
; => [ [1 2 3 4] [5 6 7 8 9] ]
```

## `squeeze`

Documentation: https://arturo-lang.io/documentation/library/collections/squeeze

### Example 1

```arturo
print squeeze [1 1 2 3 4 2 3 4 4 5 5 6 7]
; 1 2 3 4 2 3 4 5 6 7
```

### Example 2

```arturo
arr: [4 2 1 1 3 6 6]
squeeze 'arr            ; a: [4 2 1 3 6]
```

### Example 3

```arturo
print squeeze "hello world"
; helo world
```

## `take`

Documentation: https://arturo-lang.io/documentation/library/collections/take

### Example 1

```arturo
str: "some text"
take str 4              ; => some
take str neg 4          ; => text

take 1..3 2             ; => [1 2]
```

### Example 2

```arturo
arr: @1..10
take 'arr 3                   
arr                     ; => arr: [1 2 3]
```

### Example 3

```arturo
take [1 2 3] 3          ; => [1 2 3]
take [1 2 3] 4          ; => [1 2 3]
```

### Example 4

```arturo
it: to :iterator 1..6
take it 3               ; => [1 2 3]
```

### Example 5

```arturo
lazy: take.iterator 1..6 3
to :block lazy          ; => [1 2 3]
```

## `tally`

Documentation: https://arturo-lang.io/documentation/library/collections/tally

### Example 1

```arturo
tally "helloWorld"
; => [h:1 e:1 l:3 o:2 W:1 r:1 d:1]
```

### Example 2

```arturo
tally [1 2 4 1 3 5 6 2 6 3 5 7 2 4 2 4 5 6 2 1 1 1]
; => [1:5 2:5 4:3 3:2 5:3 6:3 7:1]
```

## `unique`

Documentation: https://arturo-lang.io/documentation/library/collections/unique

### Example 1

```arturo
arr: [1 2 4 1 3 2]
print unique arr              ; 1 2 4 3
```

### Example 2

```arturo
arr: [1 2 4 1 3 2]
unique 'arr
print arr                     ; 1 2 4 3
```

### Example 3

```arturo
unique.id "user-"   ; => user-67915b7a409e222b2f9a6bed
```

## `values`

Documentation: https://arturo-lang.io/documentation/library/collections/values

### Example 1

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

values user     ; => ["John" "Doe"]
```

## `zero?`

Documentation: https://arturo-lang.io/documentation/library/collections/zero-

### Example 1

```arturo
zero? 5-5           ; => true
zero? 4             ; => false
```

### Example 2

```arturo
zero? 1.0           ; => false
zero? 0.0           ; => true
```

### Example 3

```arturo
items: [1 2 3]
zero? items         ; => false    

items: []
zero? items         ; => true
```

### Example 4

```arturo
zero? ø             ; => true
```
