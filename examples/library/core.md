# core 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `alias`

Documentation: https://arturo-lang.io/documentation/library/core/alias

### Example 1

```arturo
addThem: function [x, y][
    x + y
]
alias '--> 'addThem!
    
print --> 2 3
; 5
```

### Example 2

```arturo
multiplyThem: function [x, y][ x * y ]
alias.infix {<=>} 'multiplyThem!

print 2 <=> 3
; 6
```

## `any`

Documentation: https://arturo-lang.io/documentation/library/core/any

### Example 1

```arturo

```

## `break`

Documentation: https://arturo-lang.io/documentation/library/core/break

### Example 1

```arturo
loop 1..5 'x [
    print ["x:" x]
    if x=3 -> break
    print "after check"
]
print "after loop"

; x: 1
; after check
; x: 2
; after check
; x: 3
; after loop
```

## `call`

Documentation: https://arturo-lang.io/documentation/library/core/call

### Example 1

```arturo
multiply: function [x y][
    x * y
]

call 'multiply [3 5]          ; => 15
```

### Example 2

```arturo
call $[x][x+2] [5]            ; 7
```

### Example 3

```arturo
; Calling external (C code) functions

; compile with:
; clang -c -w mylib.c
; clang -shared -o libmylib.dylib mylib.o
; 
; NOTE:
; * If you're using GCC, just replace `clang` by `gcc`
; * If you're not on MacOS, replace your `dylib` by the right extension
;   normally they can be `.so` or `.dll` in other Operational Systems.

; #include <stdio.h>
;
; void sayHello(char* name){
;    printf("Hello %s!\n", name);
; }
;
; int doubleNum(int num){
;    return num * 2;
;}

; call an external function directly
call.external: "mylib" 'sayHello ["John"]

; map an external function to a native one
doubleNum: function [num][
    ensure -> integer? num
    call .external: "mylib"
        .expect:   :integer
        'doubleNum @[num]
]

loop 1..3 'x [
    print ["The double of" x "is" doubleNum x]
]
```

## `case`

Documentation: https://arturo-lang.io/documentation/library/core/case

### Example 1

```arturo
x: 2

; the main block is always evaluated!
case x [
    1   -> print "x is one!"
    2   -> print "x is two!"
    any -> print "x is none of the above"
]
; x is two!
```

### Example 2

```arturo
key: "one"
case key [
    "one" 1,        ; we can also return
    "two" 2         ; simple constant values directly
]
; => 2
```

### Example 3

```arturo
case "hello" #[
    hello: "hola"
    adios: "goodbye"
]
; => "hola"
```

## `coalesce`

Documentation: https://arturo-lang.io/documentation/library/core/coalesce

### Example 1

```arturo
; Note that 'attr returns null if it has no attribute          
print coalesce attr "myAttr" "attr not found"
print (attr "myAttr") ?? "attr not found"

print (myData) ?? defaultData
```

## `continue`

Documentation: https://arturo-lang.io/documentation/library/core/continue

### Example 1

```arturo
loop 1..5 'x [
    print ["x:" x]
    if x=3 -> continue
    print "after check"
]
print "after loop"

; x: 1 
; after check
; x: 2 
; after check
; x: 3 
; x: 4 
; after check
; x: 5 
; after check
; after loop
```

## `discard`

Documentation: https://arturo-lang.io/documentation/library/core/discard

### Example 1

```arturo
validInteger?: function [str][
    not? throws? [
        discard to :integer str
        ; we don't really need the value here -
        ; we just want to see if the operation throws an error
    ]
]

print validInteger? "123"
; true
```

## `do`

Documentation: https://arturo-lang.io/documentation/library/core/do

### Example 1

```arturo
do "print 123"                ; 123
```

### Example 2

```arturo
do [
    x: 3
    print ["x =>" x]          ; x => 3
]
```

### Example 3

