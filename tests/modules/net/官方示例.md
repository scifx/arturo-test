# net 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `browse`

Documentation: https://arturo-lang.io/documentation/library/net/browse

### Example 1

```arturo
browse "https://arturo-lang.io"
; opens Arturo's official website in a new browser window
```

## `download`

Documentation: https://arturo-lang.io/documentation/library/net/download

### Example 1

```arturo
download "https://github.com/arturo-lang/arturo/raw/master/logo.png"
; (downloads file as "logo.png")
```

### Example 2

```arturo
download.as:"arturoLogo.png"
            "https://github.com/arturo-lang/arturo/raw/master/logo.png"

; (downloads file with a different name)
```

## `mail`

Documentation: https://arturo-lang.io/documentation/library/net/mail

### Example 1

```arturo
mail .using: #[
            server: "mymailserver.com"
            username: "myusername"
            password: "mypass123"
        ]
        "recipient@somemail.com" "Hello from Arturo" "Arturo rocks!"
```

## `request`

Documentation: https://arturo-lang.io/documentation/library/net/request

### Example 1

```arturo
print request "https://httpbin.org/get" #[some:"arg" another: 123]
; [version:1.1 body:{
;     "args": {
;          "another": "123", 
;          "some": "arg"
;     }, 
;     "headers": {
;          "Content-Length": "0", 
;          "Host": "httpbin.org", 
;          "User-Agent": "Arturo HTTP Client / 0.9.75", 
;          "X-Amzn-Trace-Id": "Root=1-608fd4b2-6b8a34291cc2fbd17a678b0f"
;     }, 
;     "origin": "92.59.209.80", 
;     "url": "https://httpbin.org/get?some=arg&another=123"
; } headers:[server:gunicorn/19.9.0 content-length:341 access-control-allow-credentials:true content-type:application/json date:2021-05-03T10:47:14+02:00 access-control-allow-origin:* connection:keep-alive] status:200]
```

### Example 2

```arturo
r: request "https://httpbin.org/get" #[some:"arg" another: 123]
body: read.json r\body
inspect body\headers
; [ :dictionary
;       Content-Length   :	0 :string
;       Host             :	httpbin.org :string
;       User-Agent       :	Arturo HTTP Client / 0.9.75 :string
;       X-Amzn-Trace-Id  :	Root=1-608fd5f3-7e47203117863c111a3aef3b :string
; ]
```

### Example 3

```arturo
print (request "https://httpbin.org/get" #[]) \ 'status
; 200
```

### Example 4

```arturo
print request.post "https://httpbin.org/post" #[some:"arg" another: 123]
; ...same as above...
```

### Example 5

```arturo
; stream a large response: we get the headers immediately,
; and `\body` is a lazy iterator of lines
r: request.stream "https://example.com/big.txt" ø
print r\status
loop r\body 'line -> print line
```

### Example 6

```arturo
; consume an AI/SSE token stream as it is generated.
; a `text/event-stream` response is decoded into events
; automatically, and JSON payloads land ready-made in `\json`
r: request.stream.post.json
     "https://api.openai.com/v1/chat/completions"
     #[model: "gpt-4o" stream: true messages: @[#[role:"user" content:"hi"]]]

loop r\body 'ev [
    if ev\data <> "[DONE]" ->
        prints ev\json\choices\0\delta\content
]
```

### Example 7

```arturo
; each event is #[event: data: id: retry: json:]
; `data` is always the raw string, `json` is :null if it isn't JSON
loop r\body 'ev ->
    print [ev\event "->" ev\json\type]
```

### Example 8

```arturo
; opt out of the automatic decoding and get raw lines back
r: request.stream.lines "https://example.com/sse" ø
```

### Example 9

```arturo
; stop early - the connection is closed for us
r: request.stream "https://example.com/endless" ø
print take r\body 5
unplug r\body
```

## `serve`

Documentation: https://arturo-lang.io/documentation/library/net/serve

### Example 1

```arturo
serve .port: 9000 [

    ; simple static routes
    GET "/"             -> "Welcome to my site!"
    GET "/about"        -> "About us"

    ; regex route with a named capture group
    GET {//user/(?<name>[a-z]+)/}  $[name][ 
        emit.html ~"Hello, |name|!" 
    ]

    ; POST with JSON body
    POST "/login"  $[username, password][
        emit.json write.json #[
            msg: ~"Welcome back, |username|!"
        ] ø
    ]

    GET {//.*/}         -> "catch-all fallback"
]

; $> curl localhost:9000/
; Welcome to my site!%

; $> curl localhost:9000/about
; About us%

; $> curl localhost:9000/user/john
; Hello, john!%

; $> curl -X POST localhost:9000/login -d "username=admin&password=secret"
; {
;     "msg": "Welcome back, admin!"
; }%

; $>  curl localhost:9000/something-else
; catch-all fallback%
```

### Example 2

```arturo
serve $[req][
    inspect req
    ;[ :dictionary
    ;    method   :        GET :string
    ;    path     :        / :string
    ;    uri      :        / :string
    ;    body     :         :string
    ;    query    :        [ :dictionary
    ;    ]
    ;    headers  :        [ :dictionary
    ;        ...
    ;    ]

    ; we have to return either a string
    ; or a dictionary like:
    #[
        body: "..."
        status: 200
        headers: #[
            ;...
        ]
    ]
]
```
