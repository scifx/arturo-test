# files 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `copy`

Documentation: https://arturo-lang.io/documentation/library/files/copy

### Example 1

```arturo
copy "testscript.art" normalize.tilde "~/Desktop/testscript.art"
; copied file
```

### Example 2

```arturo
copy "testfolder" normalize.tilde "~/Desktop/testfolder"
; copied whole folder
```

## `delete`

Documentation: https://arturo-lang.io/documentation/library/files/delete

### Example 1

```arturo
delete "testscript.art"
; file deleted
```

## `directory?`

Documentation: https://arturo-lang.io/documentation/library/files/directory-

### Example 1

```arturo
if directory? "src" [ 
    print "directory exists!" 
]
```

## `exists?`

Documentation: https://arturo-lang.io/documentation/library/files/exists-

### Example 1

```arturo
if exists? "somefile.txt" [ 
    print "path exists!" 
]
```

## `file?`

Documentation: https://arturo-lang.io/documentation/library/files/file-

### Example 1

```arturo
if file? "somefile.txt" [ 
    print "file exists!" 
]
```

## `hidden?`

Documentation: https://arturo-lang.io/documentation/library/files/hidden-

### Example 1

```arturo
hidden? "README.md"     ; => false
hidden? ".git"          ; => true
```

## `move`

Documentation: https://arturo-lang.io/documentation/library/files/move

### Example 1

```arturo
move "testscript.art" normalize.tilde "~/Desktop/testscript.art"
; moved file
```

### Example 2

```arturo
move "testfolder" normalize.tilde "~/Desktop/testfolder"
; moved whole folder
```

## `permissions`

Documentation: https://arturo-lang.io/documentation/library/files/permissions

### Example 1

```arturo
inspect permissions "bin/arturo"
; [ :dictionary
;     user    :	[ :dictionary
;         read     :		true :boolean
;         write    :		true :boolean
;         execute  :		true :boolean
;     ]
;     group   :	[ :dictionary
;         read     :		true :boolean
;         write    :		false :boolean
;         execute  :		true :boolean
;     ]
;     others  :	[ :dictionary
;         read     :		true :boolean
;         write    :		false :boolean
;         execute  :		true :boolean
;     ]
; ]
```

### Example 2

```arturo
permissions.set:#[others:#[write:true]] "bin/arturo"
; gave write permission to 'others'
```

## `read`

Documentation: https://arturo-lang.io/documentation/library/files/read

### Example 1

```arturo
; reading a simple local file
str: read "somefile.txt"
```

### Example 2

```arturo
; also works with remote urls
page: read "http://www.somewebsite.com/page.html"
```

### Example 3

```arturo
; we can also "read" JSON data as an object
data: read.json "mydata.json"
```

### Example 4

```arturo
; lazily stream lines from a local file
lines: read.lines.stream "somefile.txt"
head: take lines 10
```

### Example 5

```arturo
; lazily stream csv rows
rows: read.csv.stream "table.csv"
first rows
```

### Example 6

```arturo
; read fixed-size text buffers lazily
chunks: read.buffer:4 "somefile.txt"
first chunks
```

### Example 7

```arturo
; begin reading from a specific byte offset
later: read.buffer:4.seek:8 "somefile.txt"
first later
```

### Example 8

```arturo
; read fixed-size binary buffers lazily
bytes: read.binary.buffer:1024 "image.bin"
first bytes
```

### Example 9

```arturo
; or even convert Markdown to HTML on-the-fly
html: read.markdown "## Hello"     ; "<h2>Hello</h2>"
```

## `rename`

Documentation: https://arturo-lang.io/documentation/library/files/rename

### Example 1

```arturo
rename "README.md" "READIT.md"
; file renamed
```

## `symlink`

Documentation: https://arturo-lang.io/documentation/library/files/symlink

### Example 1

```arturo
symlink relative "arturo/README.md" 
        "/Users/drkameleon/Desktop/gotoREADME.md"
; creates a symbolic link to our readme file
; in our desktop
```

### Example 2

```arturo
symlink.hard relative "arturo/README.md" 
        "/Users/drkameleon/Desktop/gotoREADME.md"
; hard-links (effectively copies) our readme file
; to our desktop
```

## `symlink?`

Documentation: https://arturo-lang.io/documentation/library/files/symlink-

### Example 1

```arturo
if symlink? "somefile" [ 
    print "symlink exists!" 
]
```

## `timestamp`

Documentation: https://arturo-lang.io/documentation/library/files/timestamp

### Example 1

```arturo
timestamp "README.md"
; =>  [created:2022-09-21T12:35:04+02:00 accessed:2022-09-21T12:35:04+02:00 modified:2022-09-21T12:35:04+02:00]

timestamp "some-file-that-does-not-exist.txt"
; => null
```

## `unzip`

Documentation: https://arturo-lang.io/documentation/library/files/unzip

### Example 1

```arturo
unzip "folder" "archive.zip"
```

## `volume`

Documentation: https://arturo-lang.io/documentation/library/files/volume

### Example 1

```arturo
volume "README.md"
; => 13704B 
; (size in bytes)
```

## `write`

Documentation: https://arturo-lang.io/documentation/library/files/write

### Example 1

```arturo
; write some string data to given file path
write "Hello world!" "somefile.txt"
```

### Example 2

```arturo
; we can also write any type of data as JSON
write.json myData "data.json"
```

### Example 3

```arturo
; append to an existing file
write.append "Yes, Hello again!" "somefile.txt"
```

### Example 4

```arturo
; stream text chunks to disk
chunks: read.buffer:4 "source.txt"
write.buffer:4 chunks "copy.txt"
```

### Example 5

```arturo
; overwrite from a specific byte offset
write.buffer:2.seek:4 ["XY" "ZZ"] "copy.txt"
```

### Example 6

```arturo
; stream binary chunks to disk
bytes: read.binary.buffer:1024 "image.bin"
write.binary.buffer:1024 bytes "copy.bin"
```

## `zip`

Documentation: https://arturo-lang.io/documentation/library/files/zip

### Example 1

```arturo
zip "dest.zip" ["file1.txt" "img.png"]
```
