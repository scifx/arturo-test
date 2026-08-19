# iterators 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `arrange`

Documentation: https://arturo-lang.io/documentation/library/iterators/arrange

### Example 1

```arturo
arrange ["the" "brown" "fox" "jumped" "over" "the" "lazy" "dog"] => size
; => ["the" "fox" "the" "dog" "over" "lazy" "brown" "jumped"]
```

### Example 2

```arturo
arrange.descending 1..10 'x -> size factors.prime x
; => [8 4 6 9 10 2 3 5 7 1]
```

## `chunk`

Documentation: https://arturo-lang.io/documentation/library/iterators/chunk

### Example 1

```arturo
chunk [1 1 2 2 3 22 3 5 5 7 9 2 5] => even?
; => [[1 1] [2 2] [3] [22] [3 5 5 7 9] [2] [5]]
```

### Example 2

```arturo
chunk.value [1 1 2 2 3 22 3 5 5 7 9 2 5] 'x [ odd? x ]
; => [[true [1 1]] [false [2 2]] [true [3]] [false [22]] [true [3 5 5 7 9]] [false [2]] [true [5]]]
```

### Example 3

```arturo
chunk.with:'i ["one" "two" "three" "four" "five" "six"] [] -> i < 4
; => [["one" "two" "three" "four"] ["five" "six"]]
```

### Example 4

```arturo
chunk [1 7 5 4 3 6 8 2] [x y]-> even? x+y
; => [[1 7] [5 4 3 6] [8 2]]
```

## `cluster`

Documentation: https://arturo-lang.io/documentation/library/iterators/cluster

### Example 1

```arturo
cluster 1..10 => odd?
; => [[1 3 5 7 9] [2 4 6 8 10]]

cluster 1..10 'x -> prime? x
; => [[1 4 6 8 9 10] [2 3 5 7]]
```

### Example 2

```arturo
cluster 1..10 [x y] -> 10 < x+y
; => [[1 2 3 4] [5 6 7 8 9 10]]
```

### Example 3

```arturo
cluster.value 1..10 'x -> prime? x
; => [[false [1 4 6 8 9 10]] [true [2 3 5 7]]]
```

### Example 4

```arturo
#.raw flatten.once cluster.value 1..10 'x [
    (prime? x)? -> "prime"
                -> "composite"
]
; => [composite:[1 4 6 8 9 10] prime:[2 3 5 7]]
```

### Example 5

```arturo
cluster.with: 'i ["one" "two" "three" "four" "five" "six"] [] -> even? i
; => [["one" "three" "five"] ["two" "four" "six"]]
```

## `collect`

Documentation: https://arturo-lang.io/documentation/library/iterators/collect

### Example 1

```arturo
collect [1 3 5 4 6 7] => odd?
; => [1 3 5]

collect [1 2 3 4 3 2 1 2 3] 'x -> x < 4
; => [1 2 3]
```

### Example 2

```arturo
collect.after [4 6 3 5 2 0 1] => odd?
; => [3 5 2 0 1]

collect.after 1..10 'x -> x > 4
; => [5 6 7 8 9 10]
```

## `enumerate`

Documentation: https://arturo-lang.io/documentation/library/iterators/enumerate

### Example 1

```arturo
enumerate 1..10000000 => odd?
; => 5000000
```

### Example 2

```arturo
enumerate.with:'i ["one" "two" "three" "four"] 'x -> i < 3
; => 3
```

## `every?`

Documentation: https://arturo-lang.io/documentation/library/iterators/every-

### Example 1

```arturo
if every? [2 4 6 8] 'x [even? x]
    -> print "every number is an even integer"
; every number is an even integer
```

### Example 2

```arturo
print every? 1..10 'x -> x < 11
; true
```

### Example 3

```arturo
print every? 1..10 [x y]-> 20 > x+y
; true
```

### Example 4

```arturo
print every? [2 3 5 7 11 14] 'x [prime? x]
; false
```

### Example 5

```arturo
print every?.with:'i ["one" "two" "three"] 'x -> 4 > (size x)-i
; true
```

