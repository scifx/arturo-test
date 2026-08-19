# sockets 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `accept`

Documentation: https://arturo-lang.io/documentation/library/sockets/accept

### Example 1

```arturo
server: listen 18966
print "started server connection..."

client: accept server
print ["accepted incoming connection from:" client]
```

## `connect`

Documentation: https://arturo-lang.io/documentation/library/sockets/connect

### Example 1

```arturo
; connect to local server on port 18966
server: connect 18966
```

### Example 2

```arturo
; "connect" to a udp server on port 12345
server: connect.udp 12345
```

### Example 3

```arturo
; connect to a remote server on port 18966
server: connect.to:"123.456.789.123" 18966
```

### Example 4

```arturo
; parallel connect to many hosts
tasks: map hosts 'h -> connect.async.to: h 80
sockets: wait.all tasks
```

## `listen`

Documentation: https://arturo-lang.io/documentation/library/sockets/listen

### Example 1

```arturo
; start a server listening on port 18966
server: listen 18966
```

## `receive`

Documentation: https://arturo-lang.io/documentation/library/sockets/receive

### Example 1

```arturo
client: accept server
message: receive client
```

### Example 2

```arturo
; with deadline
t: receive.async client
r: wait.timeout: 5000 t      ; :error on timeout
```

### Example 3

```arturo
; from a channel
Jobs: channel 'jobs
v: receive Jobs              ; parks until something sent
```

## `send`

Documentation: https://arturo-lang.io/documentation/library/sockets/send

### Example 1

```arturo
; connect to a local server on port 256
socket: connect.to:"localhost" 256

; send a message to the server
send socket "Hello Socket World"
```

### Example 2

```arturo
; send a value through a channel
Jobs: channel 'jobs
send Jobs 42
```

## `send?`

Documentation: https://arturo-lang.io/documentation/library/sockets/send-

### Example 1

```arturo
; connect to a local server on port 256
socket: connect.to:"localhost" 256

; send a message to the server
; and check if it was successful
sent?: send? socket "Hello Socket World"

print ["Message was sent successfully:" sent?]
```

## `unplug`

Documentation: https://arturo-lang.io/documentation/library/sockets/unplug

### Example 1

```arturo
; connect to a local server on port 256
socket: connect.to:"localhost" 256

; send a message to the server
send socket "Hello Socket World"

; disconnect from the server
unplug socket
```

### Example 2

```arturo
; close a channel, parked recvs wake with :null, sends fail
Jobs: channel 'jobs
unplug Jobs
```

### Example 3

```arturo
; stop pulling from a stream and release what's behind it
; (here: terminate the child process)
s: execute.stream "yes"
print take s 3
unplug s
```
