# crypto 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `crc`

Documentation: https://arturo-lang.io/documentation/library/crypto/crc

### Example 1

```arturo
print crc "The quick brown fox jumps over the lazy dog"
; 414FA339
```

## `decode`

Documentation: https://arturo-lang.io/documentation/library/crypto/decode

### Example 1

```arturo
print decode "TnVtcXVhbSBmdWdpZW5zIHJlc3BleGVyaXM="
; Numquam fugiens respexeris
```

### Example 2

```arturo
print decode.url "http%3A%2F%2Ffoo+bar%2F"
; http://foo bar/
```

## `digest`

Documentation: https://arturo-lang.io/documentation/library/crypto/digest

### Example 1

```arturo
print digest "Hello world"
; 3e25960a79dbc69b674cd4ec67a72c62
```

### Example 2

```arturo
print digest.sha "Hello world"
; 7b502c3a1f48c8609ae212cdfb639dee39673f5e
```

## `encode`

Documentation: https://arturo-lang.io/documentation/library/crypto/encode

### Example 1

```arturo
print encode "Numquam fugiens respexeris"
; TnVtcXVhbSBmdWdpZW5zIHJlc3BleGVyaXM=
```

### Example 2

```arturo
print encode.url "http://foo bar/"
; http%3A%2F%2Ffoo+bar%2F
```

## `hash`

Documentation: https://arturo-lang.io/documentation/library/crypto/hash

### Example 1

```arturo
print hash "hello"      ; 613153351
print hash [1 2 3]      ; 645676735036410
print hash 123          ; 123

a: [1 2 3]
b: [1 2 3]
print (hash a)=(hash b) ; true
```
