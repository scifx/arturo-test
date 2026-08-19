# system 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `arg`

Documentation: https://arturo-lang.io/documentation/library/system/arg

### Example 1

```arturo
; called with no parameters
arg         ; => []

; called with: 1 two 3
arg         ; => ["1" "two" "3"]
```

## `args`

Documentation: https://arturo-lang.io/documentation/library/system/args

### Example 1

```arturo
; called with: 1 two 3
args         
; => #[
;     1 
;     "two"
;     3
; ]
```

### Example 2

```arturo
; called with switches: -c -b
args 
; => #[
;     c : true
;     b : true
;     values: []
; ]

; called with switches: -c -b and values: 1 two 3
args
; => #[
;     c : true
;     b : true
;     values: [1 "two" 3]
; ]
```

### Example 3

```arturo
; called with named parameters: -c:2 --name:newname myfile.txt
args
; => #[
;     c : 2
;     name : "newname"
;     values: ["myfile.txt"]
; ]
```

## `config`

Documentation: https://arturo-lang.io/documentation/library/system/config

### Example 1

```arturo
; `config` searches for `config.art` into your current directory. 
    ; if not found, it returns from `~/.arturo/stores/config.art`

    config
    ; => []
    ; `config.art` is empty at first, but we can change this manually

    write.append path\home ++ normalize ".arturo/stores/config.art" 
                 "language: {Arturo}"
    config
    ; => []
    
    ; this stills empty, but now try to relaunch Arturo:
    exit
```

### Example 2

```arturo
    config
    ; => [language:Arturo]
```

## `env`

Documentation: https://arturo-lang.io/documentation/library/system/env

### Example 1

```arturo
print env\SHELL
; /bin/zsh

print env\HOME
; /Users/drkameleon

print env\PATH
; /Users/drkameleon/.arturo/bin:/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

### Example 2

```arturo
; environment variables are not just readable - they're writable too!
env\MY_VARIABLE: "some value"

print env\MY_VARIABLE
; some value

; and any child process will see it as well
print execute "printenv MY_VARIABLE"
; some value
```

### Example 3

```arturo
; appending to an existing variable works just as you'd expect
env\PATH: env\PATH ++ ":/opt/my/bin"

; while setting a variable to `null` removes it altogether
env\MY_VARIABLE: null

print null? env\MY_VARIABLE
; true
```

## `execute`

Documentation: https://arturo-lang.io/documentation/library/system/execute

### Example 1

```arturo
print execute "pwd"
; /Users/admin/Desktop

split.lines execute "ls"
; => ["tests" "var" "data.txt"]
```

### Example 2

```arturo
execute.args: ["-s"] "ls"
; => total 15
; 0 aoc
; 0 architectures
; 4 bundle
; 0 cave
; 4 cmd.c
; 1 expr.art
; 0 galilee
; 4 generic_klist.c
; 1 jquery.js
; 0 shell
; 1 test.art
```

### Example 3

```arturo
execute.code "ls"
; => [output:aoc
; architectures
; bundle
; cave
; cmd.c
; expr.art
; galilee
; generic_klist.c
; jquery.js
; shell
; test.art
; code:0]
```

### Example 4

```arturo
; This prints the output directly
; And only returns the exit code.
execute.code.directly "ls"
aoc            bundle  cmd.c     galilee          jquery.js  test.art
architectures  cave    expr.art  generic_klist.c  shell
=> 0
```

### Example 5

```arturo
; process the output line-by-line, as it arrives -
; without waiting for the command to finish
loop execute.stream "ping -c 3 example.com" 'line ->
    print ["<<" line]
```

### Example 6

```arturo
; early-stop: the child process is terminated
; as soon as we stop pulling from it
print take execute.stream "yes hello" 3
; => ["hello" "hello" "hello"]
```

### Example 7

```arturo
; streams are plain iterators, so they pipe
execute.stream "cat huge.log"
    | select.iterator 'l -> contains? l "ERROR"
    | take 20
    | loop => print
```

### Example 8

```arturo
; the exit code shows up once the stream is drained
s: execute.stream "ls /nonexistent"
drain s
print s\exit    ; => 2
```

### Example 9

```arturo
; raw fixed-size chunks instead of lines
loop execute.stream.buffer:1024 "cat big.bin" 'chunk ->
    print size chunk