## `filter`

Documentation: https://arturo-lang.io/documentation/library/iterators/filter

### Example 1

```arturo
print filter 1..10 [x][
    even? x
]
; 1 3 5 7 9
```

### Example 2

```arturo
arr: 1..10
filter 'arr 'x -> even? x
print arr
; 1 3 5 7 9
```

### Example 3

```arturo
filter [1 1 2 3 5 8 13 21] [x y]-> odd? x+y
; => [1 1 13 21]
```

### Example 4

```arturo
filter.with:'i ["zero" "one" "two" "three" "four" "five"] []-> even? i
; => ["one" "three" "five"]
```

### Example 5

```arturo
filter.first 1..10 => odd?
=> [2 3 4 5 6 7 8 9 10]

filter.first:3 1..10 => odd?
=> [2 4 6 7 8 9 10]
```

### Example 6

```arturo
filter.last 1..10 => odd?
=> [1 2 3 4 5 6 7 8 10]

filter.last:3 1..10 => odd?
=> [1 2 3 4 6 8 10]
```

### Example 7

```arturo
src: to :iterator 1..8
lazy: src | filter.iterator 'x -> even? x
to :block lazy
; => [1 3 5 7]
```

## `fold`

Documentation: https://arturo-lang.io/documentation/library/iterators/fold

### Example 1

```arturo
fold 1..10 [x,y]-> x + y
; => 55 (1+2+3+4..)

fold 1..10 .seed:1 [x,y][ x * y ]
; => 3628800 (10!)
```

### Example 2

```arturo
fold 1..3 [x,y]-> x - y
; => -6

fold.right 1..3 [x,y]-> x - y
; => 2
```

### Example 3

```arturo
fold.seed:"0" to [:string] 1..5 [x,y] ->
    "(" ++ x ++ "+" ++ y ++ ")"
; => (((((0+1)+2)+3)+4)+5)

fold.right.seed:"0" to [:string] 1..5 [x,y] ->
    "(" ++ x ++ "+" ++ y ++ ")"
; => (1+(2+(3+(4+(5+0)))))
```

### Example 4

```arturo
fold 1..10 [x y z] [
    print [x y z]
    x + z - y
]
; 0 1 2
; 1 3 4
; 2 5 6
; 3 7 8
; 4 9 10
; => 5
```

### Example 5

```arturo
fold.with:'i 1..5 [x y][
    print [i x y]
    i * x+y
]
; 0 0 1
; 1 0 2
; 2 2 3
; 3 10 4
; 4 42 5
; => 188
```

## `gather`

Documentation: https://arturo-lang.io/documentation/library/iterators/gather

### Example 1

```arturo
print gather [1 2 3 4 5 6] 'x [
    x % 2
]
; [1:[1 3 5] 0:[2 4 6]]

print gather ["New York" "Washington" "Minnesota" "Montana" "New Hampshire" "New Mexico"] 'x [
    size x
]
; [8:[New York] 10:[Washington New Mexico] 9:[Minnesota] 7:[Montana] 13:[New Hampshire]]
```

### Example 2

```arturo
gather.with:'i ["one" "two" "three" "four"] 'x -> i%2
; [0:[one three] 1:[two four]]
```

## `loop`

Documentation: https://arturo-lang.io/documentation/library/iterators/loop

### Example 1

```arturo
loop [1 2 3] 'x [
    print x
]
; 1
; 2
; 3
```

### Example 2

```arturo
loop 1..3 [x][
    print ["x =>" x]
]
; x => 1
; x => 2
; x => 3
```

### Example 3

```arturo
loop [A a B b C c] [x y][
    print [x "=>" y]
]
; A => a
; B => b
; C => c
```

### Example 4

```arturo
user: #[
    name: "John"
    surname: "Doe"
]

loop user [k v][
    print [k "=>" v]
]
; name => John
; surname => Doe
```

### Example 5

```arturo
loop.with:'i ["zero" "one" "two"] 'x [
    print ["item at:" i "=>" x]
]
; 0 => zero
; 1 => one
; 2 => two
```

### Example 6

