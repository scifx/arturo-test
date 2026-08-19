# paths 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `absolute`

Documentation: https://arturo-lang.io/documentation/library/paths/absolute

### Example 1

```arturo
; we are in folder: /Users/admin/Desktop
; and have a file at: /Users/admin/Desktop/subfolder/test.txt

print absolute "../subfolder/test.txt"
; /Users/admin/subfolder/test.txt

print absolute "./test.txt"
; /Users/admin/Desktop/test.txt
```

## `absolute?`

Documentation: https://arturo-lang.io/documentation/library/paths/absolute-

### Example 1

```arturo
absolute? "/usr/bin"        ; => true
absolute? "usr/bin"         ; => false
```

## `extract`

Documentation: https://arturo-lang.io/documentation/library/paths/extract

### Example 1

```arturo
path: "/this/is/some/path.txt"

print extract.directory path        ; /this/is/some
print extract.basename path         ; path.txt
print extract.filename path         ; path
print extract.extension path        ; .txt

print extract path 
; [directory:/this/is/some basename:path.txt filename:path extension:.txt]
```

### Example 2

```arturo
url: "http://subdomain.website.com:8080/path/to/file.php?q=something#there"

print extract.scheme url            ; http
print extract.host url              ; subdomain.website.com
print extract.port url              ; 8080
print extract.user url              ; 
print extract.password url          ;
print extract.path url              ; /path/to/file.php
print extract.query url             ; q=something
print extract.anchor url            ; there

print extract url
; [scheme:http host:subdomain.website.com port:8080 user: password: path:/path/to/file.php query:q=something anchor:there]
```

### Example 3

```arturo
extract #magenta
; => [red:255 green:0 blue:255]

extract.red #FF126D
; => 255

extract.hsl #magenta
; => [hue:300 saturation:1.0 luminosity:0.5]

extract.hue #magenta
; => 300
```

## `list`

Documentation: https://arturo-lang.io/documentation/library/paths/list

### Example 1

```arturo
loop list "." 'file [
    print file
]

; tests
; var
; data.txt
```

## `normalize`

Documentation: https://arturo-lang.io/documentation/library/paths/normalize

### Example 1

```arturo
normalize "one/../two/../../three"
; => ../three

normalize "~/one/../two/../../three"
; => three
```

### Example 2

```arturo
normalize.tilde "~/one/../two/../../three"
; => /Users/three

normalize.tilde "~/Documents"
; => /Users/drkameleon/Documents
```

### Example 3

```arturo
normalize.executable "myscript"
; => ./myscript
```

## `relative`

Documentation: https://arturo-lang.io/documentation/library/paths/relative

### Example 1

```arturo
; we are in folder: /Users/admin/Desktop

print relative "test.txt"
; /Users/admin/Desktop/test.txt
```
