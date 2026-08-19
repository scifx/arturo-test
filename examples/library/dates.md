# dates 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `after`

Documentation: https://arturo-lang.io/documentation/library/dates/after

### Example 1

```arturo
print now
; 2021-03-22T11:25:30+01:00

print after.weeks:2 now
; 2021-04-05T11:25:42+02:00
```

## `before`

Documentation: https://arturo-lang.io/documentation/library/dates/before

### Example 1

```arturo
print now
; 2021-03-22T11:27:00+01:00

print before.weeks:2 now
; 2021-03-08T11:27:14+01:00

print before.years:1 now
; 2020-03-22T11:27:23+01:00
```

## `friday?`

Documentation: https://arturo-lang.io/documentation/library/dates/friday-

### Example 1

```arturo
print friday? now       ; false
```

## `future?`

Documentation: https://arturo-lang.io/documentation/library/dates/future-

### Example 1

```arturo
futureDate: after.weeks:2 now

print future? now           ; false
print future? futureDate    ; true
```

## `leap?`

Documentation: https://arturo-lang.io/documentation/library/dates/leap-

### Example 1

```arturo
print leap? now     ; false

print map 2019..2021 => leap? 
; false true false
```

## `monday?`

Documentation: https://arturo-lang.io/documentation/library/dates/monday-

### Example 1

```arturo
print sunday? now       ; false
```

## `now`

Documentation: https://arturo-lang.io/documentation/library/dates/now

### Example 1

```arturo
print now           ; 2020-10-23T14:16:13+02:00

time: now
inspect time

; [ :date
;       hour        : 14 :integer
;       minute      : 16 :integer
;       second      : 55 :integer
;       nanosecond  : 82373000 :integer
;       day         : 23 :integer
;       Day         : Friday :string
;       month       : 10 :integer
;       Month       : October :string
;       year        : 2020 :integer
;       utc         : -7200 :integer
; ]

print now\year      ; 2020
```

## `past?`

Documentation: https://arturo-lang.io/documentation/library/dates/past-

### Example 1

```arturo
pastDate: before.weeks:2 now
futureDate: after.weeks:1 now

print past? futureDate      ; false
print past? pastDate        ; true

print past? now             ; true ("now" has already become past...)
```

## `saturday?`

Documentation: https://arturo-lang.io/documentation/library/dates/saturday-

### Example 1

```arturo
print saturday? now     ; false
```

## `sunday?`

Documentation: https://arturo-lang.io/documentation/library/dates/sunday-

### Example 1

```arturo
print sunday? now       ; false
```

## `thursday?`

Documentation: https://arturo-lang.io/documentation/library/dates/thursday-

### Example 1

```arturo
print thursday? now     ; false
```

## `today?`

Documentation: https://arturo-lang.io/documentation/library/dates/today-

### Example 1

```arturo
print today? now                    ; true

print today? after.hours: 24 now    ; false
```

## `tuesday?`

Documentation: https://arturo-lang.io/documentation/library/dates/tuesday-

### Example 1

```arturo
print tuesday? now      ; true
```

## `wednesday?`

Documentation: https://arturo-lang.io/documentation/library/dates/wednesday-

### Example 1

```arturo
print wednesday? now    ; false
```
