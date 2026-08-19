# databases 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `close`

Documentation: https://arturo-lang.io/documentation/library/databases/close

### Example 1

```arturo
db: open "my.db"    ; opens an SQLite database named 'my.db'

print query db "SELECT * FROM users"

close db            ; and close it
```

## `open`

Documentation: https://arturo-lang.io/documentation/library/databases/open

### Example 1

```arturo
db: open "my.db"    ; opens an SQLite database named 'my.db'
```

## `query`

Documentation: https://arturo-lang.io/documentation/library/databases/query

### Example 1

```arturo
db: open "my.db"    ; opens an SQLite database named 'my.db'

; perform a simple query
print query db "SELECT * FROM users"

; perform an INSERT query and get back the record's ID
username: "johndoe"
lastInsertId: query.id db ~{!sql INSERT INTO users (name) VALUES ('|username|')}

; perform a safe query with given parameters
print query db .with: ["johndoe"] {!sql SELECT * FROM users WHERE name = ?}
```

## `store`

Documentation: https://arturo-lang.io/documentation/library/databases/store

### Example 1

```arturo
; create a new store with the name `mystore`
; it will be automatically live-stored in a file in the same folder
; using the native Arturo format
data: store "mystore"

; store some data
data\name: "John"
data\surname: "Doe"
data\age: 36

; and let's retrieve our data
data
; => [name:"John" surname:"Doe" age:36]
```

### Example 2

```arturo
; create a new "global" configuration store
; that will be saved automatically in ~/.arturo/stores
globalStore: store.global "configuration"

; we are now ready to add or retrieve some persistent data!
```

### Example 3

```arturo
; create a new JSON store with the name `mystore`
; it will be automatically live-stored in a file in the same folder
; with the name `mystore.json`
data: store.json "mystore"

; store some data
da\people: []

; data can be as complicated as in any normal dictionary
da\people: da\people ++ #[name: "John" surname: "Doe"]

; check some specific store value
da\people\0\name
; => "John"
```

### Example 4

```arturo
; create a new deferred store with the name `mystore`
; it will be automatically saved in a file in the same folder
; using the native Arturo format
defStore: store.deferred "mystore"

; let's save some data
defStore\name: "John"
defStore\surname: "Doe"

; and print it
print defStore
; [name:John surname:Doe]

; in this case, all data is available at any given moment
; but will not be saved to disk for each and every operation;
; instead, it will be saved in its totality just before
; the program terminates!
```