```arturo
print do "https://raw.githubusercontent.com/arturo-lang/arturo/master/examples/projecteuler/euler1.art"
; 233168
```

### Example 4

```arturo
do.times: 3 [
    print "Hello!"
]
; Hello!
; Hello!
; Hello!
```

### Example 5

```arturo
; Importing modules

; let's say you have a 'module.art' with  this code:
;
; pi: 3.14
;
; hello: $[name :string] [
;    print ["Hello" name]
;]

do relative "module.art"

print pi
; 3.14

do [
    hello "John Doe"
    ; Hello John Doe
]

; Note: always use imported functions inside a 'do block
; since they need to be evaluated beforehand.
; On the other hand, simple variables can be used without
; issues, as 'pi in this example
```

### Example 6

```arturo
; concurrent evaluation, returns a `:task`
x: 10
t: do.async [ x + 32 ]
print wait t                  ; 42
```

### Example 7

```arturo
; ⚠ closure capture is shallow-copy: writes do NOT leak back
u: 1
wait do.async [ u: 99 ]
print u                       ; 1
```

### Example 8

```arturo
; subprocess flavor: fresh VM, no closure capture
t: do.async.isolated [ print "fresh VM" ]
wait t
```

## `dup`

Documentation: https://arturo-lang.io/documentation/library/core/dup

### Example 1

```arturo
; a label normally consumes its inputs
; and returns nothing

; using dup before a call, the non-returning function
; becomes a returning one

a: b: <= 3

print a         ; 3
print b         ; 3
```

## `ensure`

Documentation: https://arturo-lang.io/documentation/library/core/ensure

### Example 1

```arturo
num: input "give me a positive number"

ensure [num > 0]

print "good, the number is positive indeed. let's continue..."
```

### Example 2

```arturo
ensure.that: "Wrong calc" ->  0 = 1 + 1
; >> Assertion | "Wrong calc": [0 = 1 + 1]
;        error |
```

## `export`

Documentation: https://arturo-lang.io/documentation/library/core/export

### Example 1

```arturo
greeting: module [
greet: method.public [user :string][
    print ~"Hello, |user|!"
]
        ]

        export greeting!

        greet "Anonymous"   ; Hello, Anonymous!
```

### Example 2

```arturo
        ; You can't use private methods
        greeting: module [
greet: method [user :string][
    print ~"Bye, bye, |user|!"
]
        ]

        export greeting!

        greet "Anonymous"
        ; Cannot resolve requested value
        ;
        ; Identifier not found: 
        ;     greet
        ;
        ; ┃ File: example.art
        ; ┃ Line: 9
        ; ┃ 
        ; ┃    7 ║  ]
        ; ┃    8 ║  
        ; ┃    9 ║► export greeting!
        ; ┃   10 ║  
        ; ┃   11 ║  greet "Anonymous"
        ; 
        ; Hint: Perhaps you meant... greeting ?
        ;                     or... repeat ?
        ;                     or... greater? ?
```

### Example 3

```arturo
        ; You can export private functions using the `.all` attribute
        greeting: module [
greet: method [user :string][
    print ~"Bye, bye, |user|!"
]
        ]

        export.all greeting!

        greet "Anonymous" ; Bye, bye, Anonymous!
```

## `express`

Documentation: https://arturo-lang.io/documentation/library/core/express

### Example 1

```arturo
example: "Hello, world"
example                 ; => Hello, world
express example         ; => "Hello, world"
```

### Example 2

```arturo
d: #[name: "John"]
d\surname: "Doe"

express d
; => #[name: "John" surname: "Doe" ]
```

### Example 3

```arturo
express.pretty #[name: "John" surname: "Doe"]
; => #[
;         name: "John"
;         surname: "Doe"
; ]
```

## `function`

Documentation: https://arturo-lang.io/documentation/library/core/function

### Example 1