```arturo
loop.forever [1 2 3] => print
; 1 2 3 1 2 3 1 2 3 ...
```

## `map`

Documentation: https://arturo-lang.io/documentation/library/iterators/map

### Example 1

```arturo
print map 1..5 [x][
    2*x
]
; 2 4 6 8 10
```

### Example 2

```arturo
arr: 1..5
map 'arr 'x -> 2*x
print arr
; 2 4 6 8 10
```

### Example 3

```arturo
map 1..6 [x y][
    print ["mapping" x "and" y "->" x+y]
    x+y
]
; mapping 1 and 2 -> 3
; mapping 3 and 4 -> 7
; mapping 5 and 6 -> 11
; => [3 7 11]
```

### Example 4

```arturo
map.with:'i ["one" "two" "three" "four"] 'x [
    (even? i)? -> upper x -> x
]
; => ["ONE" "two" "THREE" "four"]
```

### Example 5

```arturo
src: to :iterator 1..5
lazy: src | map.iterator 'x -> x*x
to :block lazy
; => [1 4 9 16 25]
```

### Example 6

```arturo
; .parallel, fan out one cooperative fiber per item.
; Bare flag = unbounded; integer = sliding-window cap.
results: map.parallel 1..5 'x [ pause 100 x*2 ]
; 5 fibers run concurrently; ~100ms total instead of ~500ms
; ⚠ each fiber gets a SHALLOW COPY of parent symbols;
; writes don't leak back. Return values; don't mutate
; outer state inside the body.
```

## `maximum`

Documentation: https://arturo-lang.io/documentation/library/iterators/maximum

### Example 1

```arturo
maximum 1..10 'x -> size factors.prime x
; => 8
; 8 has the maximum number of 
; prime factors: 2, 2, 2 (3)
```

### Example 2

```arturo
maximum.value 1..10 'x -> size factors.prime x
; => [8 3]
```

## `minimum`

Documentation: https://arturo-lang.io/documentation/library/iterators/minimum

### Example 1

```arturo
minimum [4 17 20] 'x -> size factors.prime x
; => 17
; 17 has the minimum number of 
; prime factors: 17 (1)
```

### Example 2

```arturo
minimum.value [4 17 20] 'x -> size factors.prime x
; => [17 1]
```

## `select`

Documentation: https://arturo-lang.io/documentation/library/iterators/select

### Example 1

```arturo
print select 1..10 [x][
    even? x
]
; 2 4 6 8 10
```

### Example 2

```arturo
arr: 1..10
select 'arr 'x -> even? x
print arr
; 2 4 6 8 10
```

### Example 3

```arturo
select [1 1 2 3 5 8 13 21] [x y]-> odd? x+y
; => [2 3 5 8]
```

### Example 4

```arturo
select.with:'i ["zero" "one" "two" "three" "four" "five"] []-> even? i
; => ["zero" "two" "four"]
```

### Example 5

```arturo
select.first 1..10 => odd?
=> [1]

select.first:3 1..10 => odd?
=> [1 3 5]
```

### Example 6

```arturo
select.last 1..10 => odd?
=> [9]

select.last:3 1..10 => odd?
=> [5 7 9]
```

### Example 7

```arturo
src: to :iterator 1..8
lazy: src | select.iterator 'x -> even? x
to :block lazy
; => [2 4 6 8]
```

## `some?`

Documentation: https://arturo-lang.io/documentation/library/iterators/some-

### Example 1

```arturo
if some? [1 3 5 6 7] 'x [even? x]
    -> print "at least one number is an even integer"
; at least one number is an even integer
```

### Example 2

```arturo
print some? 1..10 'x -> x > 9
; true
```

### Example 3

```arturo
print some? [4 6 8 10] 'x [prime? x]
; false
```

### Example 4

```arturo
print some? 1..10 [x y]-> 15 < x+y
; true
```

### Example 5

```arturo
print some? [2 4 6 9] 'x [prime? x]
; true
```

### Example 6

```arturo
print some?.with:'i ["three" "two" "one" "four" "five"] 'x -> i >= size x
; true
```