```

## `exit`

Documentation: https://arturo-lang.io/documentation/library/system/exit

### Example 1

```arturo
exit              ; (terminates the program)
```

## `panic`

Documentation: https://arturo-lang.io/documentation/library/system/panic

### Example 1

```arturo
panic.unstyled "oops! that was wrong"
; quits with the default exit code (= 1) and
; just outputs a simple - unformatted - message
```

### Example 2

```arturo
panic.code:0 "something went terribly wrong. quitting..."
; quits without an error code but still
; prints a properly formatted error with the given message
```

## `path`

Documentation: https://arturo-lang.io/documentation/library/system/path

### Example 1

```arturo
path
        ; => [current:C:\Users\me\my-proj home:C:\Users\me\ temp:C:\Users\me\AppData\Local\Temp\
```

## `pause`

Documentation: https://arturo-lang.io/documentation/library/system/pause

### Example 1

```arturo
print "wait a moment"

pause 1000      ; sleeping for 1000ms = one second

print "done. let's continue..."
```

### Example 2

```arturo
print "waiting for 2 seconds"

pause 2:s       ; let's sleep for a while

print "done!"
```

## `process`

Documentation: https://arturo-lang.io/documentation/library/system/process

### Example 1

```arturo
print process\id
    ; 78046

    inspect process
    ; [ :dictionary
    ;       id      :	78046 :integer
    ;       memory  :	[ :dictionary
    ;           occupied  :		1783104 :integer
    ;           free      :		360448 :integer
    ;           total     :		2379776 :integer
    ;           max       :		2379776 :integer
    ;       ]
    ; ]
```

## `script`

Documentation: https://arturo-lang.io/documentation/library/system/script

### Example 1

```arturo
;; author: {Me :P}
;; year: 2023
;; license: Some License
;; 
;; description: {
;;      This is an example of documentation.
;;
;;      You can get this by using ``script``.
;; }
;;
;; hint: {
;;      Notice that we use `;;` for documentation,
;;      while the single `;` is just a comment, 
;;      that will be ignored.   
;; }
;;
;; export: [
;;    'myFun
;;    'otherFun
;;    'someConst
;; ]
;;

inspect script
; [ :dictionary
;         author       :        Me :P :string
;         year         :        2023 :integer
;         license      :        [ :block
;                 Some :string
;                 License :string
;         ]
;         description  :        This is an example of documentation.
;  
; You can get this by using ``script``. :string
;         hint         :        Notice that we use `;;` for documentation,
; while the single `;` is just a comment, 
; that will be ignored. :string
;         export       :        [ :block
;                 myFun :string
;                 otherFun :string
;                 someConst :string
;         ]
; ]
```

## `superuser?`

Documentation: https://arturo-lang.io/documentation/library/system/superuser-

### Example 1

```arturo
; when running as root
superuser?          ; => true

; when running as regular user
superuser?          ; => false
```

## `sys`

Documentation: https://arturo-lang.io/documentation/library/system/sys

### Example 1

```arturo
inspect sys
; [ :dictionary
;         author     :        Yanis Zafirópulos :string
;         copyright  :        (c) 2019-2026 :string
;         version    :        0.10.0-dev+3454 :version
;         codename   :         :string
;         built      :        [ :date
;                 hour        :                12 :integer
;                 minute      :                56 :integer
;                 second      :                12 :integer
;                 nanosecond  :                0 :integer
;                 day         :                13 :integer
;                 Day         :                Tuesday :string
;                 days        :                12 :integer
;                 month       :                1 :integer
;                 Month       :                January :string
;                 year        :                2026 :integer
;                 utc         :                -3600 :integer
;         ]
;         deps       :        [ :dictionary
;                 gmp     :                6.3.0 :version
;                 mpfr    :                4.2.1 :version
;                 sqlite  :                3.43.2 :version
;         ]
;         binary     :        /Users/drkameleon/.arturo/bin/arturo :string
;         cpu        :        [ :dictionary
;                 arch    :                amd64 :literal
;                 endian  :                little :literal
;                 cores   :                8 :integer
;         ]
;         os         :        macos :literal
;         hostname   :        drkameleons-MacBook-Pro.local :string
;         release    :        full :literal
; ]
```

## `terminate`

Documentation: https://arturo-lang.io/documentation/library/system/terminate

### Example 1

```arturo
; terminate an external process by PID
    terminate 12345

    ; for tasks spawned via `execute.async`, prefer `cancel`:
    t: execute.async "someLongRunningCommand"
    pause 5000
    cancel t
```