```arturo
f: function [x][ x + 2 ]
print f 10                ; 12

f: $[x][x+2]
print f 10                ; 12
```

### Example 2

```arturo
multiply: function [x,y][
    x * y
]
print multiply 3 5        ; 15
```

### Example 3

```arturo
; forcing typed parameters
addThem: function [
    x :integer
    y :integer :floating
][
    x + y
]
```

### Example 4

```arturo
; adding complete documentation for user function
; using data comments within the body
addThem: function [
    x :integer :floating
    y :integer :floating
][
    ;; description: « takes two numbers and adds them up
    ;; options: [
    ;;      mul: :integer « also multiply by given number
    ;; ]
    ;; returns: :integer :floating
    ;; example: {
    ;;      addThem 10 20
    ;;      addThem.mult:3 10 20
    ;; }

    mult?: attr 'mult
    switch not? null? mult? 
        -> return mult? * x + y
        -> return x + y
]

info'addThem

; |--------------------------------------------------------------------------------
; |        addThem  :function                                          0x10EF0E528
; |--------------------------------------------------------------------------------
; |                 takes two numbers and adds them up
; |--------------------------------------------------------------------------------
; |          usage  addThem x :integer :floating
; |                         y :integer :floating
; |
; |        options  .mult :integer -> also multiply by given number
; |
; |        returns  :integer :floating
; |--------------------------------------------------------------------------------
```

### Example 5

```arturo
publicF: function .export:['x] [z][
    print ["z =>" z]
    x: 5
]

publicF 10
; z => 10

print x
; 5
```

### Example 6

```arturo
; memoization
fib: $[x].memoize[
    switch x<2 -> 1
               -> (fib x-1) + (fib x-2)
]

loop 1..25 [x][
    print ["Fibonacci of" x "=" fib x]
]
```

## `if`

Documentation: https://arturo-lang.io/documentation/library/core/if

### Example 1

```arturo
x: 2

if x=2 -> print "yes, that's right!"
; yes, that's right!
```

## `import`

Documentation: https://arturo-lang.io/documentation/library/core/import

### Example 1

```arturo
import "dummy"                      ; import the package 'dummy'
    do ::
        print dummyFunc 10              ; and use it :)
```

### Example 2

```arturo
    import.version:0.0.3 "dummy"        ; import a specific version

    import.min.version:0.0.3 "dummy"    ; import at least the give version;
                                        ; if there is a newer one, it will pull this one
```

### Example 3

```arturo
    import.latest "dummy"               ; whether we already have the package or not
                                        ; always try to pull the latest version
```

### Example 4

```arturo
    import "https://github.com/arturo-lang/dummy-package"
    ; we may also import user repositories directly

    import.branch:"main" "https://github.com/arturo-lang/dummy-package"
    ; even specifying the branch to pull
```

### Example 5

```arturo
    import "somefile.art"               ; importing a local file is possible

    import "somepackage"                ; the same works if we have a folder that
                                        ; is actually structured like a package
```

### Example 6

```arturo
    d: import.lean "dummy"              ; importing a package as a dictionary
                                        ; for better namespace isolation

    do [
        print d\dummyFunc 10            ; works fine :)
    ]
```

## `let`

Documentation: https://arturo-lang.io/documentation/library/core/let

### Example 1

```arturo
let 'x 10               ; x: 10
print x                 ; 10
```

### Example 2

```arturo
; variable assignments
"a": 2                  ; a: 2

{_someValue}: 3
print var {_someValue}  ; 3
```

### Example 3

```arturo
; multiple assignments
[a b]: [1 2]
print a                 ; 1
print b                 ; 2
```

### Example 4

```arturo
; multiple assignment to single value
[a b c]: 5
print a                 ; 5
print b                 ; 5
print c                 ; 5
```

### Example 5

```arturo
; unpacking slices and multiple assignment
[a [b] d c]: [1 2 3 4 5]
print a                 ; 1
print b                 ; [2 3]
print c                 ; 4
print d                 ; 5
```

