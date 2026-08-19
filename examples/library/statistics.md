# statistics 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `average`

Documentation: https://arturo-lang.io/documentation/library/statistics/average

### Example 1

```arturo
print average [2 4 5 6 7 2 3]
; 4.142857142857143
```

## `deviation`

Documentation: https://arturo-lang.io/documentation/library/statistics/deviation

### Example 1

```arturo
arr:  [1 2 3 4]
arr2: [3 120 4 7 87 2 6 34]

print deviation arr         ; 1.118033988749895
print deviation arr2        ; 42.70959347734417

deviation.sample arr        ; => 1.290994448735806
deviation.sample arr2       ; => 45.65847597731914
```

## `kurtosis`

Documentation: https://arturo-lang.io/documentation/library/statistics/kurtosis

### Example 1

```arturo
arr:  [1 2 3 4]
arr2: [3 120 4 7 87 2 6 34]

print kurtosis arr          ; -1.36
print kurtosis arr2         ; -0.3863717894076322

kurtosis.sample arr         ; => -1.200000000000001
kurtosis.sample arr2        ; => 0.5886192422439724
```

## `median`

Documentation: https://arturo-lang.io/documentation/library/statistics/median

### Example 1

```arturo
print median [2 4 5 6 7 2 3]
; 6

print median [1 5 2 3 4 7 9 8]
; 3.5
```

## `skewness`

Documentation: https://arturo-lang.io/documentation/library/statistics/skewness

### Example 1

```arturo
arr:  [1 2 3 4]
arr2: [3 120 4 7 87 2 6 34]

print skewness arr          ; 0.0
print skewness arr2         ; 1.127950016816592

skewness.sample arr         ; => 0.0
skewness.sample arr2        ; => 1.40680083744453
```

## `variance`

Documentation: https://arturo-lang.io/documentation/library/statistics/variance

### Example 1

```arturo
arr:  [1 2 3 4]
arr2: [3 120 4 7 87 2 6 34]

print variance arr          ; 1.25
print variance arr2         ; 1824.109375

variance.sample arr         ; => 1.666666666666667
variance.sample arr2        ; => 2084.696428571428
```