### Example 6

```arturo
; tuple unpacking
divmod: function [x,y][
    @[x/y x%y]
]
[d,m]: divmod 10 3      ; d: 3, m: 1
```

## `method`

Documentation: https://arturo-lang.io/documentation/library/core/method

### Example 1

```arturo
define :cat [
init: method [nick :string age :integer][
    this\nick: join.with: " " @["Mr." capitalize nick]
    this\age: age
]

; Function overloading
add: method [years :integer][
    this\age: age + this\age
]

meow: method [][
    print [~"|this\nick|:" "'meow!'"]
]
        ]

        a: to :cat [15 15]
        ; >> Assertion | [is? :string nick]
        ;        error |  

        snowflake: to :cat ["snowflake" 3]

        snowflake\meow
        ; Mr. Snowflake: 'meow!'

        ; use `do -> snowflake\meow` instead 
        ; when running the above code from a file

        add snowflake 3
        snowflake\age
        ; => 6

        snowflake\add 3
        print snowflake\age
        ; => 9

        ; use `do [snowflake\add 3]` instead
        ; when running the above code from a file
```

## `module`

Documentation: https://arturo-lang.io/documentation/library/core/module

### Example 1

```arturo
ui: module [

namedRule: method [title :string width :integer][
    title: ~" |title| "
    pad.center.with: '=' title width
]

section: method.public [title :string content :string width :integer][
    ~{
        |\namedRule title width|
        |content|
        |\namedRule title width|
    }
]
        ]

        export ui!

        print section "Hello" "World" 50
        ; ===================== Hello ======================
        ; World
        ; ===================== Hello ======================
        print set? 'ui          ; true
        print set? 'namedRule   ; false
        print set? 'section     ; true
```

### Example 2

```arturo
        ui: [

init: method [symbol :char][
    \symbol: symbol
]

namedRule: method [title :string width :integer][
    title: ~" |title| "
    pad.center.with: \symbol title width
]

section: method.public [title :string content :string width :integer][
    ~{
        |\namedRule title width|
        |content|
        |\namedRule title width|
    }
]
        ]

        export module.with: ['~'] ui!  
        print section "Example" "This is an example" 40
        ; ~~~~~~~~~~~~~~~ Example ~~~~~~~~~~~~~~~~
        ; This is an example
        ; ~~~~~~~~~~~~~~~ Example ~~~~~~~~~~~~~~~~
```

## `new`

Documentation: https://arturo-lang.io/documentation/library/core/new

### Example 1

```arturo
c: "Hello"
d: new c        ; make a copy of the older string

; changing one string in-place
; will change only the string in question

'd ++ "World"
print d                 ; HelloWorld
print c                 ; Hello
```

## `null`

Documentation: https://arturo-lang.io/documentation/library/core/null

### Example 1

```arturo

```

## `parse`

Documentation: https://arturo-lang.io/documentation/library/core/parse

### Example 1

```arturo
parse "123"         ; 123 (:integer)
parse "3.14"        ; 3.14 (:floating)
parse "true"        ; true (:logical)
parse "[1 2 3]"     ; [1 2 3] (:block)
```

## `return`

Documentation: https://arturo-lang.io/documentation/library/core/return

### Example 1

```arturo
f: function [x][ 
    loop 1..x 'y [ 
        if y=5 [ return y*2 ] 
    ] 
    return x*2
]

print f 3         ; 6
print f 6         ; 10
```

## `set?`

Documentation: https://arturo-lang.io/documentation/library/core/set-

### Example 1

```arturo
boom: 12
print set? 'boom          ; true

print set? 'zoom          ; false
```

## `switch`

Documentation: https://arturo-lang.io/documentation/library/core/switch

### Example 1

```arturo
x: 2

switch x=2 -> print "yes, that's right!"
           -> print "nope, that's not right!"
; yes, that's right!
```

## `unless`

Documentation: https://arturo-lang.io/documentation/library/core/unless

### Example 1

```arturo
x: 2

unless x=1 -> print "yep, x is not 1!"
; yep, x is not 1!
```

## `unset`

Documentation: https://arturo-lang.io/documentation/library/core/unset

### Example 1

```arturo
a: 2
print a
; 2

unset 'a
print a
; will throw an error
```

## `unstack`

Documentation: https://arturo-lang.io/documentation/library/core/unstack

### Example 1

```arturo
1 2 3
a: unstack 1        ; a: 3

1 2 3
b: unstack 2        ; b: [3 2]
```

### Example 2

```arturo
; You can also discard the values using `discard`
1 2 3
discard unstack 1   ; popped 3 from the stack
```

## `until`

Documentation: https://arturo-lang.io/documentation/library/core/until

### Example 1

```arturo
i: 0 
until [
    print ["i =>" i] 
    i: i + 1
][i = 10]

; i => 0 
; i => 1 
; i => 2 
; i => 3 
; i => 4 
; i => 5 
; i => 6 
; i => 7 
; i => 8 
; i => 9
```

## `using`

Documentation: https://arturo-lang.io/documentation/library/core/using

### Example 1

```arturo
p: #[name: "John" surname: "Doe" age: 38]
using p [
    print \name             ; access our
    print \age              ; fields directly

    \surname: "Smith"       ; or change their value
]
; John
; 38
```

## `var`

Documentation: https://arturo-lang.io/documentation/library/core/var

### Example 1

```arturo
a: 2
print var 'a            ; 2

f: function [x][x+2]
print f 10              ; 12

g: var 'f               
print g 10              ; 12
```

## `when`

Documentation: https://arturo-lang.io/documentation/library/core/when

### Example 1

```arturo
; the main block is always evaluated!
when [
    prime? 4 -> print "yes, 4 is prime - wait, what?!"
    prime? 5 -> print "yes, 5 is prime"
    prime? 7 -> print "yes, 6 is prime"
    true     -> print "none of the above was true"
]
; yes, 5 is prime
```

### Example 2

```arturo
when.any [
    prime? 4 -> print "yes, 4 is prime - wait, what?!"
    prime? 5 -> print "yes, 5 is prime"
    prime? 7 -> print "yes, 7 is prime"
]
; yes, 5 is prime
; yes, 7 is prime
```

### Example 3

```arturo
x: 2
when.has: x [
    [=0] -> print "x is zero!"
    [<1] -> print "x is less than 1"
    [<4] -> print "x is less than 4"
    true -> print "x is >= 4"
]
; x is less than 4
```

### Example 4

```arturo
f: function [x][
    print ["called F with:" x]
    return odd? x
]
; short-circuiting:
; conditions are not evaluated unless needed
when [
    [f 10]-> print "F 10"
    [f 11]-> print "F 11"
    [f 12]-> print "F 12"
]
; called F with: 10 
; called F with: 11 
; F 11
```

## `while`

Documentation: https://arturo-lang.io/documentation/library/core/while

### Example 1

```arturo
i: 0 
while [i<10][
    print ["i =>" i] 
    i: i + 1
]

; i => 0 
; i => 1 
; i => 2 
; i => 3 
; i => 4 
; i => 5 
; i => 6 
; i => 7 
; i => 8 
; i => 9 

while ø [
    print "something"   ; infinitely
]
```

## `window`

Documentation: https://arturo-lang.io/documentation/library/core/window

> 当前 runtime 未导出示例，或该 symbol 在当前 build 中不可解析。

## `with`

Documentation: https://arturo-lang.io/documentation/library/core/with

### Example 1

```arturo
f: function [x][
    with [x][
        "the multiple of" x "is" 2*x
    ]
]

multiplier: f 10

print multiplier
; the multiple of 10 is 20
```
